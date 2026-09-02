import subprocess
import json
import os

# Find the folder where this Python script is located
terraform_directory = os.path.dirname(os.path.abspath(__file__))

result = subprocess.run(
    ["terraform", "output", "-json"],
    cwd=terraform_directory,
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("Terraform command failed!")
    print(result.stderr)
    exit(1)

outputs = json.loads(result.stdout)

ec2_id = outputs["ec2_instance_id"]["value"]
bucket_name = outputs["s3_bucket_name"]["value"]

print("Terraform outputs:")
print("------------------")
print("EC2 Instance ID:", ec2_id)
print("S3 Bucket Name:", bucket_name)