from datetime import datetime

from models import Handler, Job, Pet, db
from pick import pick


def get_all_pets():
    return db.session.query(Pet).all()


def find_pet_by_id(id):
    return db.session.get(Pet, id)


def add_job_to_pet(pet):
    handler_names = [handler.name for handler in db.session.query(Handler).all()]
    title = "Which handler will be taking care of this job?"
    handler_name, index = pick(handler_names, title)
    handler = db.session.query(Handler).filter(Handler.name == handler_name).first()
    req_type = "What type of job are you requesting?"
    request_choice, index = pick(["Walk", "Drop-in", "Boarding"], req_type)
    date_string = input("Enter date and time in the format YYYY-MM-DD HH:MM:SS: ")
    date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    notes = input("Enter any special notes for the handler")
    job = Job(
        request=request_choice,
        handler_id=handler.id,
        pet_id=pet.id,
        date=date,
        notes=notes,
        fee=handler.hourly_rate,
    )
    db.session.add(job)
    db.session.commit()
