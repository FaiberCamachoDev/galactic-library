from storage import read_csv, write_csv, save_csv
artefact_csv = "artefacts.csv"
def generate_id_artefact():
    artefacts = read_csv(artefact_csv)
    if not artefacts:
        return 1
    
    used_ids = {int(a["id"]) for a in artefacts}
    new_id = 1
    while new_id in used_ids:
        new_id += 1
    return new_id
def register_artefact():
    id = generate_id_artefact()
    description = input("Description of artefact: ")
    rarity = input("Rarity (low/mid/high/prohibited ): ").lower()
    status = input("Status (stored/study/destroyed): ").lower()
    artefact = {
        "id": id,
        "description": description,
        "rarity": rarity,
        "status": status
    }

    artefacts = read_csv(artefact_csv)
    artefacts.append(artefact)
    save_csv(artefact_csv, artefacts)

    print(f"\nArtefacto registrado con código: {id}")
    
def list_artefacts():
    artefacts = read_csv(artefact_csv)
    if not artefacts:
        print("No hay artefactos registrados.")
        return

    print("\n--- Lista de Artefactos ---")
    for a in artefacts:
        print(f""""
            id: {a['id']} | Desc: {a['description']} | 
            Rareza: {a['rarity']} | Status: {a['status']}
        """)
def search_artefact():
    artefacts = read_csv(artefact_csv)
    if not artefacts:
        print("No data found")
        return
    id = input("Introduce the id of artefact:")
    for a in artefacts:
        if str(a["id"]) == id:
            print(f""" 
                Artefact Info:
                ID: {id}
                Descrip: {a["description"]}
                Rarity: {a["rarity"]}
                Status: {a["status"]}
                """)
            return
def classify_by_rarity(**kwargs):
    rarity = input("Insert rarity (bajo/medio/alto/prohibido): ").strip().lower()
    artefacts = read_csv(artefact_csv)

    if not artefacts:
        print("No hay artefactos registrados.")
        return

    results = [a for a in artefacts if a["rarity"].lower() == rarity]

    print(f"\nArtefactos con rareza '{rarity}':")
    if not results:
        print("No se encontraron artefactos con esa rareza.")
        return

    for a in results:
        print(a)
def artefact_stats():
    artefacts = read_csv(artefact_csv)
    if not artefacts:
        print("No hay artefactos registrados.")
        return

    total = len(artefacts)
    rarity_count = {}
    status_count = {}

    for a in artefacts:
        rarity_count[a["rarity"]] = rarity_count.get(a["rarity"], 0) + 1
        status_count[a["status"]] = status_count.get(a["status"], 0) + 1

    print("\n--- Estadísticas ---")
    print(f"Total artefactos: {total}")
    print(f"Por rareza: {rarity_count}")
    print(f"Por estatus: {status_count}")
def delete_artefact():
    artefacts = read_csv(artefact_csv)
    if not artefacts:
        print("No hay artefactos registrados.")
        return

    code = input("Código a eliminar: ")

    new_list = [a for a in artefacts if str(a["id"]) != code]

    if len(new_list) == len(artefacts):
        print("No se encontró un artefacto con ese código.")
        return

    save_csv(artefact_csv, new_list)
    print("Artefacto eliminado.")