from .models import Person

def func_persons(request):
    person = Person.objects.all()
    return {'func_persons': person}