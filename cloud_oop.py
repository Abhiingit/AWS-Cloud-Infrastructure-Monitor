class CloudResource:

    def __init__(self, resource_id, name, region):
        self.resource_id = resource_id
        self.name = name
        self.region = region

    def show_info(self):
        print("Resource ID:", self.resource_id)
        print("Name:", self.name)
        print("Region:", self.region)

    def deploy(self):
        print("Deploying cloud resource")


class EC2Resource(CloudResource):

    def __init__(
        self,
        resource_id,
        name,
        region,
        instance_type
    ):
        super().__init__(
            resource_id,
            name,
            region
        )

        self.instance_type = instance_type

    def deploy(self):
        print("Launching EC2 instance")

    def show_info(self):
        super().show_info()
        print("Instance Type:", self.instance_type)


class S3Resource(CloudResource):

    def __init__(
        self,
        resource_id,
        name,
        region,
        bucket_name
    ):
        super().__init__(
            resource_id,
            name,
            region
        )

        self.bucket_name = bucket_name

    def deploy(self):
        print("Creating S3 bucket")

    def show_info(self):
        super().show_info()
        print("Bucket Name:", self.bucket_name)


class LambdaResource(CloudResource):

    def __init__(
        self,
        resource_id,
        name,
        region,
        runtime
    ):
        super().__init__(
            resource_id,
            name,
            region
        )

        self.runtime = runtime

    def deploy(self):
        print("Deploying Lambda function")

    def show_info(self):
        super().show_info()
        print("Runtime:", self.runtime)


# Create objects

ec2 = EC2Resource(
    "i-12345",
    "WebServer",
    "ap-south-1",
    "t2.micro"
)

s3 = S3Resource(
    "s3-001",
    "BackupStorage",
    "ap-south-1",
    "my-backup-bucket"
)

lambda_function = LambdaResource(
    "lambda-001",
    "MyFunction",
    "ap-south-1",
    "Python 3.13"
)


# Display information

ec2.show_info()

print()

s3.show_info()

print()

lambda_function.show_info()


# Polymorphism

print("\nDeploying resources:")

resources = [
    ec2,
    s3,
    lambda_function
]

for resource in resources:
    resource.deploy()