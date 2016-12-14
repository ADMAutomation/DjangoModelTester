from DjangoModelTester.ModelTester import ModelTester
from django.db.models.fields import NOT_PROVIDED

from DjangoModelTester.models import ModelTesterRealModel
d = ModelTesterRealModel()
print dir(ModelTesterRealModel._meta)

fs = ModelTesterRealModel._meta.get_fields()

el = ModelTesterRealModel()
f = el._meta.get_fields()
el = ModelTester._fillStandardField(f[2], el)

import inspect, sys
from django.db.models import fields
for name, obj in inspect.getmembers(sys.modules['django.db.models.fields']):
    if inspect.isclass(obj):
        print name
