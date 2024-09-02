from blissmotors_backend.settings import project_id
import dialogflow_v2 as dialogflow
from google.protobuf.json_format import MessageToDict, MessageToJson
from .models import Message
import json

def detect_intent_texts(data):
    print(data)

    session_id = data['session_id']
    username = data.get('username', '')
    texts = json.loads(data.get('message'))['messages']
    language_code = data.get('language_code', 'en-US')

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        # print(response)
        response_dict = MessageToDict(response)

        messages = response_dict['queryResult']['fulfillmentMessages']
        new_message = Message()
        new_message.direction = 'outgoing'
        new_message.dialogflow_resp = MessageToJson(response)
        new_message.message = json.dumps({'messages': messages})
        new_message.username = username

        return response_dict['queryResult']['fulfillmentText']