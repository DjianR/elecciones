from django.conf.urls import patterns, url
from actas.views import mesa, BusquedaProvincias, BusquedaDistritos, BusquedaMesas
from actas.views import acta, actas, detalle_acta, mesas, exportar_actas, exportar_mesas,exportar_reporte_regional,exportar_reporte_provincial,exportar_reporte_distrital,reporte_regional
from actas.views import reporte_provincial, reporte_distrital, seleccion_distrito, seleccion_provincia, seleccion_region
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^$',login_required(mesa), name="mesa"),
	url(r'^actas/busquedaProvincias/$',login_required(BusquedaProvincias.as_view()), name="busquedaProvincias"),
	url(r'^actas/busquedaDistritos/$',login_required(BusquedaDistritos.as_view()), name="busquedaDistritos"),
	url(r'^actas/busquedaMesas/$',login_required(BusquedaMesas.as_view()), name="busquedaMesas"),
	url(r'^actas/acta/(?P<numero>\d+)/$',login_required(acta), name="acta"),
	url(r'^actas/actas/$',login_required(actas), name="actas"),
	url(r'^actas/mesas/$',login_required(mesas), name="mesas"),
	url(r'^actas/detalle_acta/(?P<acta>\d+)/$',login_required(detalle_acta), name="detalle_acta"),	
	url(r'^actas/exportar_actas/$',login_required(exportar_actas), name="exportar_actas"),
	url(r'^actas/exportar_mesas/$',login_required(exportar_mesas), name="exportar_mesas"),
	url(r'^actas/exportar_reporte_regional/(?P<region>\d+)/$',login_required(exportar_reporte_regional), name="exportar_reporte_regional"),
	url(r'^actas/exportar_reporte_provincial/(?P<provincia>\d+)/$',login_required(exportar_reporte_provincial), name="exportar_reporte_provincial"),
	url(r'^actas/exportar_reporte_distrital/(?P<distrito>\d+)/$',login_required(exportar_reporte_distrital), name="exportar_reporte_distrital"),
	url(r'^actas/reporte_regional/(?P<region>\d+)/$',login_required(reporte_regional), name="reporte_regional"),
	url(r'^actas/reporte_provincial/(?P<provincia>\d+)/$',login_required(reporte_provincial), name="reporte_provincial"),
	url(r'^actas/reporte_distrital/(?P<distrito>\d+)/$',login_required(reporte_distrital), name="reporte_distrital"),
	url(r'^actas/seleccion_distrito/$',login_required(seleccion_distrito), name="seleccion_distrito"),
	url(r'^actas/seleccion_provincia/$',login_required(seleccion_provincia), name="seleccion_provincia"),
	url(r'^actas/seleccion_region/$',login_required(seleccion_region), name="seleccion_region"),
)