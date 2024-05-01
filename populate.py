import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sprakashjobs.settings')
import django
django.setup()

from faker import Faker
from testapp.models import HydJobs
from testapp.models import BanJobs
from testapp.models import MumbJobs
from random import *
fake = Faker()
def phonenumbergen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements = ('project manager','Team Leader','s/w Engineer','HR','Associate Engineer'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
        ban_jobs_record = BanJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
        mumb_jobs_record = MumbJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n = int(input('Enter no of Records: '))
populate(n)
print(f'{n} records inserted Successfully...')
