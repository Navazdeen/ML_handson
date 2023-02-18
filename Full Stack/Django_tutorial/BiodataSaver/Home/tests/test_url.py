from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Home.views import index, delete, modify


class TestingUrl(SimpleTestCase):

    def test_url_index_resolves(self):
        index_url = reverse('index')
        self.assertEqual(resolve(index_url).func, index)

    def test_url_delete_resolves(self):
        delete_url = reverse('delete', args=[1])
        self.assertEqual(resolve(delete_url).func, delete)

    def test_url_modify_resolves(self):
        modify_url = reverse('modify', args=[1])
        self.assertEqual(resolve(modify_url).func, modify)

