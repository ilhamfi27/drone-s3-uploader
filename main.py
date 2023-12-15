from src.upload import S3Upload
from src.config import config
import argparse
import logging


upload_client = S3Upload()

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


def parse_args(args):
    if args.debug:
        conf = config()
        logging.info('=============================================')
        for key in conf:
            logging.info(f"{key}: {conf[key]}")
        logging.info('=============================================')


if __name__ == '__main__':
    parser = argparse.ArgumentParser("app")
    parser.add_argument(
        "--debug", help="A flag that determine if the running app is in debug mode to show all env vars", type=bool, default=False)
    args = parser.parse_args()
    parse_args(args=args)
    upload_client.upload()
