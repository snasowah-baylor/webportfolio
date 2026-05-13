from django.test import TestCase
from .models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            summary="A test project",
            description="Test description",
            category="AI",
            tools_used="Django, Python",
            key_features="Feature 1, Feature 2",
            role_contribution="Full development",
            challenges="Challenge description",
            lessons_learned="Lessons learned description",
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.category, "AI")

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")
