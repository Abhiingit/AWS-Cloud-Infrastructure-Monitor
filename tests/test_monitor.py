from unittest.mock import Mock

from monitor.aws.cloudwatch import collect_cloudwatch_summary
from monitor.aws.ec2 import collect_ec2_summary
from monitor.aws.rds import collect_rds_summary
from monitor.aws.s3 import collect_s3_summary
from monitor.health import get_overall_status
from monitor.models import (
    CloudWatchSummary,
    CostSummary,
    EC2Summary,
    InfrastructureReport,
    RDSSummary,
    S3Summary,
)


def test_ec2_summary():
    client = Mock()
    paginator = Mock()
    paginator.paginate.return_value = [
        {
            "Reservations": [
                {
                    "Instances": [
                        {"State": {"Name": "running"}},
                        {"State": {"Name": "stopped"}},
                        {"State": {"Name": "pending"}},
                    ]
                }
            ]
        }
    ]
    client.get_paginator.return_value = paginator

    result = collect_ec2_summary(client)

    assert result.total == 3
    assert result.running == 1
    assert result.stopped == 1
    assert result.other == 1


def test_s3_summary():
    client = Mock()
    client.list_buckets.return_value = {
        "Buckets": [
            {"Name": "bucket-one"},
            {"Name": "bucket-two"},
        ]
    }

    result = collect_s3_summary(client)

    assert result.total == 2


def test_rds_summary():
    client = Mock()
    paginator = Mock()
    paginator.paginate.return_value = [
        {
            "DBInstances": [
                {"DBInstanceStatus": "available"},
                {"DBInstanceStatus": "stopped"},
            ]
        }
    ]
    client.get_paginator.return_value = paginator

    result = collect_rds_summary(client)

    assert result.total == 2
    assert result.available == 1
    assert result.other == 1


def test_cloudwatch_summary():
    client = Mock()
    paginator = Mock()
    paginator.paginate.return_value = [
        {
            "MetricAlarms": [
                {"StateValue": "OK"},
                {"StateValue": "ALARM"},
                {"StateValue": "INSUFFICIENT_DATA"},
            ]
        }
    ]
    client.get_paginator.return_value = paginator

    result = collect_cloudwatch_summary(client)

    assert result.total == 3
    assert result.ok == 1
    assert result.alarm == 1
    assert result.insufficient_data == 1


def test_health_status():
    report = InfrastructureReport(
        region="ap-south-1",
        ec2=EC2Summary(),
        s3=S3Summary(),
        rds=RDSSummary(),
        cloudwatch=CloudWatchSummary(insufficient_data=1),
        cost=CostSummary(total=0.0),
    )

    assert get_overall_status(report) == "ATTENTION REQUIRED"
