import json


def get_etl_config(file_name):
    try:
        with open(file_name, "r") as f:
            etl_config = json.load(f)
    except FileNotFoundError as e:
        print(f"File not found {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Json not valid {e}")
        return None
    return etl_config


if __name__ == "modules":
    etl_config = get_etl_config("data/etl_config.json")
    print(etl_config)
