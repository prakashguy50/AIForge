import boto3

def upload_to_s3(bucket_name, file_path, object_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"Uploaded {file_path} to {bucket_name}/{object_name}")
