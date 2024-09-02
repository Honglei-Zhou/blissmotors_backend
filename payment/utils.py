import stripe
from blissmotors_backend.settings import stripe_key
from django.core.mail import EmailMessage


def process_payment(payment_data):
    stripe.api_key = stripe_key

    print(int(payment_data['price']))
    charge = stripe.Charge.create(
        amount=round(float(payment_data['price']) * 100),
        currency='usd',
        source=payment_data['token'],
        description='From: {}, Pay for: Service fee, Bliss Motors LLC'.format(payment_data['email']),
        receipt_email=payment_data['email']
    )

    mail_subject = 'Bliss Lease Order Confirmation'
    message = 'Hi\n' \
              'Thank you for placing your order, our team will be in touch shortly.\n' \
              '\n'\
              'Annie Adams\n'\
              'VP of CustomerCare'

    to_email = payment_data['email']

    if to_email is None or to_email == '':
        return charge

    from_email = 'Annie Adams <customercare@blissmotors.com>'
    customer_care = 'customercare@blissmotors.com'

    email = EmailMessage(
        mail_subject, message, from_email=from_email, to=[to_email, customer_care]
    )
    email.send()

    return charge
