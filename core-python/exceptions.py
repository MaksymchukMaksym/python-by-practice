import csv
import logging

import modules as md

logging.basicConfig(filename="data/fallback_errrors.log", level=logging.ERROR,
                    format="%(asctime)s [%(levelname)s] %(message)s")


def process_sales_etl(config_file):
    result = {}
    # TRANSFORM
    config = md.get_etl_config(config_file)
    try:
        with open(config["input_file"], 'r') as file:
            captions = [element.strip('"\t\n\r ') for element in file.readline().strip().split(';')]
            data = [dict(zip(captions,
                             [element.strip('"\t\n\r ') for element in line.strip().split(';')]))
                    for line in file]

            try:
                filters = [filter for filter in config["filters"]]
                filtered_data = [
                    element for element in data
                    if all(
                        element[filter["column"]] == filter["value"] if filter.get("operator", "==") == "=="
                        else float(element[filter["column"]].replace(",", ".")) >
                             float(filter["value"].replace(",", "."))
                        if filter.get("operator") == ">"

                        else float(element[filter["column"]].replace(",", ".")) <
                             float(filter["value"].replace(",", "."))
                        if filter.get("operator") == "<"

                        else False
                        for filter in filters
                    )

                ]
                value_column = config["value_column"]
                actions = config["actions"]

                values = [float(element[value_column].replace(",", ".")) for element in filtered_data]

                for action in actions:
                    if action == "sum":
                        result["sum"] = sum(values)
                    elif action == "avg":
                        result["avg"] = sum(values) / len(values) if values else None
                    elif action == "max":
                        result["max"] = max(values) if values else None

            except KeyError as e:
                logging.error(f"KeyError: Missing  key {e}")
            except ValueError as e:
                logging.error(f"ValueError during transformation {e}")
            except TypeError as e:
                logging.error(f"TypeError during transformation {e}")
            except ZeroDivisionError as e:
                logging.error(f"ZeroDivisionError during calculation {e}")
            except IndexError as e:
                logging.error(f"IndexError during transormation data {e}")

    except FileNotFoundError:
        logging.error(f"File {config['input_file']} not found")
    except PermissionError:
        logging.error(f"PermissionError: No access to {config['input_file']}")
    except UnicodeDecodeError:
        logging.error(f"UnicodeDecodeError: No utf-8 for {config['input_file']}")
    # LOAD
    try:
        if "output_file" in config:
            with open(config["output_file"], 'w', encoding="utf-8", newline='') as file:
                if not result:
                    raise ValueError("Result is empty")
                writer = csv.DictWriter(file, fieldnames=result.keys(), delimiter=";")
                writer.writeheader()
                writer.writerow(result)
    except FileNotFoundError:
        logging.error(f"File {config['input_file']} not found")
    except PermissionError:
        logging.error(f"PermissionError: No access to {config['input_file']}")
    except OSError as e:
        logging.error(f"General error during writing {e}")
    except ValueError as e:
        logging.error(f"ValueError during writing output {e}")
    except TypeError as e:
        logging.error(f"TypeError during writing output {e}")


process_sales_etl("data/etl_config.json")
