# AWS Cloud Practicals ☁️

A hands-on collection of AWS, Python, Boto3, Docker, Terraform, CloudFormation, LocalStack, monitoring, load-balancing, and cloud cost-management practicals.

## Overview

This repository documents my practical AWS and cloud-computing learning journey through hands-on exercises covering cloud services, automation, Infrastructure as Code, containers, monitoring, cost management, and version control.

## Technologies

- AWS
- Python 3.13
- Boto3
- Docker
- Flask
- Terraform
- AWS CloudFormation
- LocalStack
- Git & GitHub
- PowerShell

## Repository Structure

```text
aws-cloud-practicals/
├── alb-practical/
│   ├── load_balancer.py
│   ├── server1.py
│   ├── server2.py
│   └── target_health.py
├── backup-folder/
│   ├── test1.txt
│   └── test2.txt
├── docker-practical/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── terraform-practical/
│   ├── main.tf
│   ├── terraform_output.py
│   └── .terraform.lock.hcl
├── backup_s3.py
├── cloud_oop.py
├── cloudwatch.py
├── cost_report.py
├── ec2_control.py
├── ec2_test.py
├── list_buckets.py
├── list_ec2.py
├── start_ec2.py
├── stop_ec2.py
├── template.yaml
├── testingapi.py
├── cmdpromtsforaws.txt
├── test.txt
├── .gitignore
└── README.md
```

## Practicals

### 1. Amazon EC2

Hands-on work with EC2 and Python/Boto3 automation.

**Topics**
- Listing EC2 instances
- Starting and stopping instances
- Basic EC2 control
- Programmatic interaction with AWS

**Files**
- `list_ec2.py`
- `start_ec2.py`
- `stop_ec2.py`
- `ec2_control.py`
- `ec2_test.py`

**Concept**

```text
Python → Boto3 → AWS EC2 API → EC2
```

### 2. Amazon S3

Practical work with S3 buckets, objects, and backup automation.

**Topics**
- Listing S3 buckets
- Working with S3 objects
- Uploading files
- Backup automation with Python and Boto3

**Files**
- `list_buckets.py`
- `backup_s3.py`

Sample backup files are stored in `backup-folder/`.

### 3. Amazon CloudWatch

Practical work with AWS monitoring using Python and Boto3.

**Topics**
- CloudWatch
- AWS metrics
- Monitoring concepts
- Programmatic access to monitoring data

**File**
- `cloudwatch.py`

### 4. AWS Cost Management

Practical work with AWS Cost Explorer and service-level cost reporting.

**Topics**
- Cost Explorer API
- Retrieving AWS spending data
- Grouping costs by AWS service
- Generating cost reports with Python and Boto3

**File**
- `cost_report.py`

**Concept**

```text
Python → Boto3 → Cost Explorer API → AWS Cost Data → Report
```

### 5. Application Load Balancer Concepts

A local load-balancing practical using Python and LocalStack.

**Topics**
- Load balancing
- Backend servers
- Request forwarding
- Target health
- Local AWS service simulation

**Directory**
- `alb-practical/`

**Files**
- `load_balancer.py`
- `server1.py`
- `server2.py`
- `target_health.py`

**Architecture**

```text
             Client
                |
                v
       +----------------+
       | Load Balancer  |
       +-------+--------+
               |
         +-----+-----+
         |           |
         v           v
     Server 1     Server 2
```

LocalStack is used for suitable AWS simulation to avoid unnecessary AWS infrastructure costs.

### 6. Docker

Hands-on Docker work performed locally.

**Topics**
- Images
- Containers
- Dockerfiles
- Building images
- Running containers
- Container logs
- Image inspection
- Port mapping
- Dockerizing Python applications

**Directory**
- `docker-practical/`

#### Python Docker Application

The project includes a simple Python application that prints:

```text
Hello from Docker!
My Cloud Journey - Docker Practical
```

Build:

```bash
docker build -t cloud-python-app .
```

Run:

```bash
docker run cloud-python-app
```

View containers:

```bash
docker ps -a
```

View logs:

```bash
docker logs <CONTAINER_ID>
```

Inspect the image:

```bash
docker image inspect cloud-python-app
```

#### Flask + Docker

A Flask web application was also containerized and tested locally.

The application runs on port `5000` and returns:

```text
Hello from Flask + Docker!
```

Build:

```bash
docker build -t flask-docker-app .
```

Run:

```bash
docker run -p 5000:5000 flask-docker-app
```

Open:

```text
http://localhost:5000
```

### 7. Terraform

Infrastructure as Code practical using Terraform and AWS.

**Topics**
- Infrastructure as Code
- Terraform configuration
- AWS provider
- AWS resource provisioning
- `terraform init`
- `terraform plan`
- Terraform outputs
- Terraform and Python integration

**Directory**
- `terraform-practical/`

**Files**
- `main.tf`
- `terraform_output.py`
- `.terraform.lock.hcl`

**Workflow**

```text
main.tf
  ↓
terraform init
  ↓
terraform plan
  ↓
terraform apply
  ↓
AWS Resources
  ↓
terraform output
```

### 8. Terraform + Python Integration

The project demonstrates how Python can consume Terraform output.

**File**
- `terraform-practical/terraform_output.py`

The script uses Python's `subprocess` module to run:

```bash
terraform output -json
```

It then parses the JSON response and reads Terraform output values.

**Concept**

```text
Terraform
    ↓
terraform output -json
    ↓
subprocess
    ↓
JSON
    ↓
Python
    ↓
Automation
```

### 9. AWS CloudFormation

Infrastructure as Code practice using an AWS CloudFormation YAML template.

**File**
- `template.yaml`

CloudFormation provides a declarative way to describe AWS infrastructure.

```text
CloudFormation YAML
        ↓
   CloudFormation
        ↓
    AWS Resources
```

### 10. Python + Boto3

Python and Boto3 are used throughout the repository to communicate with AWS services through APIs.

**Services practiced**
- EC2
- S3
- CloudWatch
- Cost Explorer

**General model**

```text
Python Script
     ↓
   Boto3
     ↓
  AWS API
     ↓
AWS Service
```

### 11. Python OOP

Python object-oriented programming practice supporting larger automation projects.

**File**
- `cloud_oop.py`

### 12. API / Testing Practice

Additional API and testing experimentation.

**File**
- `testingapi.py`

## Security

Sensitive AWS credentials and private keys are intentionally excluded from this repository.

The `.gitignore` protects files such as:

```text
*.csv
*.pem
.aws/
.env
Terraform state files
```

Never commit the following to a public repository:

- AWS access keys
- AWS secret keys
- Private keys
- `.pem` files
- Passwords
- API tokens
- `.env` files containing secrets
- Terraform state files containing sensitive information

Use secure credential mechanisms such as AWS CLI credential configuration, environment variables, IAM roles, or a secrets-management solution.

## Cost Awareness

Cloud resources can generate charges while running.

During practical work, cost awareness is treated as an important part of learning AWS.

Approaches include:

- Using free-tier-eligible resources where applicable
- Running resources only when required
- Stopping or terminating resources after practicals
- Using LocalStack for suitable local simulations
- Reviewing costs with Cost Explorer

Always verify current AWS pricing and Free Tier conditions before deploying resources.

## Key Learning Areas

### Compute
- Amazon EC2

### Storage
- Amazon S3
- Object storage
- Backup automation

### Monitoring
- Amazon CloudWatch
- Metrics

### Cost Management
- AWS Cost Explorer
- Service-level cost reporting

### Networking
- Application Load Balancer concepts
- Backend servers
- Target health
- Request distribution

### Automation
- Python
- Boto3
- AWS APIs
- Terraform output integration

### Infrastructure as Code
- Terraform
- AWS CloudFormation

### Containers
- Docker
- Docker images
- Docker containers
- Flask applications
- Port mapping

### Development
- Git
- GitHub
- PowerShell

## Overall Learning Flow

```text
AWS Fundamentals
       ↓
Python + Boto3
       ↓
AWS Automation
       ↓
Monitoring & Cost Management
       ↓
Docker + Flask
       ↓
Infrastructure as Code
       ↓
Terraform + CloudFormation
       ↓
Load Balancing
       ↓
Cloud Architecture
       ↓
Deployment & CI/CD
```

## Future Capstone Work

Planned areas for the larger cloud capstone include:

- Custom VPC
- Public and private subnets
- EC2 web/application tier
- RDS database tier
- Auto Scaling
- CloudWatch alarms
- IAM and security best practices
- CI/CD
- GitHub Actions
- ECS concepts
- Three-tier architecture

These are future learning/capstone items and are not presented as completed in this repository.

## Learning Objective

The goal of this repository is to move from AWS theory to practical implementation by combining:

```text
Cloud Services
      +
Python Automation
      +
Infrastructure as Code
      +
Containers
      +
Monitoring
      +
Cost Awareness
      +
Version Control
```

## Author

**Abhiingit**

GitHub: https://github.com/Abhiingit/aws-cloud-practicals

---

⭐ This repository is part of my ongoing cloud-computing learning journey.
