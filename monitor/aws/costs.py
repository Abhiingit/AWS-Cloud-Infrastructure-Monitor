from datetime import datetime, timedelta, timezone

from monitor.models import CostSummary


def _today_utc() -> datetime:
    return datetime.now(timezone.utc)


def _month_start() -> str:
    return _today_utc().date().replace(day=1).isoformat()


def _tomorrow() -> str:
    return (_today_utc().date() + timedelta(days=1)).isoformat()


def collect_cost_summary(cost_explorer_client) -> CostSummary:
    response = cost_explorer_client.get_cost_and_usage(
        TimePeriod={
            "Start": _month_start(),
            "End": _tomorrow(),
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE",
            }
        ],
    )

    total = 0.0
    by_service: dict[str, float] = {}

    for result in response.get("ResultsByTime", []):
        total_amount = result.get("Total", {}).get("UnblendedCost", {}).get(
            "Amount",
            "0",
        )

        total += float(total_amount)

        for group in result.get("Groups", []):
            service_name = group.get("Keys", ["Unknown"])[0]
            amount = group.get("Metrics", {}).get("UnblendedCost", {}).get(
                "Amount",
                "0",
            )

            by_service[service_name] = (
                by_service.get(service_name, 0.0) + float(amount)
            )

    return CostSummary(
        total=total,
        by_service=dict(
            sorted(
                by_service.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        ),
    )
