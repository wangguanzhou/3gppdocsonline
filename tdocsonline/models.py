from django.db import models

# Create your models here.

class SA2_118bis_Tdoc(models.Model):
	tdoc_number = models.CharField(max_length=12, primary_key=True)
	tdoc_title = models.CharField(max_length=120)
	tdoc_source = models.CharField(max_length=60)
	tdoc_type = models.CharField(max_length=10)
	tdoc_agendaitem = models.CharField(max_length=10)
	tdoc_ai_description = models.CharField(max_length=40)
	tdoc_status = models.CharField(max_length=10)
	tdoc_revision_of = models.CharField(max_length=10)
	tdoc_revised_to = models.CharField(max_length=10)
	tdoc_release = models.CharField(max_length=10)
	tdoc_workitem = models.CharField(max_length=16)

class RAN2_AD_NR1_Tdoc(models.Model):
	tdoc_number = models.CharField(max_length=12, primary_key=True)
	tdoc_title = models.CharField(max_length=120)
	tdoc_source = models.CharField(max_length=60)
	tdoc_type = models.CharField(max_length=10)
	tdoc_agendaitem = models.CharField(max_length=10)
	tdoc_ai_description = models.CharField(max_length=40)
	tdoc_status = models.CharField(max_length=10)
	tdoc_revision_of = models.CharField(max_length=10)
	tdoc_revised_to = models.CharField(max_length=10)
	tdoc_release = models.CharField(max_length=10)
	tdoc_workitem = models.CharField(max_length=16)


TDOCLIST_TABLES = {
	'SA2-118bis': SA2_118bis_Tdoc,
	'RAN2-AH_NR1': RAN2_AD_NR1_Tdoc,
}


