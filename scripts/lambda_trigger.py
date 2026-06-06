import json

def lambda_handler(event, context):

    print("New file received in S3")

    response = {
        "statusCode": 200,
        "message": "Glue ETL Job Triggered Successfully"
    }

    return response
