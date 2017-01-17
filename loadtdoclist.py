'''\
This program reads 3GPP Tdoclist into a database defined by tdocsonline.models, which will be used
by 3gppdocsonline.com to display the Tdoclist. \
The functions for reading Excel workbook is provided by 'xlrd' package. Please install xlrd package
before running this program: \
$ pip install xlrd \
Note that xlrd doesn't support .xlsm, so please save the 3GPP Tdoclist (.xlsm) as (.xls) file
first.\
'''

import django
import os.path

django.setup()

import xlrd
from django.conf import settings
from tdocsonline.models import *

TDOCLIST_ROOT = '/home/tawayee/3gpp-docs/'

meeting = input('Please enter the 3GPP meeting number: ')
working_group = meeting.split('-')[0]
meeting_no = meeting.split('-')[1]
print('The Working Group is: ', working_group)
print('The meeting number is: ', meeting_no)

tdlist_file = TDOCLIST_ROOT + working_group + '/' + meeting + '/' + meeting + '.xls'
print(tdlist_file)

if os.path.exists(tdlist_file):
	wb = xlrd.open_workbook(tdlist_file)
	sheet = wb.sheet_by_index(0)

	num_rows = sheet.nrows
	numcols = sheet.ncols

	row = 1
	while row < num_rows:
		tdoc = TDOCLIST_TABLES[meeting](
			tdoc_number = sheet.row_values(row)[0],
			tdoc_title = sheet.row_values(row)[1],
			tdoc_source = sheet.row_values(row)[2],
			tdoc_type = sheet.row_values(row)[5],
			tdoc_agendaitem = sheet.row_values(row)[11],
			tdoc_ai_description = sheet.row_values(row)[12],
			tdoc_status = sheet.row_values(row)[14],
			tdoc_revision_of = sheet.row_values(row)[17],
			tdoc_revised_to = sheet.row_values(row)[18],
			tdoc_release = sheet.row_values(row)[19],
			tdoc_workitem = sheet.row_values(row)[22],
		)
		tdoc.save()
		row = row + 1

	print('The Tdoclist for ' + meeting + ' is loaded into the database.\n')

else:
	print('The Tdoclist for ' + meeting + ' is not found.\n')


for tdoc in TDOCLIST_TABLES[meeting].objects.all():
	print(tdoc.tdoc_number + ' ' + tdoc.tdoc_title + '\n')
