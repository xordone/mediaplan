import dotenv
import json

config = dotenv.dotenv_values('.env')
json_data = json.dumps(config, indent=4)

def get_cred():
    dotenv.load_dotenv()
    config = dotenv.dotenv_values('.env')
    json_data = json.dumps(config, indent=4)
    return json_data