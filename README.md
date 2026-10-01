# AWS Cloud Infrastructure Monitor

A Python-based AWS infrastructure monitoring tool that collects operational and cost information from AWS services and produces consolidated console and JSON reports.

## What It Does

The monitor collects:

- EC2 instance counts and states
- S3 bucket count
- RDS database instance states
- CloudWatch alarm states
- AWS Cost Explorer month-to-date cost
- An overall infrastructure health status

```text
                    AWS Account
                         |
                         v
              +-------------------+
              |  Python + Boto3   |
              +-------------------+
                 |   |   |   |   |
                 v   v   v   v   v
                EC2 S3 RDS CW Cost
                 |   |   |   |   |
                 +---+---+---+---+
                         |
                         v
              +-------------------+
              | Infrastructure    |
              | Report / Health   |
              +-------------------+
                    |        |
                    v        v
                 Console    JSON
```

## AWS Services

| Service | Purpose |
|---|---|
| EC2 | Count instances and classify states |
| S3 | Count buckets |
| RDS | Count database instances and classify status |
| CloudWatch | Inspect alarm states |
| Cost Explorer | Calculate month-to-date cost |
| IAM | Provide least-privilege read access |

## Project Structure

```text
AWS-Cloud-Infrastructure-Monitor/
│
├── monitor/
│   ├── __init__.py
│   ├── config.py
│   ├── health.py
│   ├── main.py
│   ├── models.py
│   ├── aws/
│   │   ├── __init__.py
│   │   ├── ec2.py
│   │   ├── s3.py
│   │   ├── rds.py
│   │   ├── cloudwatch.py
│   │   └── costs.py
│   └── reports/
│       ├── __init__.py
│       ├── console.py
│       └── json_report.py
│
├── tests/
│   └── test_monitor.py
├── policies/
│   └── monitor-readonly.json
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── labs/
    └── ...
```

Older AWS/cloud practicals are intended to live under `labs/`, keeping them separate from this main portfolio application.

## Requirements

- Python 3.10+
- AWS CLI
- AWS account and configured credentials
- Docker (optional)

Install runtime dependencies:

```powershell
pip install -r requirements.txt
```

Install development dependencies:

```powershell
pip install -r requirements-dev.txt
```

## AWS Authentication

Check the active AWS identity:

```powershell
aws sts get-caller-identity
```

The application defaults to `ap-south-1`.

You can change the region with:

```powershell
$env:AWS_REGION="ap-south-1"
```

## IAM Permissions

The project includes:

```text
policies/monitor-readonly.json
```

The monitor currently requires only:

```text
ec2:DescribeInstances
s3:ListAllMyBuckets
rds:DescribeDBInstances
cloudwatch:DescribeAlarms
ce:GetCostAndUsage
```

This keeps the monitoring permissions read-only and narrowly scoped to the APIs used by the application.

## Run the Monitor

From the repository root:

```powershell
python -m monitor.main
```

The application collects AWS data, evaluates health, prints a report, and writes:

```text
monitor/reports/latest.json
```

The generated report is ignored by Git.

## Example Output

A real test run produced:

```text
AWS CLOUD INFRASTRUCTURE MONITOR
==================================================

Region        : ap-south-1
Overall Status: ATTENTION REQUIRED

EC2
--------------------------------------------------
Total instances : 0
Running         : 0
Stopped         : 0
Other states    : 0

S3
--------------------------------------------------
Buckets         : 3

RDS
--------------------------------------------------
Total instances : 0
Available       : 0
Other states    : 0

CloudWatch Alarms
--------------------------------------------------
Total             : 1
OK                : 0
ALARM             : 0
Insufficient data : 1

AWS Cost
--------------------------------------------------
Month-to-date    : $0.00
```

In that run, `ATTENTION REQUIRED` was produced because a CloudWatch alarm was in `INSUFFICIENT_DATA`.

## Health Logic

The current implementation reports `ATTENTION REQUIRED` when:

- a CloudWatch alarm is `ALARM`
- a CloudWatch alarm is `INSUFFICIENT_DATA`
- an RDS instance has a status other than `available`

Otherwise it reports `HEALTHY`.

## Testing

Run the test suite:

```powershell
pytest -q
```

Run linting:

```powershell
ruff check monitor tests
```

The current tests cover EC2, S3, RDS, CloudWatch summaries and health evaluation.

## Docker

Build the image:

```powershell
docker build -t aws-cloud-infrastructure-monitor:1.0 .
```

Run it:

```powershell
docker run --rm -e AWS_REGION=ap-south-1 aws-cloud-infrastructure-monitor:1.0
```

The container must have access to valid AWS credentials through the environment or an appropriate AWS credential mechanism. Do not hard-code credentials into the image.

## Design

The application separates AWS collection, data models, health logic and reporting:

```text
monitor/
├── config.py
├── models.py
├── health.py
├── main.py
├── aws/
│   ├── ec2.py
│   ├── s3.py
│   ├── rds.py
│   ├── cloudwatch.py
│   └── costs.py
└── reports/
    ├── console.py
    └── json_report.py
```

This keeps the code modular and makes individual components easier to test and extend.

## Current Capabilities

- Real AWS API integration with Boto3
- Read-only IAM policy
- EC2 monitoring
- S3 inventory summary
- RDS monitoring
- CloudWatch alarm inspection
- Cost Explorer integration
- Console reporting
- JSON reporting
- Pytest unit tests
- Ruff linting
- Docker support
- Environment-based configuration

## Future Improvements

- Scheduled monitoring
- SNS/email notifications
- Historical report storage
- Additional CloudWatch metrics
- EC2 CPU and status checks
- RDS CPU/storage monitoring
- S3 storage/object statistics
- Web dashboard
- GitHub Actions CI
- Automated container publishing
- Infrastructure-as-code deployment
- Multi-region monitoring

## Cloud Labs

The repository also contains earlier AWS/cloud practical work. These will be grouped under:

```text
labs/
```

so the repository clearly separates the main application from learning exercises.

```text
Main Project
└── AWS Cloud Infrastructure Monitor

Labs
├── EC2
├── S3
├── CloudWatch
├── Terraform
├── CloudFormation
├── Docker
├── ALB
├── Boto3
└── Other AWS practicals
```

## Author

**Abhijeet Pratap Singh**

Computer Science & Engineering  
AWS • Cloud • DevOps • Python

## License

Educational and portfolio project.
