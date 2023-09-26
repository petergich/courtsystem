from django.contrib import admin
from .models import clients_id,advocates_roll_number,lawyers,case,charge_sheet,demand_letter,client

admin.site.register(clients_id)
admin.site.register(advocates_roll_number)
admin.site.register(demand_letter)
admin.site.register(charge_sheet)
admin.site.register(case)
admin.site.register(client)
admin.site.register(lawyers)
# Register your models here.
