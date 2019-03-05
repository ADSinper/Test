from django.shortcuts import render


# Create your views here.
from books.models import Publisher
from django.shortcuts import HttpResponse


def insertdata(request):
    """Insert data into database"""
    p1 = Publisher.objects.create(name='Apress',
                                  address='2855 Telegraph Avenue',
                                  city='Beijing',
                                  state_province='BJ',
                                  country='China',
                                  website='http://www.apress.com/',
                                  )
    p1.save()
    p2 = Publisher.objects.create(name='freax',
                                  address='2855 Telegraph Avenue',
                                  city='Chengdu',
                                  state_province='SC',
                                  country='China',
                                  website='http://www.freax.com/',
                                  )
    p2.save()
    return HttpResponse('OK')

