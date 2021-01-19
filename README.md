Below are the steps to set up SNS notification when a production EC2 server abruptly stops

Step 1 : Create a Lambda function using python boto3

step 2 : Set IAM Role for Lambda FUnction to have access to the EC2 and SNS service.

step 3 : Create a SNS Topic and create subscription and choose Email as the protocol and mention the endpoint email address.

step 4 : Make note of  the ARN of the SNS Topic and use it in the lambda function so that the SNS topic is invoked when the lambda function runs.

step 5 : Go to Cloud Watch and create a Event based rule so that the desired Lambda function is trigerred when the event occurs.



