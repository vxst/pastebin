import random
import re

from django.test import TestCase, Client

from .models import Paste


class PasteModelTests(TestCase):
    """
    This is a test for a model
    """
    def test_create(self):
        paste = Paste(title='123456', content='hello')
        self.assertEqual(paste.title, '123456')
        self.assertEqual(paste.content, 'hello')

    def test_save_load(self):
        for _ in range(100):
            title = f'{random.randrange(0, 1000000):06}'
            content = f'{random.randrange(0, 1000000):06}'
            paste = Paste(title=title, content=content)
            paste.save()

            new_paste = Paste.objects.get(title=title)
            self.assertEqual(new_paste.content, content)


class AppTests(TestCase):
    """
    This is a test for the app
    """
    def test_exists(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        response = client.post('/add', {'content': "1314"})
        self.assertEqual(response.status_code, 200)
        title = f'{random.randrange(0, 1000000):06}'
        content = f'{random.randrange(0, 1000000):06}'
        paste = Paste(title=title, content=content)
        paste.save()
        response = client.post('/get', {'title': title})
        self.assertEqual(response.status_code, 200)

    def test_add_and_get(self):
        client = Client()
        content = f'{random.randrange(0, 1000000):06}'

        response = client.post('/add', {'content': content}, follow=True)
        finder = re.compile(r"<h2>\d{6}</h2>")
        code = finder.search(str(response.content))[0][4:-5]

        response = client.post('/get', {'title': code}, follow=True)
        finder = re.compile(r">\d{6}<")
        value = finder.search(str(response.content))[0][1:-1]

        self.assertEqual(value, content)

