from django.shortcuts import render
import os.path
from tdocsonline.models import *
from tdocsonline.forms import *

# Create your views here.

SITE_ROOT = '/var/www/xgppdocsonline.com/'
DOCS_ROOT = 'docs/'
REPORTS_ROOT = 'reports/'

def homepage(request):
	context = {}
	tdoc_filters = {'tdoc_source': 'All',
					'tdoc_agendaitem': 'All',
					'tdoc_workitem': 'All',
					'tdoc_release': 'All',
					'tdoc_type': 'All',
					}

	if request.GET:
		selected_work_group = request.GET['work_group']
		selected_meeting_no = request.GET['meeting_no']

		if 'load_tdoclist' in request.GET:
		# 'Load Tdoclist' button click has triggered this request
			context['tdoc_form'] = set_tdoc_form(selected_work_group, selected_meeting_no)
			context['tdoc_list'] = populate_tdoc_list(selected_work_group, selected_meeting_no, tdoc_filters)

		elif 'filter_tdoclist' in request.GET:
		# 'Filter Tdocs' button click has triggered this request
			context['tdoc_form'] = set_tdoc_form(selected_work_group, selected_meeting_no)
			tdoc_filters['tdoc_source'] = request.GET['tdoc_source']
			tdoc_filters['tdoc_agendaitem'] = request.GET['tdoc_agenda_item']
			tdoc_filters['tdoc_workitem'] = request.GET['tdoc_workitem']
			tdoc_filters['tdoc_release'] = request.GET['tdoc_release']
			tdoc_filters['tdoc_type'] = request.GET['tdoc_type']
			context['tdoc_list'] = populate_tdoc_list(selected_work_group, selected_meeting_no, tdoc_filters)
			
		else:
		# change of 'work_group' dropdown selection has triggered this request.
			context['tdoc_form'] = set_tdoc_form(selected_work_group, '')
			return render(request, 'index.html', context)
		
		return render(request, 'showtdocs.html', context)
	else:
		context['tdoc_form'] = set_tdoc_form('', '')
		return render(request, 'index.html', context)

	
def showreports(request):
	context = {}
	if request.GET:
		selected_work_group = request.GET['work_group']
		context['tdoc_form'] = set_tdoc_form(selected_work_group, '')
		context['report_list'] = populate_report_list(selected_work_group)

	else:
		context['tdoc_form'] = set_tdoc_form('', '')

	return render(request, 'showreports.html', context)	


def set_tdoc_form(selected_work_group, selected_meeting_no):
	tdoc_form = TdocFilterForm()
	
	tdoc_form.fields['work_group'].choices = WORKGROUP_CHOICES
	if selected_work_group != '':
		tdoc_form.fields['work_group'].initial = selected_work_group
		tdoc_form.fields['meeting_no'].choices = XGPP_MEETING_LIST[selected_work_group]
		tdoc_form.fields['meeting_no'].initial = XGPP_MEETING_LIST[selected_work_group][0][0]
	else:
		default_wg = WORKGROUP_CHOICES[0][0]
		tdoc_form.fields['work_group'].initial = default_wg
		tdoc_form.fields['meeting_no'].choices = XGPP_MEETING_LIST[default_wg]
		tdoc_form.fields['meeting_no'].initial = XGPP_MEETING_LIST[default_wg][0][0]
		
	if selected_meeting_no != '':
		tdoc_form.fields['meeting_no'].initial = selected_meeting_no
		tdoc_source_choices = populate_source_choices(selected_work_group, selected_meeting_no)
		tdoc_form.fields['tdoc_source'].choices = tdoc_source_choices 
		tdoc_form.fields['tdoc_source'].initial = tdoc_source_choices[0][0] 
			
		tdoc_agendaitem_choices = populate_agendaitem_choices(selected_work_group, selected_meeting_no)
		tdoc_form.fields['tdoc_agenda_item'].choices = tdoc_agendaitem_choices
		tdoc_form.fields['tdoc_agenda_item'].initial = tdoc_agendaitem_choices[0][0]

		tdoc_workitem_choices = populate_workitem_choices(selected_work_group, selected_meeting_no)
		tdoc_form.fields['tdoc_workitem'].choices = tdoc_workitem_choices
		tdoc_form.fields['tdoc_workitem'].initial = tdoc_workitem_choices[0][0]

		tdoc_release_choices = populate_release_choices(selected_work_group, selected_meeting_no)
		tdoc_form.fields['tdoc_release'].choices = tdoc_release_choices
		tdoc_form.fields['tdoc_release'].initial = tdoc_release_choices[0][0]

		tdoc_type_choices = populate_type_choices(selected_work_group, selected_meeting_no)
		tdoc_form.fields['tdoc_type'].choices = tdoc_type_choices
		tdoc_form.fields['tdoc_type'].initial = tdoc_type_choices[0][0]

		#nable_tdoc_filters(tdoc_form)

	else:
		tdoc_form.fields['tdoc_source'].choices = (('All', 'Source(All)'),)
		tdoc_form.fields['tdoc_agenda_item'].choices = (('All', 'Agenda Item(All)'),)
		tdoc_form.fields['tdoc_workitem'].choices = (('All', 'Work Item(All)'),)
		tdoc_form.fields['tdoc_release'].choices = (('All', 'Release(All)'),)
		tdoc_form.fields['tdoc_type'].choices = (('All', 'Type(All)'),)
		#disable_tdoc_filters(tdoc_form)	

	return tdoc_form


def set_default_tdoc_form():
	tdoc_form = TdocFilterForm()
	default_wg = WORKGROUP_CHOICES[0][0]
	tdoc_form.fields['work_group'].choices = WORKGROUP_CHOICES
	tdoc_form.fields['work_group'].initial = default_wg
	tdoc_form.fields['meeting_no'].choices = XGPP_MEETING_LIST[default_wg]
	tdoc_form.fields['meeting_no'].initial = XGPP_MEETING_LIST[default_wg][0][0]

	tdoc_form.fields['tdoc_source'].choices = (('All', 'Source(All)'),)
	tdoc_form.fields['tdoc_agenda_item'].choices = (('All', 'Agenda Item(All)'),)
	tdoc_form.fields['tdoc_workitem'].choices = (('All', 'Work Item(All)'),)
	tdoc_form.fields['tdoc_release'].choices = (('All', 'Release(All)'),)
	tdoc_form.fields['tdoc_type'].choices = (('All', 'Type(All)'),)
	disable_tdoc_filters(tdoc_form)	
	return tdoc_form
	

def disable_tdoc_filters(tdoc_form):
	tdoc_form.fields['tdoc_source'].widget.attrs['disabled'] = 'True'
	tdoc_form.fields['tdoc_agenda_item'].widget.attrs['disabled'] = 'True'
	tdoc_form.fields['tdoc_workitem'].widget.attrs['disabled'] = 'True'
	tdoc_form.fields['tdoc_release'].widget.attrs['disabled'] = 'True'
	tdoc_form.fields['tdoc_type'].widget.attrs['disabled'] = 'True'

def enable_tdoc_filters(tdoc_form):
	tdoc_form.fields['tdoc_source'].widget.attrs.pop('disabled', 'none')
	tdoc_form.fields['tdoc_agenda_item'].widget.attrs.pop('disabled', 'none')
	tdoc_form.fields['tdoc_workitem'].widget.attrs.pop('disabled', 'none')
	tdoc_form.fields['tdoc_release'].widget.attrs.pop('disabled', 'none')
	tdoc_form.fields['tdoc_type'].widget.attrs.pop('disabled', 'none')

def populate_report_list(workgroup):
	report_list = []	
	for meeting in MEETING_REPORT_LIST[workgroup]:
		report = {}
		report['name'] = workgroup + '-' + meeting + '-report'
		report_file1 = SITE_ROOT + REPORTS_ROOT + report['name'] + '.docx' 
		report_file2 = SITE_ROOT + REPORTS_ROOT + report['name'] + '.doc' 
		if os.path.exists(report_file1):
			report['exist'] = True
			report['file'] = report_file1[len(SITE_ROOT):]
		elif os.path.exists(report_file2):
			report['exist'] = True
			report['file'] = report_file2[len(SITE_ROOT):]
		else:
			report['exist'] = False
			report['file'] = ''

		report_list.append(report)
	
	return report_list
			
		
def populate_tdoc_list(workgroup, meetingno, tdoc_filters):
	tdoc_list = []
		
	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tdoc_list
	
	else:
		tdoc_path = SITE_ROOT + DOCS_ROOT + workgroup + '/' + target_meeting + '/'
		tdoclist_objects = TDOCLIST_TABLES[target_meeting].objects.all() 
		if tdoc_filters['tdoc_source'] != 'All':
			tdoclist_objects = tdoclist_objects.filter(tdoc_source__icontains=tdoc_filters['tdoc_source'])
		if tdoc_filters['tdoc_agendaitem'] != 'All':
			tdoclist_objects = tdoclist_objects.filter(tdoc_agendaitem=tdoc_filters['tdoc_agendaitem'])
		if tdoc_filters['tdoc_workitem'] != 'All':
			tdoclist_objects = tdoclist_objects.filter(tdoc_workitem__icontains=tdoc_filters['tdoc_workitem'])
		if tdoc_filters['tdoc_release'] != 'All':
			tdoclist_objects = tdoclist_objects.filter(tdoc_release=tdoc_filters['tdoc_release'])
		if tdoc_filters['tdoc_type'] != 'All':
			tdoclist_objects = tdoclist_objects.filter(tdoc_type__icontains=tdoc_filters['tdoc_type'])

		for tdoc in tdoclist_objects:
			tdoc_number = tdoc.tdoc_number
			tdoc_source = tdoc.tdoc_source	
			tdoc_file1 = tdoc_path + tdoc_number +'.doc'
			tdoc_file2 = tdoc_path + tdoc_number +'.docx'
			tdoc_file3 = tdoc_path + tdoc_number +'.pdf'
			tdoc_file4 = tdoc_path + tdoc_number +'.pptx'
			if os.path.exists(tdoc_file1):
				tdoc_exist = True
				tdoc_file = tdoc_file1[len(SITE_ROOT):]
			elif os.path.exists(tdoc_file2):
				tdoc_exist = True
				tdoc_file = tdoc_file2[len(SITE_ROOT):]
			elif os.path.exists(tdoc_file3):
				tdoc_exist = True
				tdoc_file = tdoc_file3[len(SITE_ROOT):]
			elif os.path.exists(tdoc_file4):
				tdoc_exist = True
				tdoc_file = tdoc_file4[len(SITE_ROOT):]
			else:
				tdoc_exist = False
				tdoc_file = ''
			
			this_tdoc = {
				'tdoc_number': tdoc_number,
				'tdoc_source': tdoc_source,
				'tdoc_exist': tdoc_exist,
				'tdoc_file': tdoc_file,
			}		
			tdoc_list.append(this_tdoc)

		return tdoc_list	


def populate_source_choices(workgroup, meetingno):
	source_list = [('All', 'Source(All)')]
	company_list = []

	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tuple(source_list)

	else:
		tdoclist_table = TDOCLIST_TABLES[target_meeting]
		for tdoc in tdoclist_table.objects.all():
			tdoc_src_list = tdoc.tdoc_source.split(',')
			for company in tdoc_src_list:
				if not company.lower().strip() in [x.lower() for x in company_list] \
                   and len(company) > 0 :
					company_list.append(company.strip())

		company_list = sorted(company_list)
		if len(company_list) > 0:
			for company in company_list:
				tdoc_src_tuple = (company, company)  
				source_list.append(tdoc_src_tuple)
		return tuple(source_list)

def populate_agendaitem_choices(workgroup, meetingno):
	agendaitem_list = [('All', 'Agenda Item(All)')]
	temp_list = []
	ai_description_list = {}

	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tuple(agendaitem_list)

	else:
		tdoclist_table = TDOCLIST_TABLES[target_meeting]
		for tdoc in tdoclist_table.objects.all():
			agendaitem = tdoc.tdoc_agendaitem	
			ai_description = tdoc.tdoc_ai_description
			if not agendaitem in temp_list:
				temp_list.append(agendaitem)
				ai_description_list[agendaitem] = ai_description

		temp_list = sorted(temp_list)
		for ai in temp_list:
			ai_tuple = (ai, ai + ' --- ' + ai_description_list[ai])
			agendaitem_list.append(ai_tuple)

		return tuple(agendaitem_list)

def populate_workitem_choices(workgroup, meetingno):
	workitem_list = [('All', 'Work Item(All)')]
	temp_list = []

	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tuple(workitem_list)

	else:
		tdoclist_table = TDOCLIST_TABLES[target_meeting]
		for tdoc in tdoclist_table.objects.all():
			workitem = tdoc.tdoc_workitem	
			if not workitem in temp_list and len(workitem) > 0:
				temp_list.append(workitem)

		temp_list = sorted(temp_list)
		for wi in temp_list:
			wi_tuple = (wi, wi)
			workitem_list.append(wi_tuple)

		return tuple(workitem_list)

def populate_release_choices(workgroup, meetingno):
	release_list = [('All', 'Release(All)')]
	temp_list = []

	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tuple(release_list)

	else:
		tdoclist_table = TDOCLIST_TABLES[target_meeting]
		for tdoc in tdoclist_table.objects.all():
			release = tdoc.tdoc_release	
			if not release in temp_list and len(release) > 0:
				temp_list.append(release)

		temp_list = sorted(temp_list)
		for rel in temp_list:
			rel_tuple = (rel, rel)
			release_list.append(rel_tuple)

		return tuple(release_list)

def populate_type_choices(workgroup, meetingno):
	type_list = [('All', 'Type(All)')]
	temp_list = []

	target_meeting = workgroup + '-' +  meetingno;
	if not target_meeting in TDOCLIST_TABLES:
		return tuple(type_list)

	else:
		tdoclist_table = TDOCLIST_TABLES[target_meeting]
		for tdoc in tdoclist_table.objects.all():
			tdoc_type = tdoc.tdoc_type	
			if not tdoc_type in temp_list and len(tdoc_type) > 0:
				temp_list.append(tdoc_type)

		temp_list = sorted(temp_list)
		for typ  in temp_list:
			typ_tuple = (typ, typ)
			type_list.append(typ_tuple)

		return tuple(type_list)


