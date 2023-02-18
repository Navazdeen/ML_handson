from django.test import TestCase, Client
from django.urls import reverse, resolve
from Home.models import StudentBio


class TestingViews(TestCase):

    def test_index_get_data(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/index.html')

    def test_index_post_data(self):
        client = Client()
        response = client.post('', {
            "Email": "test@email.com",
            "Name": "Test",
            "Age": 12,
            "Gender": 'F'
        })
        Email = StudentBio.objects.first().Email
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/index.html')
        self.assertEqual(Email, "test@email.com")

    def test_delete_get_data(self):
        client = Client()
        StudentBio.objects.create(
            id=10,
            Email="test@email.com",
            Name="Test",
            Age=12,
            Gender='F'
        )
        url = reverse('modify', kwargs={'id': 10})
        response = client.delete(url)
        self.assertEqual(response.status_code, 200)

    def test_modify_get_data(self):
        client = Client()
        StudentBio.objects.create(
            id=10,
            Email="test@email.com",
            Name="Test",
            Age=12,
            Gender='F'
        )
        url = reverse('modify', kwargs={'id': 10})
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/modify.html')
    
    def test_modify_data_post(self):
        client = Client()
        StudentBio.objects.create(
            id=10,
            Email="test@email.com",
            Name="Test",
            Age=12,
            Gender='F'
        )
        url = reverse('modify', kwargs={'id': 10})
        response = client.post(url, {
            "Email": "test1@email.com",
            "Name": "Test",
            "Age": 12,
            "Gender": 'F'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(StudentBio.objects.get(id=10).Email, "test1@email.com")

