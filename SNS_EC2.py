import json
import boto3
def lambda_handler(event, context):
    sns_client=boto3.client("sns","us-east-1")
    
    sns_client.publish(TargetArn="arn:aws:sns:us-east-1:638644014481:Status_of_EC2",Message="EC2 Instance is in stopped status")
