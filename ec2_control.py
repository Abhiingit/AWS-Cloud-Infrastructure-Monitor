#starting an instance
'''import boto3

REGION = "us-east-1"
INSTANCE_ID = "i-013b626f469247014"

ec2 = boto3.client(
    "ec2",
    region_name=REGION
)

response = ec2.start_instances(
    InstanceIds=[INSTANCE_ID]
)

print("EC2 start request sent!")
print(response["StartingInstances"])'''

#stopping an instance

import boto3

REGION = "us-east-1"
INSTANCE_ID = "i-013b626f469247014"

ec2 = boto3.client(
    "ec2",
    region_name=REGION
)

response = ec2.stop_instances(
    InstanceIds=[INSTANCE_ID]
)

print("EC2 stop request sent!")
print(response["StoppingInstances"])