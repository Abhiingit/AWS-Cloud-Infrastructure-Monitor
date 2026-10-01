import boto3


# --------------------------------
# Configuration
# --------------------------------

REGION = "ap-south-1"

TARGET_GROUP_ARN = (
    "YOUR_TARGET_GROUP_ARN"
)

SNS_TOPIC_ARN = (
    "YOUR_SNS_TOPIC_ARN"
)


# --------------------------------
# AWS clients
# --------------------------------

elbv2 = boto3.client(
    "elbv2",
    region_name=REGION
)

sns = boto3.client(
    "sns",
    region_name=REGION
)


# --------------------------------
# Check target health
# --------------------------------

response = elbv2.describe_target_health(
    TargetGroupArn=TARGET_GROUP_ARN
)


# --------------------------------
# Check every target
# --------------------------------

for target in response["TargetHealthDescriptions"]:

    instance_id = target["Target"]["Id"]

    health = target["TargetHealth"]

    state = health["State"]

    reason = health.get(
        "Reason",
        "No reason provided"
    )

    print(
        f"Instance: {instance_id}"
    )

    print(
        f"Status: {state}"
    )

    print(
        f"Reason: {reason}"
    )

    print("-" * 40)


    # --------------------------------
    # Alert if unhealthy
    # --------------------------------

    if state == "unhealthy":

        message = (
            f"ALERT!\n\n"
            f"Target Group health check failed.\n\n"
            f"Instance ID: {instance_id}\n"
            f"Status: {state}\n"
            f"Reason: {reason}\n"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="ALB Target Unhealthy",
            Message=message
        )

        print(
            "SNS alert sent!"
        )