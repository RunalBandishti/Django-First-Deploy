import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project1.settings')

import django
django.setup()

##fake pop script
import random
from demo.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topics=['Search','Social','MarketPlace','News','Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        #get the topics for the entry
        top=add_topics()

        #create the fake entry
        fake_url= fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake accessRecord
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print ("populating script")
    populate(20)
    print ("populating complete")
