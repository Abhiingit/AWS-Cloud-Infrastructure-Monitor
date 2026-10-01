from dataclasses import dataclass, field


@dataclass
class EC2Summary:
    total: int = 0
    running: int = 0
    stopped: int = 0
    other: int = 0


@dataclass
class S3Summary:
    total: int = 0


@dataclass
class RDSSummary:
    total: int = 0
    available: int = 0
    other: int = 0


@dataclass
class CloudWatchSummary:
    total: int = 0
    ok: int = 0
    alarm: int = 0
    insufficient_data: int = 0
    other: int = 0


@dataclass
class CostSummary:
    total: float | None = None
    by_service: dict[str, float] = field(default_factory=dict)


@dataclass
class InfrastructureReport:
    region: str
    ec2: EC2Summary
    s3: S3Summary
    rds: RDSSummary
    cloudwatch: CloudWatchSummary
    cost: CostSummary
