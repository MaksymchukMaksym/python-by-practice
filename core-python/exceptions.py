import csv

import modules as md


def process_sales_etl(config_file):
    result = {}
    # TRANSFORM
    config = md.get_etl_config(config_file)
    with open(config["input_file"], 'r') as file:
        captions = [element.strip('"\t\n\r ') for element in file.readline().strip().split(';')]
        data = [dict(zip(captions,
                         [element.strip('"\t\n\r ') for element in line.strip().split(';')]))
                for line in file]

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

        # LOAD
    if "output_file" in config:
        with open(config["output_file"], 'w', encoding="utf-8", newline='') as file:
            if not result:
                raise ValueError("Result is empty")
            writer = csv.DictWriter(file, fieldnames=result.keys())
            writer.writeheader()
            writer.writerow(result)


process_sales_etl("data/etl_config.json")
# except:
