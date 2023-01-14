import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith("csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            read = csv.reader(file)
            return list(read)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
