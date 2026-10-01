import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    aws_region: str = os.getenv("AWS_REGION", "ap-south-1")
    output_format: str = os.getenv("MONITOR_OUTPUT", "console")


settings = Settings()
