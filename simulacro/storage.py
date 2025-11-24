import csv

def read_csv(path):
    data = []
    """
    Lee un archivo CSV y devuelve una lista de filas (sin el header).
    """
    try:
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader) # Salta el header
            for row in reader:
                item = {header[i]: row[i] for i in range(len(header))}
                data.append(item)
    except FileNotFoundError:
        print("File not founded.")
    return data

def write_csv(path, data):
    """
    Sobrescribe un archivo CSV con header + datos.
    'data' debe ser una lista donde data[0] es el header.
    """
    if not data:
        raise ValueError("No se puede escribir un CSV vacío.")

    header = data[0]
    rows = data[1:]

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def append_csv(path, row):
    """
    Agrega una fila nueva al CSV.
    """
    with open(path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_csv(path, data):
    if not data:
        print("No data to save.")
        return
    header = list(data[0].keys())
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for item in data:
            writer.writerow([item[key] for key in header])