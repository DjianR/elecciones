from django.contrib import admin
from actas.models import Region, Provincia, Distrito, Partido, CentroVotacion, Mesa, DisenioActaMunicipal, DetalleDisenioActaMunicipal,DisenioActaRegional, DetalleDisenioActaRegional, ActaMunicipal,DetalleActaMunicipal, VotacionPresidenteRegional,VotacionConsejeroRegional, VotacionProvincial, VotacionDistrital, ActaRegional

class DetalleDisenioActaMunicipalEnLinea(admin.TabularInline):
	model = DetalleDisenioActaMunicipal
		
class DisenioActaMunicipalAdmin(admin.ModelAdmin):
	inlines = [DetalleDisenioActaMunicipalEnLinea]

class DetalleDisenioActaRegionalEnLinea(admin.TabularInline):
	model = DetalleDisenioActaRegional
		
class DisenioActaRegionalAdmin(admin.ModelAdmin):

	inlines = [DetalleDisenioActaRegionalEnLinea]

class MesaAdmin(admin.ModelAdmin):
	search_fields = ('numero',)

class ProvinciaAdmin(admin.ModelAdmin):
	ordering = ('nombre',)

class DistritoAdmin(admin.ModelAdmin):
	ordering = ('nombre',)

class CentroVotacionAdmin(admin.ModelAdmin):
	ordering = ('distrito','nombre',)	

admin.site.register(Region)
admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Partido)
admin.site.register(CentroVotacion, CentroVotacionAdmin)
admin.site.register(Mesa,MesaAdmin)
admin.site.register(ActaMunicipal)
admin.site.register(ActaRegional)
admin.site.register(DetalleActaMunicipal)
admin.site.register(VotacionPresidenteRegional)
admin.site.register(VotacionConsejeroRegional)
admin.site.register(VotacionProvincial)
admin.site.register(VotacionDistrital)
admin.site.register(DisenioActaMunicipal, DisenioActaMunicipalAdmin)
admin.site.register(DisenioActaRegional, DisenioActaRegionalAdmin)