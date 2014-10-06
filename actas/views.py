from django.shortcuts import render
from actas.models import Region, Provincia, Distrito, CentroVotacion, Mesa, ActaMunicipal, DetalleActaMunicipal, DisenioActaMunicipal, DetalleDisenioActaMunicipal, VotacionDistrital, VotacionProvincial, VotacionPresidenteRegional, VotacionConsejeroRegional, DisenioActaRegional, DetalleDisenioActaRegional, ActaRegional, DetalleActaRegional
from django.views.generic import TemplateView, ListView, DetailView
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum

# Create your views here.
def mesa_municipal(request):
	mesas = Mesa.objects.filter(procesada_municipal=False)
	if request.method == 'POST':
		mesa = request.POST['mesas']
		try: 
			obj_mesa = Mesa.objects.get(pk=mesa)
			return HttpResponseRedirect(reverse('actas:acta_municipal', args=[mesa]))
		except Mesa.DoesNotExist:
			return HttpResponseRedirect(reverse('actas:mesa_municipal'))
	context = {'mesas':mesas}
	return render(request, 'actas/mesa_municipal.html', context)

def mesa_regional(request):
	mesas = Mesa.objects.filter(procesada_regional=False)
	if request.method == 'POST':
		mesa = request.POST['mesas']
		try: 
			obj_mesa = Mesa.objects.get(pk=mesa)
			return HttpResponseRedirect(reverse('actas:acta_regional', args=[mesa]))
		except Mesa.DoesNotExist:
			return HttpResponseRedirect(reverse('actas:mesa_regional'))
	context = {'mesas':mesas}
	return render(request, 'actas/mesa_regional.html', context)

def acta_regional(request, numero):
	mesa = Mesa.objects.get(numero=numero)
	centro_votacion = mesa.centro_votacion
	distrito = centro_votacion.distrito
	provincia = distrito.provincia
	region = provincia.region
	try:
		disenio_acta = DisenioActaRegional.objects.get(region=region)
	except DisenioActaRegional.DoesNotExist:
		return HttpResponseRedirect(reverse('admin:login'))
	detalles = DetalleDisenioActaRegional.objects.filter(disenio_acta=disenio_acta).order_by('id')
	if request.method == 'POST':
		votos_blancos_pres = request.POST['voto_blanco_pres']
		votos_nulos_pres = request.POST['voto_nulo_pres']
		votos_imp_pres = request.POST['voto_impugnado_pres']
		votos_tot_pres = request.POST['voto_total_pres']
		votos_blancos_cons = request.POST['voto_blanco_cons']
		votos_nulos_cons = request.POST['voto_nulo_cons']
		votos_imp_cons = request.POST['voto_impugnado_cons']
		votos_tot_cons = request.POST['voto_total_cons']
		acta = ActaRegional(mesa=mesa,votos_blancos_pres=votos_blancos_pres,votos_nulos_pres=votos_nulos_pres,
			votos_impugnados_pres=votos_imp_pres,votos_emitidos_pres=votos_tot_pres,votos_blancos_cons=votos_blancos_cons,
			votos_nulos_cons=votos_nulos_cons,votos_impugnados_cons=votos_imp_cons,votos_emitidos_cons=votos_tot_cons)
		acta.save()
		for detalle in detalles:
			pres = "pres_"+str(detalle.partido.pk)
			votos_pres = request.POST[pres]
			cons = "cons_"+str(detalle.partido.pk)
			votos_cons = request.POST[cons]
			
			try:
				detalle_acta = DetalleActaRegional.objects.get(acta=acta,partido=detalle.partido)
			except DetalleActaRegional.DoesNotExist:
				detalle_acta = DetalleActaRegional(acta=acta,partido=detalle.partido)
				detalle_acta.votos_pres = 0
				detalle_acta.votos_cons = 0

			if not votos_pres.isnumeric():
				votos_pres=0
			else:
				try:
					vot_pres = VotacionPresidenteRegional.objects.get(partido=detalle.partido, region=region)
				except VotacionPresidenteRegional.DoesNotExist:
					vot_pres = VotacionPresidenteRegional(partido=detalle.partido, region=region)
				vot_pres.votos = vot_pres.votos + int(votos_pres) - detalle_acta.votos_pres
				vot_pres.save()
				
			if not votos_cons.isnumeric():
				votos_cons=0
			else:
				try:
					vot_cons = VotacionConsejeroRegional.objects.get(partido=detalle.partido, provincia=provincia)
				except VotacionConsejeroRegional.DoesNotExist:
					vot_cons = VotacionConsejeroRegional(partido=detalle.partido, provincia=provincia)
				vot_cons.votos = vot_cons.votos + int(votos_cons) - detalle_acta.votos_cons
				vot_cons.save()			
			
			detalle_acta.votos_pres=votos_pres
			detalle_acta.votos_cons=votos_cons
			detalle_acta.save()
		mesa.procesada_regional=True
		mesa.save()
		return HttpResponseRedirect(reverse('actas:mesa_regional'))

	context = {'distrito':distrito,'provincia':provincia,'region':region,'disenio_acta':disenio_acta,
	'detalles':detalles,'mesa':mesa}
	return render(request, 'actas/acta_regional.html', context)

def acta_municipal(request, numero):
	mesa = Mesa.objects.get(numero=numero)
	centro_votacion = mesa.centro_votacion
	distrito = centro_votacion.distrito
	provincia = distrito.provincia
	region = provincia.region
	try:
		disenio_acta = DisenioActaMunicipal.objects.get(distrito=distrito)
	except DisenioActaMunicipal.DoesNotExist:
		return HttpResponseRedirect(reverse('admin:login'))
	detalles = DetalleDisenioActaMunicipal.objects.filter(disenio_acta=disenio_acta).order_by('id')
	
	if request.method == 'POST':
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

		acta = ActaMunicipal(mesa=mesa,votos_blancos_prov=votos_blancos_prov,votos_blancos_dis=votos_blancos_dis,
			votos_nulos_prov=votos_nulos_prov,votos_nulos_dis=votos_nulos_dis,
			votos_impugnados_prov=votos_imp_prov,votos_impugnados_dis=votos_imp_dis,
			votos_emitidos_prov=votos_tot_prov,votos_emitidos_dis=votos_tot_dis)
		acta.save()
		for detalle in detalles:
			prov = "prov_"+str(detalle.partido.pk)
			votos_provincial = request.POST[prov]
			dis = "dis_"+str(detalle.partido.pk)
			votos_distrital = request.POST[dis]
			
			try:
				detalle_acta = DetalleActaMunicipal.objects.get(acta=acta,partido=detalle.partido)
			except DetalleActaMunicipal.DoesNotExist:
				detalle_acta = DetalleActaMunicipal(acta=acta,partido=detalle.partido)
				detalle_acta.votos_provincial = 0
				detalle_acta.votos_distrital = 0

			if not votos_provincial.isnumeric():
				votos_provincial=0
			else:
				try:
					vot_prov = VotacionProvincial.objects.get(partido=detalle.partido, provincia=provincia)
				except VotacionProvincial.DoesNotExist:
					vot_prov = VotacionProvincial(partido=detalle.partido, provincia=provincia)
				vot_prov.votos = vot_prov.votos + int(votos_provincial) - detalle_acta.votos_provincial
				vot_prov.save()
				
			if not votos_distrital.isnumeric():
				votos_distrital=0
			else:
				try:
					vot_dis = VotacionDistrital.objects.get(partido=detalle.partido, distrito=distrito)
				except VotacionDistrital.DoesNotExist:
					vot_dis = VotacionDistrital(partido=detalle.partido, distrito=distrito)
				vot_dis.votos = vot_dis.votos + int(votos_distrital) - detalle_acta.votos_distrital
				vot_dis.save()
			
			
			detalle_acta.votos_provincial=votos_provincial
			detalle_acta.votos_distrital=votos_distrital
			detalle_acta.save()
		mesa.procesada_municipal=True
		mesa.save()
		return HttpResponseRedirect(reverse('actas:mesa_municipal'))

	context = {'distrito':distrito,'provincia':provincia,'region':region,'disenio_acta':disenio_acta,
	'detalles':detalles,'mesa':mesa}
	return render(request, 'actas/acta_municipal.html', context)

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

def actas_municipales(request):
    actas = ActaMunicipal.objects.all()
    paginador = Paginator(actas, 10) 
    pagina = request.GET.get('pagina')
    try:
    	actas = paginador.page(pagina)
    except PageNotAnInteger:      
        actas = paginador.page(1)
    except EmptyPage:      
        actas = paginador.page(paginador.num_pages)       
    context = {'actas':actas}
    return render(request, 'actas/actas_municipales.html', context)

def actas_regionales(request):
    actas = ActaRegional.objects.all()
    paginador = Paginator(actas, 10) 
    pagina = request.GET.get('pagina')
    try:
    	actas = paginador.page(pagina)
    except PageNotAnInteger:      
        actas = paginador.page(1)
    except EmptyPage:      
        actas = paginador.page(paginador.num_pages)       
    context = {'actas':actas}
    return render(request, 'actas/actas_regionales.html', context)

def mesas(request):
    mesas = Mesa.objects.all().order_by('centro_votacion','numero')
    paginador = Paginator(mesas, 10) 
    pagina = request.GET.get('pagina')
    try:
    	mesas = paginador.page(pagina)
    except PageNotAnInteger:      
        mesas = paginador.page(1)
    except EmptyPage:      
        mesas = paginador.page(paginador.num_pages)       
    context = {'mesas':mesas}
    return render(request, 'actas/mesas.html', context)

def detalle_acta_municipal(request,acta):
	obj_acta = ActaMunicipal.objects.get(pk=acta)
	detalles = DetalleActaMunicipal.objects.filter(acta=acta)
	context = {'acta':obj_acta, 'detalles':detalles}
	return render(request, 'actas/detalle_acta_municipal.html', context)

def detalle_acta_regional(request,acta):
	obj_acta = ActaRegional.objects.get(pk=acta)
	detalles = DetalleActaRegional.objects.filter(acta=acta)
	context = {'acta':obj_acta, 'detalles':detalles}
	return render(request, 'actas/detalle_acta_regional.html', context)

def exportar_actas_municipales(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="actas_municipales.csv"'

	writer = csv.writer(response)
	writer.writerow(['MESA', 'VOTOS REGIONALES', 'VOTOS PROVINCIALES', 'VOTOS DISTRITALES'])
	actas = ActaMunicipal.objects.all()
	for acta in actas:
		writer.writerow([ActaMunicipal.mesa, ActaMunicipal.votos_emitidos_reg,ActaMunicipal.votos_emitidos_prov, ActaMunicipal.votos_emitidos_dis])
	return response

def exportar_mesas(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="mesas.csv"'

	writer = csv.writer(response)
	writer.writerow(['MESA', 'CENTRO VOTACION', 'DISTRITO', 'NRO ELECTORES', 'PROCESAMIENTO'])
	mesas = Mesa.objects.all()
	for mesa in mesas:
		if mesa.procesada_municipal:
			procesada = "MESA PROCESADA MUNICIPAL"
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

def seleccion_prov_consejero(request):
	regiones = Region.objects.order_by('nombre')
	if request.method == 'POST':
		provincia = request.POST['provincias']
		return HttpResponseRedirect(reverse('actas:reporte_consejero_regional', args=[provincia]))
	context = {'regiones':regiones}
	return render(request, 'actas/seleccion_consejero_prov.html', context)

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
		return HttpResponseRedirect(reverse('actas:reporte_presidente_regional', args=[region]))
	context = {'regiones':regiones}
	return render(request, 'actas/seleccion_region.html', context)

def reporte_presidente_regional(request, region):
	total_vb = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=Provincia.objects.filter(region=region))))).aggregate(Sum('votos_blancos_pres'))
	total_vn = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=Provincia.objects.filter(region=region))))).aggregate(Sum('votos_nulos_pres'))
	total_vi = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=Provincia.objects.filter(region=region))))).aggregate(Sum('votos_impugnados_pres'))
	total_vv = VotacionConsejeroRegional.objects.filter(provincia=Provincia.objects.filter(region=region)).aggregate(Sum('votos'))
	total_votos = total_vv['votos__sum']+total_vb['votos_blancos_pres__sum']+total_vn['votos_nulos_pres__sum']+total_vi['votos_impugnados_pres__sum']
	votos_partidos = VotacionPresidenteRegional.objects.filter(region=region).order_by('-votos')
	context = {'votos_partidos':votos_partidos, 'region':region,'total_votos':total_votos,'total_vb':total_vb,'total_vn':total_vn,'total_vi':total_vi}
	return render(request, 'actas/reporte_presidente_regional.html', context)

def reporte_consejero_regional(request, provincia):
	total_vb = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_blancos_cons'))
	total_vn = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_nulos_cons'))
	total_vi = ActaRegional.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_impugnados_cons'))
	total_vv = VotacionConsejeroRegional.objects.filter(provincia=provincia).aggregate(Sum('votos'))
	total_votos = total_vv['votos__sum']+total_vb['votos_blancos_cons__sum']+total_vn['votos_nulos_cons__sum']+total_vi['votos_impugnados_cons__sum']
	votos_partidos = VotacionConsejeroRegional.objects.filter(provincia=provincia).order_by('-votos')

	context = {'votos_partidos':votos_partidos, 'provincia':provincia,'total_votos':total_votos,'total_vb':total_vb,'total_vn':total_vn,'total_vi':total_vi}
	return render(request, 'actas/reporte_consejero_regional.html', context)

def reporte_provincial(request, provincia):
	total_vb = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_blancos_prov'))
	total_vn = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_nulos_prov'))
	total_vi = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=Distrito.objects.filter(provincia=provincia)))).aggregate(Sum('votos_impugnados_prov'))
	total_vv = VotacionProvincial.objects.filter(provincia=provincia).aggregate(Sum('votos'))
	total_votos = total_vv['votos__sum']+total_vb['votos_blancos_prov__sum']+total_vn['votos_nulos_prov__sum']+total_vi['votos_impugnados_prov__sum']
	votos_partidos = VotacionProvincial.objects.filter(provincia=provincia).order_by('-votos')
	context = {'votos_partidos':votos_partidos,'provincia':provincia,'total_votos':total_votos,'total_vb':total_vb,'total_vn':total_vn,'total_vi':total_vi}
	return render(request, 'actas/reporte_provincial.html', context)

def reporte_distrital(request, distrito):
	distrito_obj = Distrito.objects.get(pk=distrito)
	total_vb = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=distrito))).aggregate(Sum('votos_blancos_dis'))
	total_vn = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=distrito))).aggregate(Sum('votos_nulos_dis'))
	total_vi = ActaMunicipal.objects.filter(mesa=Mesa.objects.filter(centro_votacion=CentroVotacion.objects.filter(distrito=distrito))).aggregate(Sum('votos_impugnados_dis'))
	total_vv = VotacionDistrital.objects.filter(distrito=distrito_obj).aggregate(Sum('votos'))
	total_votos = total_vv['votos__sum']+total_vb['votos_blancos_dis__sum']+total_vn['votos_nulos_dis__sum']+total_vi['votos_impugnados_dis__sum']
	votos_partidos = VotacionDistrital.objects.filter(distrito=distrito_obj).order_by('-votos')
	context = {'votos_partidos':votos_partidos,'distrito':distrito,'total_votos':total_votos,'total_vb':total_vb,'total_vn':total_vn,'total_vi':total_vi}
	return render(request, 'actas/reporte_distrital.html', context)
			
def exportar_reporte_regional(request, region):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-regional.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'REGION', 'VOTACION'])
	votos_partidos = VotacionRegional.objects.filter(region=region).order_by('-votos')
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.region, votos_partido.votos])
	return response

def exportar_reporte_provincial(request, provincia):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-provincial.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'PROVINCIA', 'VOTACION'])
	votos_partidos = VotacionProvincial.objects.filter(provincia=provincia).order_by('-votos')
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.provincia, votos_partido.votos])
	return response

def exportar_reporte_distrital(request, distrito):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="reporte-distrital.csv"'

	writer = csv.writer(response)
	writer.writerow(['PARTIDO', 'DISTRITO', 'VOTACION'])
	votos_partidos = VotacionDistrital.objects.filter(distrito=distrito).order_by('-votos')
	for votos_partido in votos_partidos:
		writer.writerow([votos_partido.partido, votos_partido.distrito, votos_partido.votos])
	return response