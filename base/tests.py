from django.test import TestCase

 room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context={'room':room}
