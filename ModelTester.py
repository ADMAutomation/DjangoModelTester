# import time
import inspect, hashlib
from django.db import models
from django.db.models.fields import NOT_PROVIDED
from autofixture import AutoFixture

class ModelTester():
    models_to_test = []
    models_values = {}
    actions = ['create', 'delete', 'string']
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
        w = '%s%s' % ( modelElement.__module__, modelElement)
        return hashlib.md5(w).hexdigest()[:15]
    
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
        
    def _getModelInstance(self, modelElement, empty=False, field_values=None):
        if modelElement._meta.abstract:
            raise Exception('Can\'t make instance of an Abstract model. Class: %s' % modelElement.__class__ )
               
        if empty:
            return modelElement()
        if field_values is None:
            h = self._getModelHash(modelElement)
            if h in self.models_values.keys():
                field_values = self.models_values[h]
        fixtures = AutoFixture(modelElement, field_values=field_values, none_p=1, overwrite_defaults=False, generate_fk=True )
        return fixtures.create(1)[0]
    
    @staticmethod
    def getModelInstance(modelElement, empty=False, field_values=None):
        if modelElement._meta.abstract:
            raise Exception('Can\'t make instance of an Abstract model. Class: %s' % modelElement.__class__ )
               
        if empty:
            return modelElement()
        
        fixtures = AutoFixture(modelElement, generate_fk=True, none_p=1, overwrite_defaults=False, field_values=field_values )
        return fixtures.create(1)[0]

    def testModel(self, modelElement, field_values=None):
        ModelTester.checkModelType(modelElement)
        # start_time = time.time()
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
        el = self._getModelInstance(modelElement, field_values=field_values)
        el.clean()
        
        """
        Si testa la versione stringa del modello
        """
        if 'string' in self.actions:
            str(el)
            
        """
        Si testa l'eliminazione
        """
        if 'delete' in self.actions:
            """
            Si cancella l'istanza appena creata
            """
            el.delete()
        # print "Time: %s" % (time.time() - start_time)
        return True