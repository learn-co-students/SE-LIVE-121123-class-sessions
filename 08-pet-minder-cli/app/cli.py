from db_utils import add_job_to_pet, find_pet_by_id, get_all_pets
from models import db
from rich import print

from app.database import app, migrate

# Tasks:
# 1. Show all the pets
# 2. See a pet's details
# 3. See a pet's jobs
# 4. Add a job
# 5. Add a pet (stretch)


# Define interface operations
def display_welcome():
    print("[magenta]Hello! Welcome to [/magenta][bold cyan]Pet Minder[/bold cyan]")


def display_main_menu():
    print("[bold cyan]Main Menu[/]")
    print("1. Show all pets")
    print("2. Add a pet")
    print("3. Exit")


def get_main_choice():
    return input("What is your command?")


def display_all_pets():
    pets = get_all_pets()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species} |")
    print("What would you like to do?")
    print("1. See more about a pet")
    print("2. Return to the main menu")
    choice = input()
    if choice == "1":
        choose_pet_by_id()
    else:
        pass


def choose_pet_by_id():
    search_id = input("Enter the id of the pet you'd like to see")
    pet = find_pet_by_id(search_id)
    print(
        f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Temperament: {pet.temperament}"
    )
    display_pet_submenu(pet)


def display_pet_submenu(pet):
    print("1. See a pet's jobs")
    print("2. Add a job to a pet")
    print("3. Exit")
    print("What would you like to do?")
    choice = input()
    handle_pet_choice(choice, pet)


def handle_pet_choice(choice, pet):
    if choice == "1":
        show_pets_jobs(pet)
    elif choice == "2":
        add_job(pet)
    else:
        display_main_menu()


def add_job(pet):
    add_job_to_pet(pet)
    show_pets_jobs(pet)


def show_pets_jobs(pet):
    jobs = pet.jobs
    for job in jobs:
        print(
            f"{job.id} | {job.request} | {job.date} | {job.notes} | ${job.fee:.2f} || with {job.handler.name}"
        )
    display_pet_submenu(pet)


def goodbye():
    print("Goodbye! Thanks for using the Pet Minder App!")


if __name__ == "__main__":
    # Give app context at runtime and initialize Migrate obj
    with app.app_context():
        migrate.init_app(app, db)

        # Define command line interface
        display_welcome()
        while True:
            display_main_menu()
            choice = get_main_choice()
            if choice == "1":
                display_all_pets()
            elif choice == "2":
                print("add pet feature coming soon")
            else:
                break
        goodbye()
