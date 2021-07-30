import json
from main import run


def lambda_handler(event, context):
    run()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
