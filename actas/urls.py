from django.conf.urls import patterns, url
from actas.views import mesa_municipal, BusquedaProvincias, BusquedaDistritos, BusquedaMesas, mesa_regional, acta_regional, actas_regionales, detalle_acta_regional, seleccion_prov_consejero, reporte_consejero_regional
from actas.views import acta_municipal, actas_municipales, detalle_acta_municipal, mesas, exportar_actas_municipales, exportar_mesas,exportar_reporte_regional,exportar_reporte_provincial,exportar_reporte_distrital,reporte_presidente_regional
from actas.views import reporte_provincial, reporte_distrital, seleccion_distrito, seleccion_provincia, seleccion_region
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^mesa_municipal/$',login_required(mesa_municipal), name="mesa_municipal"),
	url(r'^mesa_regional/$',login_required(mesa_regional), name="mesa_regional"),
	url(r'^actas/busquedaProvincias/$',login_required(BusquedaProvincias.as_view()), name="busquedaProvincias"),
	url(r'^actas/busquedaDistritos/$',login_required(BusquedaDistritos.as_view()), name="busquedaDistritos"),
	url(r'^actas/busquedaMesas/$',login_required(BusquedaMesas.as_view()), name="busquedaMesas"),
	url(r'^actas/acta_municipal/(?P<numero>\d+)/$',login_required(acta_municipal), name="acta_municipal"),
	url(r'^actas/acta_regional/(?P<numero>\d+)/$',login_required(acta_regional), name="acta_regional"),
	url(r'^actas/actas_municipales/$',login_required(actas_municipales), name="actas_municipales"),
	url(r'^actas/actas_regionales/$',login_required(actas_regionales), name="actas_regionales"),
	url(r'^actas/mesas/$',login_required(mesas), name="mesas"),
	url(r'^actas/detalle_acta_municipal/(?P<acta>\d+)/$',login_required(detalle_acta_municipal), name="detalle_acta_municipal"),
	url(r'^actas/detalle_acta_regional/(?P<acta>\d+)/$',login_required(detalle_acta_regional), name="detalle_acta_regional"),	
	url(r'^actas/exportar_actas_municipales/$',login_required(exportar_actas_municipales), name="exportar_actas_municipales"),
	url(r'^actas/exportar_mesas/$',login_required(exportar_mesas), name="exportar_mesas"),
	url(r'^actas/exportar_reporte_regional/(?P<region>\d+)/$',login_required(exportar_reporte_regional), name="exportar_reporte_regional"),
	url(r'^actas/exportar_reporte_provincial/(?P<provincia>\d+)/$',login_required(exportar_reporte_provincial), name="exportar_reporte_provincial"),
	url(r'^actas/exportar_reporte_distrital/(?P<distrito>\d+)/$',login_required(exportar_reporte_distrital), name="exportar_reporte_distrital"),
	url(r'^actas/reporte_presidente_regional/(?P<region>\d+)/$',login_required(reporte_presidente_regional), name="reporte_presidente_regional"),
	url(r'^actas/reporte_consejero_regional/(?P<provincia>\d+)/$',login_required(reporte_consejero_regional), name="reporte_consejero_regional"),
	url(r'^actas/reporte_provincial/(?P<provincia>\d+)/$',login_required(reporte_provincial), name="reporte_provincial"),
	url(r'^actas/reporte_distrital/(?P<distrito>\d+)/$',login_required(reporte_distrital), name="reporte_distrital"),
	url(r'^actas/seleccion_distrito/$',login_required(seleccion_distrito), name="seleccion_distrito"),
	url(r'^actas/seleccion_prov_consejero/$',login_required(seleccion_prov_consejero), name="seleccion_prov_consejero"),
	url(r'^actas/seleccion_provincia/$',login_required(seleccion_provincia), name="seleccion_provincia"),
	url(r'^actas/seleccion_region/$',login_required(seleccion_region), name="seleccion_region"),
)