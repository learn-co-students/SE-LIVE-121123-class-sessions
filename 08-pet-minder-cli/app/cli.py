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


if __name__ == "__main__":
    # Give app context at runtime and initialize Migrate obj
    with app.app_context():
        migrate.init_app(app, db)

        # Define command line interface
