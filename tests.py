from django.test import TestCase
from django.db import models
from DjangoModelTester.models import ModelTesterRealModel
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
        
    def test_testMethod(self):
        el = ModelTester()
        self.assertRaises(Exception, el.testModel, modelElement=ModelTesterAbstractModel)
        
        
"""
AutoField
BigAutoField
BigIntegerField
BinaryField
BooleanField
CharField
CommaSeparatedIntegerField
DateField
DateTimeCheckMixin
DateTimeField
DecimalField
DeferredAttribute
DictWrapper
DurationField
EmailField
Empty
Field
FieldDoesNotExist
FilePathField
FloatField
GenericIPAddressField
IPAddressField
IntegerField
NOT_PROVIDED
NullBooleanField
PositiveIntegerField
PositiveIntegerRelDbTypeMixin
PositiveSmallIntegerField
Promise
RegisterLookupMixin
RemovedInDjango20Warning
SlugField
SmallIntegerField
TextField
TimeField
URLField
UUIDField
cached_property
warn_about_renamed_method
"""