from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

drone_plugin_prefix = 'PLUGIN'


def config():
    return {
        'endpoint': os.environ.get(f"{drone_plugin_prefix}_ENDPOINT", 'https://s3.amazonaws.com'),
        'access_key': os.environ.get(f"{drone_plugin_prefix}_ACCESS_KEY"),
        'secret_key': os.environ.get(f"{drone_plugin_prefix}_SECRET_KEY"),
        'session_token': os.environ.get(f"{drone_plugin_prefix}_SESSION_TOKEN"),
        'secure': os.environ.get(f"{drone_plugin_prefix}_SECURE"),
        'region': os.environ.get(f"{drone_plugin_prefix}_REGION"),
        'http_client': os.environ.get(f"{drone_plugin_prefix}_HTTP_CLIENT"),
        'credentials': os.environ.get(f"{drone_plugin_prefix}_CREDENTIALS"),
        'bucket': os.environ.get(f"{drone_plugin_prefix}_BUCKET"),

        # file location target
        'target': os.environ.get(f"{drone_plugin_prefix}_TARGET"),

        # file location source
        'source': os.environ.get(f"{drone_plugin_prefix}_SOURCE"),
        
    }
