from django.shortcuts import render
from actas.models import Region, Provincia, Distrito, CentroVotacion, Mesa, Acta, DetalleActa, DiseñoActa, DetalleDiseñoActa, VotacionDistrital, VotacionProvincial, VotacionRegional
from django.views.generic import TemplateView, ListView, DetailView
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import csv

# Create your views here.
def mesa(request):
	mesas = Mesa.objects.filter(procesada=False)
	if request.method == 'POST':
		mesa = request.POST['mesas']
		try: 
			obj_mesa = Mesa.objects.get(pk=mesa)
			return HttpResponseRedirect(reverse('actas:acta', args=[mesa]))
		except Mesa.DoesNotExist:
			return HttpResponseRedirect(reverse('actas:mesa'))
	context = {'mesas':mesas}
	return render(request, 'actas/mesa.html', context)

def acta(request, numero):
	mesa = Mesa.objects.get(numero=numero)
	centro_votacion = mesa.centro_votacion
	distrito = centro_votacion.distrito
	provincia = distrito.provincia
	region = provincia.region
	try:
		diseño_acta = DiseñoActa.objects.get(distrito=distrito)
	except DiseñoActa.DoesNotExist:
		return HttpResponseRedirect(reverse('admin:login'))
	detalles = DetalleDiseñoActa.objects.filter(diseño_acta=diseño_acta)
	
	if request.method == 'POST':
		votos_blancos_reg = request.POST['voto_blanco_reg']
		votos_nulos_reg = request.POST['voto_nulo_reg']
		votos_imp_reg = request.POST['voto_impugnado_reg']
		votos_tot_reg = request.POST['voto_total_regional']
		votos_blancos_prov = request.POST['voto_blanco_prov']
		votos_nulos_prov = request.POST['voto_nulo_prov']
		votos_imp_prov = request.POST['voto_impugnado_prov']
		votos_tot_prov = request.POST['voto_total_provincial']
		
		if not distrito.capital_provincia:
			votos_blancos_dis = request.POST['voto_blanco_dis']
			votos_nulos_dis = request.POST['voto_nulo_dis']
			votos_imp_dis = request.POST['voto_impugnado_dis']
			votos_tot_dis = request.POST['voto_total_distrital']
		else:
			votos_blancos_dis = 0
			votos_nulos_dis = 0
			votos_imp_dis = 0
			votos_tot_dis = 0

		acta = Acta(mesa=mesa,votos_blancos_reg=votos_blancos_reg,votos_blancos_prov=votos_blancos_prov,
			votos_blancos_dis=votos_blancos_dis,votos_nulos_reg=votos_nulos_reg,votos_nulos_prov=votos_nulos_prov,
			votos_nulos_dis=votos_nulos_dis,votos_impugnados_reg=votos_imp_reg,
			votos_impugnados_prov=votos_imp_prov,votos_impugnados_dis=votos_imp_dis,
			votos_emitidos_reg=votos_tot_reg,votos_emitidos_prov=votos_tot_prov,votos_emitidos_dis=votos_tot_dis)
		acta.save()
		for detalle in detalles:
			reg = "reg_"+str(detalle.partido.pk)
			votos_regional = request.POST[reg]
			prov = "prov_"+str(detalle.partido.pk)
			votos_provincial = request.POST[prov]
			dis = "dis_"+str(detalle.partido.pk)
			votos_distrital = request.POST[dis]
			
			if not votos_regional.isnumeric():
				votos_regional=0
			else:
				try:
					vot_reg = VotacionRegional.objects.get(partido=detalle.partido, region=region)
				except VotacionRegional.DoesNotExist:
					vot_reg = VotacionRegional(partido=detalle.partido, region=region)
				vot_reg.votos = vot_reg.votos + int(votos_regional)
				vot_reg.save()

			if not votos_provincial.isnumeric():
				votos_provincial=0
			else:
				try:
					vot_prov = VotacionProvincial.objects.get(partido=detalle.partido, provincia=provincia)
				except VotacionProvincial.DoesNotExist:
					vot_prov = VotacionProvincial(partido=detalle.partido, provincia=provincia)
				vot_prov.votos = vot_prov.votos + int(votos_provincial)
				vot_prov.save()
				
			if not votos_distrital.isnumeric():
				votos_distrital=0
			else:
				try:
					vot_dis = VotacionDistrital.objects.get(partido=detalle.partido, distrito=distrito)
				except VotacionDistrital.DoesNotExist:
					vot_dis = VotacionDistrital(partido=detalle.partido, distrito=distrito)
				vot_dis.votos = vot_dis.votos + int(votos_distrital)
				vot_dis.save()

			detalle_acta = DetalleActa(acta=acta,partido=detalle.partido,votos_regional=votos_regional,
				votos_provincial=votos_provincial,votos_distrital=votos_distrital)
			detalle_acta.save()
		mesa.procesada=True
		mesa.save()
		return HttpResponseRedirect(reverse('actas:mesa'))

	context = {'distrito':distrito,'provincia':provincia,'region':region,'diseño_acta':diseño_acta,
	'detalles':detalles,'mesa':mesa}
	return render(request, 'actas/acta.html', context)

class BusquedaProvincias(TemplateView):

	def get(self, request, *args, **kwargs):
		region = request.GET['region']
		provincias = Provincia.objects.filter(region=region)
		if provincias:
			data = serializers.serialize('json', provincias, fields= ('pk','nombre'))
		else:
			data = []
		return HttpResponse(data, content_type='application/json')

class BusquedaDistritos(TemplateView):

	def get(self, request, *args, **kwargs):
		provincia = request.GET['provincia']
		distritos = Distrito.objects.filter(provincia=provincia)
		if distritos:
			data = serializers.serialize('json', distritos, fields= ('id','nombre'))
		else:
			data = []
		return HttpResponse(data, content_type='application/json')

class BusquedaMesas(TemplateView):

	def get(self, request, *args, **kwargs):
		distrito = request.GET['distrito']
		centro_votacion = CentroVotacion.objects.filter(distrito=distrito)
		mesas = Mesa.objects.filter(centro_votacion=centro_votacion,procesada=False)
		if mesas:
			data = serializers.serialize('json', mesas, fields= ('numero'))
		else:
			data = []
		return HttpResponse(data, content_type='application/json')

def actas(request):
    actas = Acta.objects.all()
    context = {'actas':actas}
    return render(request, 'actas/actas.html', context)

class Mesas(ListView):
    model = Mesa
    template_name = "actas/mesas.html"
    context_object_name = "mesas"

def detalle_acta(request,acta):
	obj_acta = Acta.objects.get(pk=acta)
	detalles = DetalleActa.objects.filter(acta=acta)
	context = {'acta':obj_acta, 'detalles':detalles}
	return render(request, 'actas/detalle_acta.html', context)

def exportar_actas(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="actas.csv"'

	writer = csv.writer(response)
	writer.writerow(['MESA', 'VOTOS REGIONALES', 'VOTOS PROVINCIALES', 'VOTOS DISTRITALES'])
	actas = Acta.objects.all()
	for acta in actas:
		writer.writerow([acta.mesa, acta.votos_emitidos_reg,acta.votos_emitidos_prov, acta.votos_emitidos_dis])
	return response

def exportar_mesas(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="mesas.csv"'

	writer = csv.writer(response)
	writer.writerow(['MESA', 'CENTRO VOTACION', 'DISTRITO', 'NRO ELECTORES', 'PROCESAMIENTO'])
	mesas = Mesa.objects.all()
	for mesa in mesas:
		if mesa.procesada:
			procesada = "MESA PROCESADA"
		else:
			procesada = "MESA SIN PROCESAR"
		writer.writerow([mesa.numero, mesa.centro_votacion,mesa.centro_votacion.distrito, mesa.total_electores,procesada])
	return response

def seleccion_distrito(request):
	regiones = Region.objects.order_by('nombre')
	if request.method == 'POST':
		distrito = request.POST['distritos']
		return HttpResponseRedirect(reverse('actas:reporte_distrital', args=[distrito]))
	context = {'regiones':regiones}
	return render(request, 'actas/seleccion_distrito.html', context)

def seleccion_provincia(request):
	regiones = Region.objects.order_by('nombre')
	if request.method == 'POST':
		provincia = request.POST['provincias']
		return HttpResponseRedirect(reverse('actas:reporte_provincial', args=[provincia]))
	context = {'regiones':regiones}
	return render(request, 'actas/seleccion_provincia.html', context)

def seleccion_region(request):
	regiones = Region.objects.order_by('nombre')
	if request.method == 'POST':
		region = request.POST['regiones']
		return HttpResponseRedirect(reverse('actas:reporte_regional', args=[region]))
	context = {'regiones':regiones}
	return render(request, 'actas/seleccion_region.html', context)

def reporte_regional(request, region):
	votos_partidos = VotacionRegional.objects.filter(region=region)
	context = {'votos_partidos':votos_partidos, 'region':region}
	return render(request, 'actas/reporte_regional.html', context)

def reporte_provincial(request, provincia):
	votos_partidos = VotacionProvincial.objects.filter(provincia=provincia)
	context = {'votos_partidos':votos_partidos,'provincia':provincia}
	return render(request, 'actas/reporte_provincial.html', context)

def reporte_distrital(request, distrito):
	distrito_obj = Distrito.objects.get(pk=distrito)
	votos_partidos = VotacionDistrital.objects.filter(distrito=distrito_obj)
	context = {'votos_partidos':votos_partidos,'distrito':distrito}
	return render(request, 'actas/reporte_distrital.html', context)
			
def exportar_reporte_regional(request, region):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-regional.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'REGION', 'VOTACION'])
	votos_partidos = VotacionRegional.objects.filter(region=region)
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.region, votos_partido.votos])
	return response

def exportar_reporte_provincial(request, provincia):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-provincial.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'PROVINCIA', 'VOTACION'])
	votos_partidos = VotacionProvincial.objects.filter(provincia=provincia)
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.provincia, votos_partido.votos])
	return response

def exportar_reporte_distrital(request, distrito):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-distrital.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'DISTRITO', 'VOTACION'])
	votos_partidos = VotacionDistrital.objects.filter(distrito=distrito)
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.distrito, votos_partido.votos])
	return response