import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ChatHistory')

def lambda_handler(event, context):

    body = json.loads(event['body'])
    user_message = body.get("message", "Hello")

    response_text = f"AI Response: You said '{user_message}'"

    table.put_item(
        Item={
            "id": str(datetime.utcnow()),
            "message": user_message,
            "response": response_text
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": response_text
        })
    }
