from monitor.models import InfrastructureReport


def get_overall_status(report: InfrastructureReport) -> str:
    if report.cloudwatch.alarm > 0:
        return "ATTENTION REQUIRED"

    if report.cloudwatch.insufficient_data > 0:
        return "ATTENTION REQUIRED"

    if report.rds.other > 0:
        return "ATTENTION REQUIRED"

    return "HEALTHY"