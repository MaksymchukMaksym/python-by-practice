import json
import logging

logging.basicConfig(filename="data/fallback_errors.log", level=logging.ERROR,
                    format="%(asctime)s [%(levelname)s] %(message)s")


class ConfigError(Exception):
    pass


# EXTRACT
def get_etl_config(file_name):
    errors = []
    try:
        with open(file_name, "r") as f:
            etl_config = json.load(f)
        required_keys = {"input_file", "output_file", "log_file", "filters", "value_column", "actions"}
        if not all(key in etl_config for key in required_keys):
            error_message = f"ConfigError: Missing required keys in {file_name}"
            logging.error(error_message)
            errors.append(error_message)
            raise ConfigError(error_message)
    except FileNotFoundError:
        print("FileNotFoundError")
        error_message = f"FileNotFoundError: {file_name} not found"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}
    except PermissionError:
        error_message = f"PermissionError: No access to {file_name}"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}
    except json.JSONDecodeError as e:
        error_message = f"JSONDecodeError:{file_name} wrong JSON format"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}
    except OSError as e:
        error_message = f"OSError: Failed to process {file_name}: {str(e)}"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}
    except Exception as e:
        error_message = f"Unexpected error: {type(e).__name__}: {str(e)}"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}
    except ConfigError as e:
        error_message = f"ConfigError: Invalid configuration in {file_name}: {str(e)}"
        logging.error(error_message)
        errors.append(error_message)
        return {"status": "failed", "config": None, "errors": errors}

    return etl_config
