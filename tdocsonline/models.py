from django.db import models

# Create your models here.

class CT1_103_Tdoc(models.Model):
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

class SA2_122_Tdoc(models.Model):
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


class SA2_121_Tdoc(models.Model):
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


class SA2_120_Tdoc(models.Model):
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


class SA2_119_Tdoc(models.Model):
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

class SA2_118_Tdoc(models.Model):
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

class SA2_117_Tdoc(models.Model):
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



class RAN2_AH_NR1_Tdoc(models.Model):
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

class RAN2_97bis_Tdoc(models.Model):
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

class RAN2_97_Tdoc(models.Model):
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



class RAN2_96_Tdoc(models.Model):
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

class RAN2_95bis_Tdoc(models.Model):
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
	'CT1-103': CT1_103_Tdoc,
	'SA2-122': SA2_122_Tdoc,
	'SA2-121': SA2_121_Tdoc,
	'SA2-120': SA2_120_Tdoc,
	'SA2-119': SA2_119_Tdoc,
	'SA2-118bis': SA2_118bis_Tdoc,
	'SA2-118': SA2_118_Tdoc,
	'SA2-117': SA2_117_Tdoc,
	'RAN2-97bis': RAN2_97bis_Tdoc,
	'RAN2-97': RAN2_97_Tdoc,
	'RAN2-AH_NR1': RAN2_AH_NR1_Tdoc,
	'RAN2-96': RAN2_96_Tdoc,
	'RAN2-95bis': RAN2_95bis_Tdoc,
}


