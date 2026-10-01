from monitor.models import EC2Summary


def collect_ec2_summary(ec2_client) -> EC2Summary:
    summary = EC2Summary()

    paginator = ec2_client.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                summary.total += 1

                state = instance.get("State", {}).get("Name", "unknown")

                if state == "running":
                    summary.running += 1
                elif state == "stopped":
                    summary.stopped += 1
                else:
                    summary.other += 1

    return summary
