from django.contrib import admin
from actas.models import Region, Provincia, Distrito, Partido, CentroVotacion, Mesa, DisenioActa, DetalleDisenioActa

class DetalleDisenioActaEnLinea(admin.TabularInline):
	model = DetalleDisenioActa
		
class DisenioActaAdmin(admin.ModelAdmin):

	inlines = [DetalleDisenioActaEnLinea]

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Partido)
admin.site.register(CentroVotacion)
admin.site.register(Mesa)
admin.site.register(DisenioActa, DisenioActaAdmin)