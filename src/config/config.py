from os import path
import json

# will be read in this order
CONFIG_TO_BE_READ = ['default', 'secret']
CONFIG_DIR = "../config"

# this is our config
CONFIG = {}

for config_name in CONFIG_TO_BE_READ:
    config_path = path.join(CONFIG_DIR, "{}.json".format(config_name))
    with open(config_path) as secret_file:
        CONFIG = dict(CONFIG, **json.loads(secret_file.read()))
