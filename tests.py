from django.test import TestCase
from django.db import models
from DjangoModelTester.ModelTester import ModelTester

class ExampleModel(models.Model):
    class Meta:
        abstract = True

# Create your tests here.
class ModelTesterTestCase(TestCase):
    def test_class_declaration(self):
        el = ModelTester()
    
    def test_methods(self):
        self.assertEqual(ModelTester.checkModelType(ExampleModel), None)
        self.assertRaises(Exception, ModelTester.checkModelType, modelElement='1234')
        self.assertRaises(Exception, ModelTester.checkModelType, modelElement=models.Model)
        self.assertIsNot(ModelTester.getModelHash(ExampleModel), None)