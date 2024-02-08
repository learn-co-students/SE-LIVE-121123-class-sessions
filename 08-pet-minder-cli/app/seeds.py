import random

from faker import Faker
from models import Handler, Job, Owner, Pet, db

from app.database import app

if __name__ == "__main__":
    with app.app_context():
        # 2.a ✅ Add delete methods for Pet and Owner to clear the database before each seeding

        # ----------
        # 5.✅ Add Delete methods for Job and Handler
        db.session.query(Pet).delete()
        db.session.query(Owner).delete()

        # Initialize faker
        fake = Faker()
        # Create an list for species with "CAT" and "Dog"
        species = ["CAT", "DOG"]
        # Create an list of cat breeds
        cat_breeds = [
            "Domestic long hair",
            "Domestic short hair",
            "Siamese",
            "Ragdoll",
            "Sphynx",
            "Burmese",
        ]

        # Create an list of dog breeds
        dog_breeds = [
            "Mix",
            "Husky",
            "Malamute",
            "Dachshound",
            "Samoyed",
            "Shiba Inu",
            "Corgi",
        ]

        # Create an list of temperaments
        temperament = ["Calm", "Nervous", "Mischievous", "Aggressive", "Hyper"]

        # Create an empty list for owners
        owners = []
        # Create a for loop that iterates 50 times
        for _ in range(50):
            # Create an owner using data from faker
            owner = Owner(
                name=f"{fake.first_name()} {fake.last_name()}",
                email=fake.email(),
                phone=random.randint(1000000000, 9999999999),
                address=fake.address(),
            )

            # Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
            db.session.add(owner)
            db.session.commit()
            # Append the owner to the owners list
            owners.append(owner)

        # Create an empty pets list
        pets = []
        # Create a for loop that iterates over the owners list
        for owner in owners:
            # Create a for loop that iterates 1 - 3 times
            for _ in range(random.randint(1, 3)):
                # Use faker and the species, cat breeds, dog breeds and temperament list to create a pet
                rand_species = random.choice(species)
                pet = Pet(
                    name=fake.name(),
                    species=rand_species,
                    breed=(
                        random.choice(cat_breeds)
                        if rand_species == "CAT"
                        else random.choice(dog_breeds)
                    ),
                    temperament=random.choice(temperament),
                    owner_id=owner.id,
                )
                # Use .add and .commit to save the pet to the database
                db.session.add(pet)
                db.session.commit()
                # Append the pet to the pets list
                pets.append(pet)
        # 3✅ run the seed file and head over to debug.py to test out your one to many
        # -----------------------------------------------------

        # 5.✅ Create a empty list set to handlers
        handlers = []
        # Create a for loop that iterates 50 times
        for _ in range(50):
            # Create a handler with faker data
            handler = Handler(
                name=f"{fake.first_name()} {fake.last_name()}",
                email=fake.email(),
                phone=random.randint(1000000000, 9999999999),
                hourly_rate=random.uniform(25.50, 80.50),
            )
            # Use .add and .commit to save the handler to the database
            db.session.add(handler)
            db.session.commit()
            # Append handler to handlers
            handlers.append(handler)
        # Create an list of requests, "Walk", "Drop-in" and "Boarding"
        requests = ["Walk", "Drop-in", "Boarding"]

        # Create an empty list and set it to jobs
        jobs = []
        # Create a for loop that iterates over the handlers list
        for handler in handlers:
            # Create a for loop that iterates 1 - 10 times
            for _ in range(random.randint(1, 10)):
                # Create a Job using faker, the request list and pets list
                job = Job(
                    request=random.choice(requests),
                    date=fake.date_this_year(),
                    notes=fake.sentence(),
                    fee=handler.hourly_rate,
                    handler_id=handler.id,
                    pet_id=random.choice(pets).id,
                )
                # append the job to the jobs list
                jobs.append(job)
        # Bulk save the jobs (we wont need their id)
        db.session.bulk_save_objects(jobs)
        db.session.commit()
        db.session.close()

    # 6.✅ Run the seeds file and head over to debug.py to test out your Many to Many
