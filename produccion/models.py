from django.db import models

class ProdLeche(models.Model):
    fecha = models.DateField()
    venta = models.IntegerField()
    consumo = models.IntegerField()
    vo = models.IntegerField()
    temp = models.DecimalField(verbose_name='Temperatura entregada',decimal_places=2,max_digits=4)

    class Meta:
        verbose_name = 'Produccion de Leche'
        verbose_name_plural = 'Produccion de Leche'
        ordering = ('-fecha',)

    def lts_totales(self):
        return self.venta + self.consumo
    lts_total = property(lts_totales)

    def lt_vo(self):
        return self.lts_total/self.vo
    ltsxvo = property(lt_vo)

    

    def __str__(self):
        return str(self.fecha)


class Alimento(models.Model):
    alimento = models.CharField('Alimento', max_length=100,blank=False,null=False)
    ms = models.DecimalField(verbose_name='Materia Seca', default=0.00,max_digits=4,decimal_places=2,null=True,blank=True)
    pt = models.DecimalField(verbose_name='Porcentaje proteico', default=0.00,max_digits=4,decimal_places=2,null=True,blank=True)

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering = ('alimento',)

    def __str__(self):
        return self.alimento


class ExistenciaTambo(models.Model):
    fecha = models.DateField()
    vo = models.IntegerField('VO',default=0)
    vs = models.IntegerField('VS',default=0)
    vaqpp = models.IntegerField('Vaq. PP',default=0)
    # vaqcserv = models.IntegerField('Vaq/Servicio',default=0)
    to = models.IntegerField('Toros',default=0)

    class Meta:
        verbose_name = 'Existencia Tambo'
        verbose_name_plural = 'Existencias de Tambo'
        ordering = ('-fecha',)

    def vt(self):
        return self.vo + self.vs
    vtotal = property(vt)

    def tg(self):
        return self.vtotal + self.vaqpp + self.to
    tg = property(tg)


    def __str__(self):
        return str(self.fecha)


class ExistenciaRecria(models.Model):
    fecha = models.DateField()
    terneros = models.IntegerField('Terneros',default=0)
    recria = models.IntegerField('Recría',default=0)
    vaq = models.IntegerField('Vaquillonas',default=0)
    vaqcserv = models.IntegerField('Vaq/Servicio',default=0)
    nov = models.IntegerField('Novillos',default=0)

    class Meta:
        verbose_name = 'Existencia de Bovinos derivados del tambo'
        verbose_name_plural = 'Existencias de Bovinos derivados del tambo'
        ordering = ('-fecha',)

    def rt(self):
        return self.terneros + self.recria + self.vaq + self.vaqcserv + self.nov
    rt = property(rt)

    def __str__(self):
        return str(self.fecha)
