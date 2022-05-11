import boto3
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='',
    aws_secret_access_key=''
)
bucket_name="shreyasstorage"
# Downloading file from aws s3 bucket
try:
    s3.Bucket(bucket_name).download_file("Elephant.jpg","E://AWS//Workspace//downloadedelephant.jpg")
    print("File Download Success")
except Exception as e:
    print("File Download Failed")
    print(e)
# Uploading file to aws s3 bucket
try:
    s3.Bucket(bucket_name).upload_file("E://AWS//Workspace//Dog.jpg","DogUploadedImage.jpg")
    print("File Upload Success")
except Exception as e:
    print("File Upload Failed")
    print(e)
