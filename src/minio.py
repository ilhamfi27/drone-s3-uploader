from minio import Minio
from src.config import config

conf = config()


def define_secure():
    secure = conf['secure']
    return secure in ['true', 'True']


client = Minio(
    conf['endpoint'],
    access_key=conf['access_key'],
    secret_key=conf['secret_key'],
    secure=define_secure()
)
