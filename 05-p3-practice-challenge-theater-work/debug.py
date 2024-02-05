import ipdb
from faker import Faker

from lib.audition import Audition
from lib.role import Role

fake = Faker()

romeo = Role("romeo")
juliet = Role("juliet")
roles = [romeo, juliet]

a1 = Audition(romeo, fake.name(), fake.address(), fake.phone_number())
for role in roles:
    for _ in range(5):
        Audition(role, fake.name(), fake.address(), fake.phone_number())

ipdb.set_trace()
