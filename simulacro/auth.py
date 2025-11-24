import csv
# with open("admin_access.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     # for fila in reader:
#     #     print(fila)
def load_admin_credential():
    with open("admin_access.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            return {
                "username": row[0],
                "password": row[1],
                "role": row[2]
            }
def login():
    admin = load_admin_credential()
    user = input("Insert Admin ID: ")
    pwd = input("Insert password: ")
    if user == admin["username"] and pwd == admin["password"]:
        print("Correct credentials, welcome Admin!")
        return True
    else:
        return False
def login_try(attempts):
    attempts -= 1
    if attempts > 0:
        print(f"Incorrect credentials. Attempts remaining: {attempts}")
    return attempts
