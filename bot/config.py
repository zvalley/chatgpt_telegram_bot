import yaml
import dotenv
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--config_env", type=str, required=False, help="Custom configuration file for environments")
parser.add_argument("--config_yml", type=str, required=False, help="Custom configuration file for bot")
args = parser.parse_args()

config_dir = Path(__file__).parent.parent.resolve() / "config"

config_yaml_filepath=None
if args.config_yml is not None:
    config_yaml_filepath=args.config_yml
else:
    config_yaml_filepath=config_dir / "config.yml"
# load yaml config
with open(config_yaml_filepath, 'r') as f:
    config_yaml = yaml.safe_load(f)

with open(config_dir / "tokens.yml", 'r') as f:
    tokens_yaml = yaml.safe_load(f)

# load .env config
if args.config_env is not None:
    config_env = dotenv.dotenv_values(args.config_env)
else:
    config_env = dotenv.dotenv_values(config_dir / "config.env")


# config parameters
telegram_token = tokens_yaml["telegram_token"]
openai_api_key = tokens_yaml["openai_api_key"]
openai_api_url = config_yaml["openai_api_url"]
openai_api_version = config_yaml["openai_api_version"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://{config_env['MONGODB_HOST']}:{config_env['MONGODB_PORT']}"
# mongodb_uri = f"mongodb://mongo.chatgpt_telegram_bot_default:{config_env['MONGODB_PORT']}"
# mongodb_uri = f"mongodb://localhost:{config_env['MONGODB_PORT']}"

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
