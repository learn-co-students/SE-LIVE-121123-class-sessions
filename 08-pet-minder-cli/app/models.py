# 1.✅ Create models to include a One to Many association
# Pet >- Owner

from app.database import db


class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    temperament = db.Column(db.String)

    # 1.a✅ Add  ForeignKey('owners.id') to owner)id
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    # 4b. Associate the models with relationship("<ModelNameHere>", backref="<singular of tablename>")
    jobs = db.relationship("Job", backref=db.backref("job"))

    def __repr__(self):
        return (
            f"Id: {self.id}, "
            + f"Name: {self.name}, "
            + f"Species: {self.species}, "
            + f"Breed: {self.breed}, "
            + f"Temperament: {self.temperament}"
        )


# 1.b✅ Add an Owners table
class Owner(db.Model):
    __tablename__ = "owners"
    # Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # address -> type string
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)
    address = db.Column(db.String)
    # 1.c✅ Associate the Pet model with the owner Model
    pets = db.relationship("Pet", backref="owner")

    # add a __repr__ method that returns a string containing the id, name, email, phone and address of our class
    def __repr__(self):
        return (
            f"Id: {self.id}, "
            + f"Name: {self.name}, "
            + f"Email: {self.email}, "
            + f"Phone: {self.phone}, "
            + f"Address: {self.address}"
        )


# 2.✅ Update your migrations by running `flask db migrate -m "create pets and owners"` and `flask db upgrade head`


# After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

# 4.✅ Update our Model to have a Many to Many association
# Pet-< Jobs >- Handlers


class Handler(db.Model):
    __tablename__ = "handlers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.Integer)
    hourly_rate = db.Column(db.Float)
    # 4b. Associate the models with relationship("<ModelNameHere>", backref="<singular of tablename>")
    jobs = db.relationship("Job", backref="handler")


class Job(db.Model):

    def __repr__(self):
        return (
            f"Id: {self.id}, "
            + f"Name: {self.name}, "
            + f"Email: {self.email}, "
            + f"Phone: {self.phone}, "
            + f"Hourly Rate: {self.hourly_rate}"
        )

    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String)
    date = db.Column(db.DateTime)
    notes = db.Column(db.String)
    fee = db.Column(db.Float)
    # 4a. add columns for foreign keys
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"))
    handler_id = db.Column(db.Integer, db.ForeignKey("handlers.id"))

    def __repr__(self):
        return (
            f"Id: {self.id}, "
            + f"Request: {self.request}, "
            + f"Date: {self.date}, "
            + f"Notes: {self.notes}, "
            + f"Fee: {self.fee}, "
            + f"Pet ID: {self.pet_id}, "
            + f"Handler ID: {self.handler_id}"
        )


# 5.✅ Update your migrations by running `flask db migrate -m "create pets and owners"` and `flask db upgrade head`

# After running your migrations, go build out some seeds and test your many to many with debug.py
