from django.db import models

# Create your models here.


class Ecology(models.Model):
    typeAction: models.CharField(verbose_name='type_action', max_length=50)
    fingerPrint = models.BooleanField(verbose_name='fingerprint', default=False)
    legalObligation = models.BooleanField(verbose_name='legal_obligation', default=False)
    objetive = models.BooleanField(verbose_name='objetives', default=False)
    responsible = models.BooleanField(verbose_name='responsible', default=False)
    nameResponsible = models.CharField(verbose_name='name_responsible', max_length=75)
