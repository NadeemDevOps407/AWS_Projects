import json
import os.path 
import boto3

def lambda_handler(event, context):
    record0s3= event["Records"][0]["s3"]
    
    bucketname= record0s3["bucket"]["name"]
    filepath = record0s3["object"]["key"]
    filesize = record0s3["object"]["size"]
    folder = os.path.dirname(filepath)
    
    if folder == "":
        folder = "<Empty>"
    dynamo = boto3.resource("dynamodb").Table("mytabl07") #replace "mytabl07" with your table you create in Dynamodb
    dynamo.put_item(Item={"folder":folder, "filename":filepath, "filesize":filesize, "bucketname":bucketname})
    
    print(bucketname)
    print(filepath)
    print(filesize)
    print(folder)
    # TODO implement
    return {
        'statusCode': 200, 
        'body': json.dumps(record0s3)
    }
