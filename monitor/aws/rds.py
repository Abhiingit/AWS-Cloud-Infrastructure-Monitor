from monitor.models import RDSSummary


def collect_rds_summary(rds_client) -> RDSSummary:
    summary = RDSSummary()

    paginator = rds_client.get_paginator("describe_db_instances")

    for page in paginator.paginate():
        for instance in page.get("DBInstances", []):
            summary.total += 1

            status = instance.get("DBInstanceStatus", "unknown")

            if status == "available":
                summary.available += 1
            else:
                summary.other += 1

    return summary
