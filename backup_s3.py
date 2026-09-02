import boto3
import os

# AWS S3 configuration
BUCKET_NAME = "cloud-practical-backup-20260816-xyz"
SOURCE_FOLDER = r"C:\Users\DELL\Downloads\backup-folder"
S3_FOLDER = "daily-backup"

# Create S3 client
s3 = boto3.client("s3", region_name="ap-south-1")


def backup_folder():
    for root, dirs, files in os.walk(SOURCE_FOLDER):

        for file in files:

            # Full path of local file
            local_path = os.path.join(root, file)

            # Path relative to backup-folder
            relative_path = os.path.relpath(
                local_path,
                SOURCE_FOLDER
            )

            # S3 object key
            s3_key = f"{S3_FOLDER}/{relative_path}".replace("\\", "/")

            print(f"Uploading: {local_path}")
            print(f"       To: s3://{BUCKET_NAME}/{s3_key}")

            # Upload file
            s3.upload_file(
                local_path,
                BUCKET_NAME,
                s3_key
            )

    print("\nBackup completed successfully!")


if __name__ == "__main__":
    backup_folder()