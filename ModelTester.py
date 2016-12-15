import inspect
from django.db import models
from django.db.models.fields import NOT_PROVIDED
from autofixture import AutoFixture

class ModelTester():
    models_to_test = []
    actions = ['create', 'delete']
    verbose = True
    def runTests(self):
        for modelElement in self.models_to_test:
            self.testModel(modelElement)
    
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
        return '%s %s' % ( modelElement.__module__, modelElement)
    
    @staticmethod
    def getModelHash(modelElement):
        ModelTester.checkModelType(modelElement)
        return ModelTester._getModelHash(modelElement)
    @staticmethod
    def _mustCheck(f):
        if f.null or f.auto_created or f.default != NOT_PROVIDED:
            """
            Not tested
            """
            return False
        return True
        
    @staticmethod
    def _getModelInstance(modelElement, empty=False):
        if modelElement._meta.abstract:
            raise Exception('Can\'t make instance of an Abstract model. Class: %s' % modelElement.__class__ )
               
        if empty:
            return modelElement()
        
        fixtures = AutoFixture(modelElement, generate_fk=True, none_p=1, overwrite_defaults=False )
        return fixtures.create(1)[0]
    
    @staticmethod
    def getModelInstance(modelElement, empty=False):
        ModelTester.checkModelType(modelElement)
        return ModelTester._getModelInstance(modelElement, empty)

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
        
        """
        Si comunica che inizia il test del modello alla shell
        """
        if self.verbose:
            print 'Testing model %s' % (modelElement._meta.verbose_name)
                
        """
        Si crea un'instanza del modello che si vuole testare
        """
        el = ModelTester._getModelInstance(modelElement)
        if 'delete' in self.actions:
            """
            Si cancella l'istanza appena creata
            """
            el.delete()
        return True