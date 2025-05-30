import modules as md

if __name__ == "__main__":
    config = md.get_etl_config("data/etl_config.json")
    try:
        with open(config["file"], 'r') as file:
            data = file.readlines()
            headers = data[0].strip().split(";")
            lines = [line.strip().split(";") for line in data[1:]]
            rows = [
                dict(zip(headers, line.strip().split(";")))
                for line in data[1:]
                if line.strip()
            ]
            operated = [el for el in rows if el[config["filter-column"]] == config["filter-value"]]
            values = [float(el[config['value-column']]) for el in operated]

            for trans in config['action']:
                print(f"Transform {trans}: {eval(f'{trans}({values})')}")
    except FileNotFoundError as e:
        print(f"File with data not found {e}")
# data/output.csv
