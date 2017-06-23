'''\
This program does the following automatically:\
1, download tdoclist.xlsm for a meeting;\
2, populate the database of tdocsonline.models\
3, download the tdocs (.zip) from the 3GPP FTP site;\
4, unzip the .zip files\
'''
from ftplib import FTP
from zipfile import ZipFile
import sys
import os, shutil
import django
import xlrd

django.setup()

from django.conf import settings
from tdocsonline.models import *

ftp_paths = {
	'CT1-103': '/tsg_ct/WG1_mm-cc-sm_ex-CN1/TSGC1_103_Spokane/docs/',
	'SA2-122': '/tsg_sa/WG2_Arch/TSGS2_122_Cabo/Docs/',
	'SA2-121': '/tsg_sa/WG2_Arch/TSGS2_121_Hangzhou/Docs/',
	'SA2-120': '/tsg_sa/WG2_Arch/TSGS2_120_Busan/Docs/',
	'SA2-119': '/tsg_sa/WG2_Arch/TSGS2_119_Dubrovnik/Docs/',
	'SA2-118bis': '/tsg_sa/WG2_Arch/TSGS2_118BIS_Spokane/Docs/',
	'SA2-118': '/tsg_sa/WG2_Arch/TSGS2_118_Reno/Docs/',
	'SA2-117': '/tsg_sa/WG2_Arch/TSGS2_117_Kaohsiung_City/Docs/',
	'RAN2-97bis': '/tsg_ran/WG2_RL2/TSGR2_97bis/Docs/',
	'RAN2-97': '/tsg_ran/WG2_RL2/TSGR2_97/Docs/',
	'RAN2-AH_NR1': '/tsg_ran/WG2_RL2/TSGR2_AHs/2017_01_NR/Docs/',
	'RAN2-96': '/tsg_ran/WG2_RL2/TSGR2_96/Docs/',
	'RAN2-95bis': '/tsg_ran/WG2_RL2/TSGR2_95bis/Docs/',
}

DOC_ROOT = '/var/www/xgppdocsonline.com/docs/'

doc_paths = {
	'CT1-103': DOC_ROOT + 'CT1/CT1-103/',
	'SA2-122': DOC_ROOT + 'SA2/SA2-122/',
	'SA2-121': DOC_ROOT + 'SA2/SA2-121/',
	'SA2-120': DOC_ROOT + 'SA2/SA2-120/',
	'SA2-119': DOC_ROOT + 'SA2/SA2-119/',
	'SA2-118bis': DOC_ROOT + 'SA2/SA2-118bis/',
	'SA2-118': DOC_ROOT + 'SA2/SA2-118/',
	'SA2-117': DOC_ROOT + 'SA2/SA2-117/',
	'RAN2-97bis': DOC_ROOT + 'RAN2/RAN2-97bis/',
	'RAN2-97': DOC_ROOT + 'RAN2/RAN2-97/',
	'RAN2-AH_NR1': DOC_ROOT + 'RAN2/RAN2-AH_NR1/',
	'RAN2-96': DOC_ROOT + 'RAN2/RAN2-96/',
	'RAN2-95bis': DOC_ROOT + 'RAN2/RAN2-95bis/',
}

tdoclist_files = {
	'CT1-103': 'TDoc_List_Meeting_CT1#103.xlsm',
	'SA2-122': 'TDoc_List_Meeting_SA2#122.xlsm',
	'SA2-121': 'TDoc_List_Meeting_SA2#121.xlsm',
	'SA2-120': 'TDoc_List_Meeting_SA2#120.xlsm',
	'SA2-119': 'TDoc_List_Meeting_SA2#119.xlsm',
	'SA2-118bis': 'TDoc_List_Meeting_SA2#118-Bis.xlsm',
	'SA2-118': 'TDoc_List_Meeting_SA2#118.xlsm',
	'SA2-117': 'TDoc_List_Meeting_SA2#117.xlsm',
	'RAN2-97bis': 'TDoc_List_Meeting_RAN2#97-Bis.xlsm',
	'RAN2-97': 'TDoc_List_Meeting_RAN2#97.xlsm',
	'RAN2-AH_NR1': 'TDoc_List_Meeting_RAN2-NR#1.xlsm',
	'RAN2-96': 'TDoc_List_Meeting_RAN2#96.xlsm',
	'RAN2-95bis': 'TDoc_List_Meeting_RAN2#95-BIS.xlsm',
}

def unzip_tdoc(tdoc_number):
	tdoc_zip = tdoc_number + '.zip'
	if not os.path.exists(tdoc_zip):
		print('The zip file ' + tdoc_zip + ' does not exist.\n')
		return
	else:
		if not os.path.exists('./tmp'):
			os.makedirs('./tmp')
		try:
			with ZipFile(tdoc_zip, 'r') as zf:
				zf.extractall('./tmp')
				zf.close()
		except:
			print("bad zip file. \n")
		for fname in os.listdir('./tmp'): 
			if os.path.isdir(fname):
				pass
			elif tdoc_number in fname:
				srcfile = './tmp/' + fname
				fileext = os.path.splitext(fname)[1]
				destfile = './' + tdoc_number.upper() + fileext
				shutil.move(srcfile, destfile)
				print(destfile + ' has been successfully unzipped.\n')
			else:
				print(tdoc_number + ' not found in ' + tdoc_zip + '\n')
		os.remove(tdoc_zip)
		shutil.rmtree('./tmp', ignore_errors=True)
	

target_meeting = sys.argv[1]
if not target_meeting in ftp_paths or not target_meeting in doc_paths:
	print('The target meeting is not valid.\n')
	exit()

ftp = FTP('ftp.3gpp.org')
ftp.login()
ftp.cwd(ftp_paths[target_meeting])

current_dir = os.getcwd()
os.chdir(doc_paths[target_meeting])
filename = tdoclist_files[target_meeting]

try:
	ff = open(filename, 'wb')
	ftp.retrbinary('RETR '+filename, ff.write)
	ff.close()
	print(filename + ' has been successfully downloaded.\n')
except:
	print('Unable to download ' + filename + '\n')
	exit()


tdlist_file = doc_paths[target_meeting] + filename

if os.path.exists(tdlist_file):
	wb = xlrd.open_workbook(tdlist_file)
	sheet = wb.sheet_by_index(0)
	
	num_rows = sheet.nrows
	numcols = sheet.ncols

	row = 1
	while row < num_rows:
		tdoc = TDOCLIST_TABLES[target_meeting](
			tdoc_number = sheet.row_values(row)[0],
			tdoc_title = sheet.row_values(row)[1],
			tdoc_source = sheet.row_values(row)[2],
			tdoc_type = sheet.row_values(row)[5],
			tdoc_agendaitem = sheet.row_values(row)[10],
			tdoc_ai_description = sheet.row_values(row)[11],
			tdoc_status = sheet.row_values(row)[13],
			tdoc_revision_of = sheet.row_values(row)[16],
			tdoc_revised_to = sheet.row_values(row)[17],
			tdoc_release = sheet.row_values(row)[18],
			tdoc_workitem = sheet.row_values(row)[21],
		)
		tdoc.save()
		row = row + 1

	print('The Tdoclist for ' + target_meeting + ' is loaded into the database.\n')

else:
	print('The Tdoclist for ' + target_meeting + ' is not found.\n')
	exit()


for tdoc in TDOCLIST_TABLES[target_meeting].objects.all():
	tdoc_file1 = doc_paths[target_meeting] + tdoc.tdoc_number + ".doc"
	tdoc_file2 = doc_paths[target_meeting] + tdoc.tdoc_number + ".docx"
	tdoc_file3 = doc_paths[target_meeting] + tdoc.tdoc_number + ".pdf"

	if os.path.exists(tdoc_file1) or os.path.exists(tdoc_file2) or os.path.exists(tdoc_file3):
		print(tdoc.tdoc_number + ' already exists.')
	else:
		tdoc_zip = tdoc.tdoc_number + '.zip'
		if tdoc_zip in ftp.nlst():
			zipfile = open(tdoc_zip, 'wb')
			ftp.retrbinary('RETR '+tdoc_zip, zipfile.write)
			zipfile.close()
			print(tdoc_zip + ' has been successfully downloaded')
			unzip_tdoc(tdoc.tdoc_number)
		elif tdoc_zip.lower() in ftp.nlst():
			zipfile = open(tdoc_zip.lower(), 'wb')
			ftp.retrbinary('RETR '+tdoc_zip.lower(), zipfile.write)
			zipfile.close()
			print(tdoc_zip + ' has been successfully downloaded')
			unzip_tdoc(tdoc.tdoc_number.lower())

		else:
			print(tdoc_zip + ' is not available in ftp.3gpp.org.\n')

os.chdir(current_dir)

	

