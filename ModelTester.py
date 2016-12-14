import inspect
from django.db import models

class ModelTester():
    _tested_models = []
    @staticmethod
    def checkModelType(modelElement):
        """
        Si verifica che stiamo testando un modello django
        """            
        if models.Model not in inspect.getmro(modelElement):
            raise Exception('Not a valid Django Model. Ancestors: %s' % inspect.getmro(modelElement) )
        try:
            meta = modelElement._meta
        except AttributeError:
            raise Exception('Not _meta attribute. Class: %s' % modelElement.__class__ )
        
    @staticmethod
    def _getModelHash(modelElement):
        return '%s %s' % ( modelElement.__module__, modelElement.__class__)
    
    @staticmethod
    def getModelHash(modelElement):
        ModelTester.checkModelType(modelElement)
        return ModelTester._getModelHash(modelElement)

    def testModel(self, modelElement):
        ModelTester.checkModelType(modelElement)
        """
        Si ricordano quali sono i modelli gia' testati
        """
        modelHash = self._getModelHash(modelElement)
        if modelHash in self._tested_models:
            return True
        else:
            self._tested_models.append(modelHash)
        
        
        
        return False