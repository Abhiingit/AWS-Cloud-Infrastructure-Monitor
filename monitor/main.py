from __future__ import annotations

import os

import boto3

from monitor.aws.cloudwatch import collect_cloudwatch_summary
from monitor.aws.costs import collect_cost_summary
from monitor.aws.ec2 import collect_ec2_summary
from monitor.aws.rds import collect_rds_summary
from monitor.aws.s3 import collect_s3_summary
from monitor.config import settings
from monitor.models import InfrastructureReport
from monitor.reports.console import render_console_report
from monitor.reports.json_report import write_json_report


def build_report() -> InfrastructureReport:
    session = boto3.Session(region_name=settings.aws_region)

    ec2_client = session.client("ec2")
    s3_client = session.client("s3")
    rds_client = session.client("rds")
    cloudwatch_client = session.client("cloudwatch")
    cost_client = session.client("ce", region_name="us-east-1")

    return InfrastructureReport(
        region=settings.aws_region,
        ec2=collect_ec2_summary(ec2_client),
        s3=collect_s3_summary(s3_client),
        rds=collect_rds_summary(rds_client),
        cloudwatch=collect_cloudwatch_summary(cloudwatch_client),
        cost=collect_cost_summary(cost_client),
    )


def main() -> None:
    report = build_report()

    print(render_console_report(report))

    output_path = os.path.join(
        "monitor",
        "reports",
        "latest.json",
    )

    write_json_report(report, output_path)

    print(f"JSON report written to: {output_path}")


if __name__ == "__main__":
    main()
