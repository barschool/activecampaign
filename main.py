import os
from datetime import date
from pprint import pprint

from dotenv import load_dotenv
load_dotenv()

from ac import find_contact_id, trigger_eval_automation
from db import courses_by_startdate

DATE = date.today()
TYPES = ['basic-bartending-cou','4-week-international','advanced-bartender-c','barista-academy']
no_results = True

print(f"Finding courses...")
for (num_bookings, start_date, course_ref, destination_ref, name,) in courses_by_startdate(startdate=DATE, course_type_refs=TYPES):
    no_results = False
    print(f"{course_ref} in {name} starting today, finding ac contact id...")
    contact_id = find_contact_id(name)
    if contact_id:
        print(f"{name} found, adding contact {contact_id} to automation.")
        trigger_eval_automation(contact_id)
    else:
        print(f"Contact {name} not found in ActiveCampaign.")

if no_results:
    print('No courses starting today found.')