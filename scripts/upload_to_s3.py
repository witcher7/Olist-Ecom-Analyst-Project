import boto3
BUCKET_NAME = "your-bucket-name"
s3 = boto3.client('s3')

local_file_path = "path/to/your/local/file"
s3_file_key = "your/s3/file/folder/filename.parquet"
print(f"Uploading {local_file_path} to s3://{BUCKET_NAME}/{s3_file_key}...")
s3.upload_file(local_file_path, BUCKET_NAME, s3_file_key)
print("Upload completed successfully.")