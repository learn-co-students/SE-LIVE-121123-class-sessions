from config import app, db, migrate

# from prompt_toolkit import prompt
from rich import print

# Configure the database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pet_app.db"
# db.init_app(app)


# def apply_migrations():
#     config = Config("alembic.ini")
#     config.set_main_option("sqlalchemy.url", db.engine.url)
#     command.upgrade(config, "head")


# Tasks:
# 1. Show all the pets
# 2. See a pet's details
# 3. See a pet's jobs
# 4. Add a job
# 5. Add a pet (stretch)

# Define interface operations


if __name__ == "__main__":
    # Apply migrations
    # apply_migrations()
    with app.app_context():
        migrate.init_app(app, db)

        # Define command line interface
