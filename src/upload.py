from minio.error import S3Error
from src.minio import client
from src.config import config

conf = config()


class S3Upload:
    def __init__(self) -> None:
        self.client = client

    def upload(self):
        try:
            bucket = conf['bucket']
            target = conf['target']
            source = conf['source']
            if not self.client.bucket_exists(bucket):
                self.client.make_bucket(bucket)
            self.client.fput_object(bucket, target, source)
        except S3Error as e:
            print(f'Error: {e}')
