import boto3

REGION = "ap-south-1"

INSTANCE_ID = "i-0123456789abcdef"

EMAIL = "your-email@example.com"

SNS_TOPIC_NAME = "cloud-practical-cpu-alerts"

ALARM_NAME = "cloud-practical-ec2-high-cpu"


# -----------------------------------
# 1. Create SNS client
# -----------------------------------

sns = boto3.client(
    "sns",
    region_name=REGION
)


# -----------------------------------
# 2. Create SNS topic
# -----------------------------------

topic_response = sns.create_topic(
    Name=SNS_TOPIC_NAME
)

topic_arn = topic_response["TopicArn"]

print("SNS Topic created:")
print(topic_arn)


# -----------------------------------
# 3. Subscribe email
# -----------------------------------

sns.subscribe(
    TopicArn=topic_arn,
    Protocol="email",
    Endpoint=EMAIL
)

print("Email subscription created.")
print("Check your email and confirm the SNS subscription.")


# -----------------------------------
# 4. Create CloudWatch client
# -----------------------------------

cloudwatch = boto3.client(
    "cloudwatch",
    region_name=REGION
)


# -----------------------------------
# 5. Create CloudWatch alarm
# -----------------------------------

cloudwatch.put_metric_alarm(

    AlarmName=ALARM_NAME,

    AlarmDescription=(
        "Alarm when EC2 CPU utilization "
        "exceeds 70%"
    ),

    Namespace="AWS/EC2",

    MetricName="CPUUtilization",

    Dimensions=[
        {
            "Name": "InstanceId",
            "Value": INSTANCE_ID
        }
    ],

    Statistic="Average",

    Period=300,

    EvaluationPeriods=1,

    Threshold=70.0,

    ComparisonOperator="GreaterThanThreshold",

    ActionsEnabled=True,

    AlarmActions=[
        topic_arn
    ]
)


print("CloudWatch alarm created successfully!")

print()
print("Alarm:", ALARM_NAME)
print("Threshold: CPU > 70%")
print("Period: 5 minutes")
print("SNS:", topic_arn)