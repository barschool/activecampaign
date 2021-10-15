import os
from datetime import date
from pprint import pprint

from dotenv import load_dotenv
load_dotenv()

from ac import find_contact_id

print(find_contact_id(name='Malmo'))
print(find_contact_id(name='Rome'))
print(find_contact_id(name='Milan'))
print(find_contact_id(name='Goa'))
print(find_contact_id(name='Bangalore'))

