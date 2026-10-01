import boto3
from datetime import date, timedelta

# Create Cost Explorer client
ce = boto3.client("ce", region_name="us-east-1")

# Last 30 days
end_date = date.today() + timedelta(days=1)
start_date = end_date - timedelta(days=30)

# Ask AWS Cost Explorer for cost data
response = ce.get_cost_and_usage(
    TimePeriod={
        "Start": start_date.isoformat(),
        "End": end_date.isoformat()
    },
    Granularity="MONTHLY",
    Metrics=["UnblendedCost"],
    GroupBy=[
        {
            "Type": "DIMENSION",
            "Key": "SERVICE"
        }
    ]
)

# Store total cost for each service
service_costs = {}

for result in response["ResultsByTime"]:
    for group in result["Groups"]:
        service = group["Keys"][0]
        amount = float(group["Metrics"]["UnblendedCost"]["Amount"])

        service_costs[service] = service_costs.get(service, 0) + amount

# Display results
print("\nAWS Cost Report - Last 30 Days")
print("=" * 40)

for service, cost in sorted(
    service_costs.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{service}: ${cost:.4f}")

print("=" * 40)

total = sum(service_costs.values())
print(f"Total: ${total:.4f}")