from monitor.models import CloudWatchSummary


def collect_cloudwatch_summary(cloudwatch_client) -> CloudWatchSummary:
    summary = CloudWatchSummary()

    paginator = cloudwatch_client.get_paginator("describe_alarms")

    for page in paginator.paginate():
        for alarm in page.get("MetricAlarms", []):
            summary.total += 1

            state = alarm.get("StateValue", "UNKNOWN")

            if state == "OK":
                summary.ok += 1
            elif state == "ALARM":
                summary.alarm += 1
            elif state == "INSUFFICIENT_DATA":
                summary.insufficient_data += 1
            else:
                summary.other += 1

    return summary
