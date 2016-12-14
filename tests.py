from django.test import TestCase
from django.db import models
from DjangoModelTester.models import ModelTesterRealModel, ModelTesterRelatedRealModel
from DjangoModelTester.ModelTester import ModelTester

class ModelTesterAbstractModel(models.Model):
    class Meta:
        abstract = True

# Create your tests here.
class ModelTesterTestCase(TestCase):
    def test_class_declaration(self):
        el = ModelTester()
    
    def test_methods(self):
        """
        checkModelType
        """
        self.assertEqual(ModelTester.checkModelType(ModelTesterAbstractModel), None)
        self.assertRaises(Exception, ModelTester.checkModelType, modelElement='1234')
        self.assertRaises(Exception, ModelTester.checkModelType, modelElement=models.Model)
        
        """
        getModelHash
        """
        self.assertIsNot(ModelTester.getModelHash(ModelTesterAbstractModel), None)
        
        """
        getModelInstance
        """
        self.assertRaises(Exception, ModelTester.getModelInstance, modelElement=models.Model)
        ModelTester.getModelInstance(ModelTesterRealModel)
    
    def test_getInstance(self):
        el = ModelTester._getModelInstance(ModelTesterRealModel, True)
        el = ModelTester._getModelInstance(ModelTesterRealModel, False)
        el = ModelTester._getModelInstance(ModelTesterRelatedRealModel)
                
    def test_testModelMethod(self):
        el = ModelTester()
        self.assertRaises(Exception, el.testModel, modelElement=ModelTesterAbstractModel)
        
    def test_testOnModelList(self):
        el = ModelTester()
        el.models_to_test = [ModelTesterRealModel, ModelTesterRelatedRealModel]
        el.runTests()
        