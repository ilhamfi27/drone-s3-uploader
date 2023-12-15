from minio import Minio
from src.config import config

conf = config()

client = Minio(
    conf['endpoint'],
    access_key=conf['access_key'],
    secret_key=conf['secret_key'],
    secure=False
)
