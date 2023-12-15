from src.upload import S3Upload

upload_client = S3Upload()
if __name__ == '__main__':
    upload_client.upload()
