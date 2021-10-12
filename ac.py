import os
from pprint import pprint

from activecampaign.client import Client

URL = os.getenv('ACTIVECAMPAIGN_URL')
API_KEY = os.getenv('ACTIVECAMPAIGN_API_KEY')
EVALUATION_AUTOMATION_ID = os.getenv('EVALUATION_AUTOMATION_ID')

ac = Client(URL, API_KEY)

def find_contact_id(name):
    search_results = ac.contacts.list_all_contacts(search='EBS ' + name)
    contact = next(iter(search_results['contacts']), None)
    return contact['id'] if contact else None

def trigger_eval_automation(contact_id):
    r = ac.contacts.add_a_contact_to_an_automation({
        "contactAutomation": {
            "contact": contact_id,
            "automation": EVALUATION_AUTOMATION_ID
        }
    })
