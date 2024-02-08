import sys

import ipdb
from models import Handler, Job, Owner, Pet, db

from app.database import app


def debug_hook(type, value, tb):
    # Call ipdb.launch_ipdb_on_exception with the correct arguments
    ipdb.launch_ipdb_on_exception(type, value, tb)


if __name__ == "__main__":

    with app.app_context():
        # 3✅ One to Many
        # Getting an owners pets
        # Use session.query and first to grab the first owner
        own1 = db.session.query(Owner).first()
        own2 = db.session.get(Owner, 2)
        # use db.session.query and filter_by to get the owners pets from Pet
        own1_pets = db.session.query(Pet).filter(Pet.owner_id == own1.id)
        own2_pets = own2.pets
        # print out your owners pets
        print([pet for pet in own1_pets])
        print([pet for pet in own2_pets])
        # Getting a pets owner
        # Use db.session.query and first to grab the first pet
        pet = db.session.get(Pet, 33)
        owner = db.session.query(Owner).filter(Owner.id == pet.owner_id)
        print([o for o in owner])
        # Use db.session.query and filter_by to get the owner associated with this pet

        # 4✅ Head back to models to build out a Many to Many
        # --------------------------------------------

        # 6.✅ Many to Many
        # Use db.session.query and .first to get the first handler
        handler = db.session.query(Handler).first()
        # Use db.session.query and the .filter_by to grab the jobs
        # handler_jobs = db.session.query(Job).filter(Job.handler_id == handler.id)
        handler_jobs = handler.jobs
        # ipdb.set_trace()
        # Print the jobs
        print([job for job in handler_jobs])
        # Use the handler_jobs to query pets for the associated pet to each job.
        handler_pets = [db.session.get(Pet, job.pet_id) for job in handler_jobs]
        print([pet for pet in handler_pets])
        # Optional breakpoint for debugging
        # current_frame = sys._getframe()
        # # current_namespace = current_frame.f_locals

    ipdb.set_trace(sys._getframe())
    # Set the debug_here function to be called on exceptions
    # sys.excepthook = debug_hook

    # Raise an exception to enter the debugger
    # raise Exception("Entering debugger")
