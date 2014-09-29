from django.db import models

# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=80)
   
    def __str__(self):
        return self.nombre
    

class Provincia(models.Model):
    nombre = models.CharField(max_length=80)
    region = models.ForeignKey(Region)
    
    def __str__(self):
        return self.nombre
    

class Distrito(models.Model):
    nombre = models.CharField(max_length=80)
    provincia = models.ForeignKey(Provincia)
    capital_provincia = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    

class Partido(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class VotacionRegional(models.Model):
    partido = models.ForeignKey(Partido)
    region = models.ForeignKey(Region)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        pass

class VotacionProvincial(models.Model):
    partido = models.ForeignKey(Partido)
    provincia = models.ForeignKey(Provincia)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
        pass

class VotacionDistrital(models.Model):
    partido = models.ForeignKey(Partido)
    distrito = models.ForeignKey(Distrito)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.partido, self.distrito)
    

class CentroVotacion(models.Model):
    nombre = models.CharField(max_length=50)
    distrito = models.ForeignKey(Distrito)

    def __str__(self):
        return "%s - %s" % (self.nombre, self.distrito)

class Mesa(models.Model):
    numero = models.CharField(max_length=6, primary_key=True)
    total_electores = models.IntegerField()
    centro_votacion = models.ForeignKey(CentroVotacion)
    procesada = models.BooleanField(default=False)

    def __str__(self):
        return self.numero
    
class Acta(models.Model):
    mesa = models.ForeignKey(Mesa)
    votos_blancos_reg = models.IntegerField()
    votos_blancos_prov = models.IntegerField()
    votos_blancos_dis = models.IntegerField()
    votos_nulos_reg = models.IntegerField()
    votos_nulos_prov = models.IntegerField()
    votos_nulos_dis = models.IntegerField()
    votos_impugnados_reg = models.IntegerField()
    votos_impugnados_prov = models.IntegerField()
    votos_impugnados_dis = models.IntegerField()
    votos_emitidos_reg = models.IntegerField()
    votos_emitidos_prov = models.IntegerField()
    votos_emitidos_dis = models.IntegerField()

    def __str__(self):
        return self.mesa.numero

class DetalleActa(models.Model):
    acta = models.ForeignKey(Acta)
    partido = models.ForeignKey(Partido)
    votos_regional = models.IntegerField()
    votos_provincial = models.IntegerField()
    votos_distrital = models.IntegerField()

    def __str__(self):
        return self.acta.mesa.numero+" "+self.partido.nombre

class DiseñoActa(models.Model):
	nombre = models.CharField(max_length=50)
	distrito = models.ForeignKey(Distrito)

	def __str__(self):
		return self.nombre

class DetalleDiseñoActa(models.Model):
    diseño_acta = models.ForeignKey(DiseñoActa)
    partido = models.ForeignKey(Partido)
    distrital = models.BooleanField(default=False)
    provincial = models.BooleanField(default=False)
    regional = models.BooleanField(default=False)

    def __str__(self):
        return self.partido.nombre
    