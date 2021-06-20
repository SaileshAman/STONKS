from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Broker)
admin.site.register(Stock)
admin.site.register(Client_Stock)
admin.site.register(Client_Broker)