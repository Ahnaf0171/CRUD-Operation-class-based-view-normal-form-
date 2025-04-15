from django.contrib import admin
from new_gadget.models import Gadget_table

# Register your models here.
class Gadget_tableAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'picture', 'price', 'about')
admin.site.register(Gadget_tableAdmin, Gadget_table)
