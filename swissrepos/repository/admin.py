from django.contrib import admin
from repository.models import *

admin.site.register(Repository)
admin.site.register(Category)
admin.site.register(Indicator)
admin.site.register(IndicatorValue)
admin.site.register(MetricCategory)
admin.site.register(IndicatorCategory)