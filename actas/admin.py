from django.contrib import admin
from actas.models import Region, Provincia, Distrito, Partido, CentroVotacion, Mesa, DiseñoActa, DetalleDiseñoActa

class DetalleDiseñoActaEnLinea(admin.TabularInline):
	model = DetalleDiseñoActa
		
class DiseñoActaAdmin(admin.ModelAdmin):

	inlines = [DetalleDiseñoActaEnLinea]

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Partido)
admin.site.register(CentroVotacion)
admin.site.register(Mesa)
admin.site.register(DiseñoActa, DiseñoActaAdmin)