from app.config.config import settings
from app.schemas.email import Email
import boto3
from botocore.exceptions import ClientError


def send_notification(email: Email):
    client = boto3.client('ses', aws_access_key_id=settings.aws_access_key,
                          aws_secret_access_key=settings.aws_secret_key, region_name=settings.aws_region)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': email.receipts,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': email.message,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': email.subject,
                },
            },
            Source=settings.email_sender,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])