import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

print("Boto3 connected to AWS successfully!")