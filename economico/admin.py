from django.contrib import admin
from .models import RubroVenta,Subrubro,Gasto,Umedida,Empleado,GastoMO,Venta,RubroGasto,Cliente,Proveedor,Gasto

class GastoAdmin(admin.ModelAdmin):
    list_display = ['fecha','rubro','subrubro','importe','iva','imp_total']

class VentaAdmin(admin.ModelAdmin):
    list_display = ['fecha','rubro','cantidad','unidades','importe','iva','imp_total']

# class GastoAdmin(admin.ModelAdmin):
#     list_display = ['fecha','proveedor','comprobante','concepto','importe_total']

admin.site.register(RubroVenta)
admin.site.register(RubroGasto)
admin.site.register(Subrubro)
admin.site.register(Gasto,GastoAdmin)
admin.site.register(Umedida)
admin.site.register(Empleado)
admin.site.register(GastoMO)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Cliente)

