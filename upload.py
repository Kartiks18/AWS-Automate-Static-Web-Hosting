import boto3
import os

bucket_name = "kaartik-static-website"

s3 = boto3.client("s3")

folder = "website"

for file in os.listdir(folder):

    filepath = os.path.join(folder, file)

    s3.upload_file(
        filepath,
        bucket_name,
        file,
        ExtraArgs={
            "ContentType":
            "text/html" if file.endswith(".html")
            else "text/css"
        }
    )

    print(f"{file} uploaded")

print("Upload Completed")