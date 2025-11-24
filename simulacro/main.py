from auth import login, login_try
from visitors import (
    register_visit,
    list_visitors,
    search_visitor_id,
    update_status,
    delete_visitor,
    visitors_stats
)
from artefacts import(
    register_artefact,
    list_artefacts,
    search_artefact,
    classify_by_rarity,
    artefact_stats,
    delete_artefact
)
def main_menu():
    while True:
        print("\n========= FEDERATION DATABASE =========")
        print("1. Visitor Module")
        print("2. Artefact Module")
        print("3. Exit")

        op = input("Choose an option: ")

        match op:
            case "1":
                menu_visitors()
            case "2":
                menu_artefacts()
            case "3":
                print("Closing system...")
                exit()
            case _:
                print("Invalid option.")
def menu_visitors():
    while True:
        print("\n--- Visitor Management ---")
        print("1. Register visitor")
        print("2. List visitors")
        print("3. Search visitor by ID")
        print("4. Update visitor status")
        print("5. Delete visitor")
        print("6. Show statistics")
        print("7. Back to main menu")

        op = input("Choose an option: ")

        match op:
            case "1":
                register_visit()
            case "2":
                list_visitors()
            case "3":
                search_visitor_id()
            case "4":
                update_status()
            case "5":
                delete_visitor()
            case "6":
                visitors_stats()
            case "7":
                return
            case _:
                print("Invalid option.")
def menu_artefacts():
    while True:
        print("\n--- Artefact Management ---")
        print("1. Register artefact")
        print("2. List artefacts")
        print("3. Search artefact")
        print("4. Classify by rarity")
        print("5. Show statistics")
        print("6. Delete artefact")
        print("7. Back to main menu")

        op = input("Choose an option: ")

        match op:
            case "1":
                register_artefact()
            case "2":
                list_artefacts()
            case "3":
                search_artefact()
            case "4":
                classify_by_rarity()
            case "5":
                artefact_stats()
            case "6":
                delete_artefact()
            case "7":
                return
            case _:
                print("Invalid option.")
def entry_login():
    attempts = 3
    while attempts > 0:
        if login():
            print("Welcome superadmin!")
            main_menu()
        else:
            login_try(attempts)
    print('System Blocked')
    return False
entry_login()

