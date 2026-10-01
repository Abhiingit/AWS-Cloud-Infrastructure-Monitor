from monitor.models import S3Summary


def collect_s3_summary(s3_client) -> S3Summary:
    response = s3_client.list_buckets()

    return S3Summary(
        total=len(response.get("Buckets", []))
    )
