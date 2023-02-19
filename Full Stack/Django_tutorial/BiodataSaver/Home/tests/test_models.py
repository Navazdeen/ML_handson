from django.test import TestCase
from Home.models import StudentBio


class TestingModels(TestCase):

    def setUp(self):
        self.student1 = StudentBio.objects.create(
            Email="test@gmail.com",
            Name="Test",
            Age=19,
            Gender='M'
        )

    def test_create_entry_studentBio(self):
        self.assertEqual(StudentBio.objects.first().Email, 'test@gmail.com')
        self.assertEqual(StudentBio.objects.count(), 1)
    
    def test_modify_entry_studentBio(self):
        self.student1.Email = "test1@gmail.com"
        self.student1.save()

        self.assertEqual(StudentBio.objects.first().Email, "test1@gmail.com")
        self.assertEqual(StudentBio.objects.count(), 1)

    def test_delete_entry_studentBio(self):
        self.student1.delete()

        self.assertEqual(StudentBio.objects.count(), 0)
    
    def test_search_entry_studentBio(self):
        self.student2 = StudentBio.objects.create(
            Email="test@gmail.com",
            Name="Test",
            Age=19,
            Gender='M'
        )
        self.student3 = StudentBio.objects.create(
            Email="test1@gmail.com",
            Name="Test1",
            Age=19,
            Gender='M'
        )

        search = StudentBio.search('Test1')

        self.assertEqual(search.count(), 1)
        self.assertEqual(search[0].Email, "test1@gmail.com")