import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondProject.settings')

import django
django.setup()
import random
from secondApp.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def get_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populateApp(n=5):
    for i in range(n):
        top = get_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == "__main__":
    print('populating APP')
    populateApp(5)
    print('Completed')
