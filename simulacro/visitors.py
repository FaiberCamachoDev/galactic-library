from storage import read_csv, write_csv, save_csv
visitor_csv = "visitors.csv"
def generate_id():
    visitor = read_csv(visitor_csv)
    if not visitor:
        return 1
    
    used_ids = {int(v["id"]) for v in visitor}
    new_id = 1
    while new_id in used_ids:
        new_id += 1
    return new_id
def register_visit():
    name = input("Name of visitant: ")
    specie = input("Specie: ")
    planet = input("Origin Planet: ")
    status = input("Write Status (Active/Retired): ").lower()
    val_status = True
    new_id = generate_id()
    while val_status:
        match status:
            case "active":
                print("set status Active.")
                val_status = False
            case "retired":
                val_status = False
            case _:
                print("Write a valid status.")
                status = input("Write Status (Active/Retired): ").lower()
    visitor_d = {
        "id": new_id,
        "name": name,
        "specie": specie,
        "planet": planet,
        "status": status 
    }
    visitor = read_csv(visitor_csv)
    visitor.append(visitor_d)
    save_csv(visitor_csv, visitor)
    
    print(f" New ID register: {new_id}")
def list_visitors():
    visitor = read_csv(visitor_csv)
    if not visitor:
        print("Not visitor registered")
        return
    
    print("Visitor list")
    for v in visitor:
        visitor_tuple = (
            int(v["id"]),
            v["name"],
            v["specie"],
            v["planet"],
            v["status"],
        )
        print(visitor_tuple)
def search_visitor_id():
    search_id = ("insert ID: ")
    visitor = read_csv(visitor_csv).strip()
    if not visitor:
        print("No data registered for this ID")
        return
    found = None
    for v in visitor:
        if str(v["id"]) == search_id:
            found = v
            break
    if found:
        print("\n--- visitant ---")
        print(f"""
            ID: {found['id']}
            Name: {found['name']}
            Specie: {found['specie']}
            Planet: {found['planet']}
            Status: {found['status']}
            """)
    else:
        print(f"There is no visitant with ID {search_id}")
def update_status():
    visitor = read_csv(visitor_csv)
    if not visitor:
        print("No visitor data found")
        return
    val_target = True
    while val_target:
        target_id = input("Enter visito ID for update status: ")
        if not target_id.isdigit():
            print("Insert a valid ID.")
            continue
        else:
            val_target = False
    target_id = int(target_id)
    found = False
    for v in visitor:
        if int(v["id"]) == target_id:
            found = True
            print(f"Current status of {target_id} ID: {v["status"]}")
            if v["status"] == "active":
                v["status"] = "retired"
                print("status changed to retired")
            else:
                v["status"] = "active"
                print("status changed to active")
            break
    if not found:
        print("No ID founded")
        return
    save_csv(visitor_csv, visitor)
    print("Status updated successfully!")
def delete_visitor():
    visitor = read_csv(visitor_csv)

    if not visitor:
        print("No visitor records found.")
        return

    try:
        target_id = int(input("Enter Visitor ID to delete: "))
    except ValueError:
        print("Invalid ID format.")
        return

    # Buscar el visitante y eliminarlo
    new_list = []
    found = False

    for v in visitor:
        if int(v["id"]) == target_id:
            found = True
            print(f"Visitor with ID {target_id} deleted successfully.")
            continue  # No agregarlo a la nueva lista
        new_list.append(v)

    if not found:
        print("Visitor ID not found.")
        return

    # Guardar la nueva lista sin el visitante eliminado
    save_csv(visitor_csv, new_list)
    print("CSV updated successfully.")
def visitors_stats():
    visitor = read_csv(visitor_csv)

    if not visitor:
        print("No visitors registered.")
        return

    print("\n=== Visitors Statistics ===")

    # Total
    total = len(visitor)
    print(f"Total visitors: {total}")

    # Visitors by specie (dict)
    specie_count = {}
    for v in visitor:
        specie = v["specie"].lower()
        specie_count[specie] = specie_count.get(specie, 0) + 1

    print("\nVisitors by specie:")
    for s, count in specie_count.items():
        print(f"  {s}: {count}")

    # Active vs retired (sets for the challenge)
    active = set()
    retired = set()

    for v in visitor:
        if v["status"] == "active":
            active.add(v["id"])
        else:
            retired.add(v["id"])

    print("\nStatus summary:")
    print(f"  Active: {len(active)}")
    print(f"  Retired: {len(retired)}")
