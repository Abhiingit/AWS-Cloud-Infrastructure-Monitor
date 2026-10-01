import json
from dataclasses import asdict

from monitor.health import get_overall_status
from monitor.models import InfrastructureReport


def build_json_report(report: InfrastructureReport) -> dict:
    data = asdict(report)
    data["overall_status"] = get_overall_status(report)
    return data


def write_json_report(report: InfrastructureReport, output_path: str) -> None:
    payload = build_json_report(report)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)
