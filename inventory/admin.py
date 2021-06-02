from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import Laptops, Desktops, Mobiles
# Register your models here.

admin.site.register(Laptops)
admin.site.register(Desktops)
admin.site.register(Mobiles)
