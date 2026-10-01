from monitor.health import get_overall_status
from monitor.models import InfrastructureReport


def render_console_report(report: InfrastructureReport) -> str:
    status = get_overall_status(report)

    lines = [
        "",
        "AWS CLOUD INFRASTRUCTURE MONITOR",
        "=" * 50,
        "",
        f"Region        : {report.region}",
        f"Overall Status: {status}",
        "",
        "EC2",
        "-" * 50,
        f"Total instances : {report.ec2.total}",
        f"Running         : {report.ec2.running}",
        f"Stopped         : {report.ec2.stopped}",
        f"Other states    : {report.ec2.other}",
        "",
        "S3",
        "-" * 50,
        f"Buckets         : {report.s3.total}",
        "",
        "RDS",
        "-" * 50,
        f"Total instances : {report.rds.total}",
        f"Available       : {report.rds.available}",
        f"Other states    : {report.rds.other}",
        "",
        "CloudWatch Alarms",
        "-" * 50,
        f"Total             : {report.cloudwatch.total}",
        f"OK                : {report.cloudwatch.ok}",
        f"ALARM             : {report.cloudwatch.alarm}",
        f"Insufficient data : {report.cloudwatch.insufficient_data}",
        "",
        "AWS Cost",
        "-" * 50,
    ]

    if report.cost.total is not None:
        lines.append(f"Month-to-date    : ${report.cost.total:.2f}")
    else:
        lines.append("Month-to-date    : unavailable")

    if report.cost.by_service:
        lines.extend(
            [
                "",
                "Cost by service:",
            ]
        )

        for service, amount in list(report.cost.by_service.items())[:10]:
            lines.append(f"  {service:<30} ${amount:.2f}")

    lines.extend(
        [
            "",
            "Overall Status",
            "-" * 50,
            status,
            "",
        ]
    )

    return "\n".join(lines)
