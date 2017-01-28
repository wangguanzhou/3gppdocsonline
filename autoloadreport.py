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
import xlrd

FTP_ROOT_SA2 = '/tsg_sa/WG2_Arch'

report_file_list = [
	{'workgroup': 'SA2',
	 'meetingno': '118',
	 'bis': 'bis',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_118BIS_Spokane/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '118',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_118_Reno/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '117',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_117_Kaohsiung_City/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '116',
	 'bis': 'bis',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_116BIS_Sanya/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '116',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_116_Vienna/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '115',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_115_Nanjing_China/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '114',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_114_Sophia_Antipolis/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '113',
	 'bis': 'AH',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_113AH_Sophia_Antipolis/Report/',
	 'ftp-file': '',
	 },
	{'workgroup': 'SA2',
	 'meetingno': '113',
	 'bis': '',
	 'ftp-path': FTP_ROOT_SA2 + '/TSGS2_113_St_Kitts/Report/',
	 'ftp-file': '',
	 },

]
	
DOC_ROOT = '/var/www/xgppdocsonline.com/reports/'

def unzip_report(workgroup, meetingno, bis):
	report_zip = workgroup + '-' + meetingno + bis + '-report.zip'
	if not os.path.exists(report_zip):
		print('The zip file ' + report_zip + ' does not exist. \n')
		return
	else:
		if not os.path.exists('./tmp'):
			os.makedirs('./tmp')
		with ZipFile(report_zip) as zf:
			zf.extractall('./tmp')
			zf.close()
		for fname in os.listdir('./tmp'):
			if os.path.isdir(fname):
				pass
			elif meetingno in fname:
				srcfile = './tmp/' + fname
				ext = os.path.splitext(fname)[1] 
				destfile = './' + workgroup + '-' + meetingno + bis + '-report' + ext
				shutil.move(srcfile, destfile)
				print(destfile + ' has been successfully unzipped.\n')
			else:
				print(workgroup + '-' + meetingno + ' report file is not found in ' + report_zip + '\n')
		
		shutil.rmtree('./tmp', ignore_errors=True)

ftp = FTP('ftp.3gpp.org')
ftp.login()

print('ftp.3gpp.org logged in')

current_dir = os.getcwd()
os.chdir(DOC_ROOT)

for report in report_file_list:
	ftp.cwd(report['ftp-path'])
	for rf in ftp.nlst():
		if ('Rep' in rf or report['meetingno'] in rf) and not 'rm' in rf:
			print('The report file for the meeting has been found: ' + rf) 
			report['ftp-file'] = rf
	if report['ftp-file'] == '':
		print('The report file for the meeting has NOT been found: ') 
	else:
		report_file_name = report['workgroup'] + '-' + report['meetingno'] + report['bis'] + '-report.zip'
		ff = open(report_file_name, 'wb')
		ftp.retrbinary('RETR ' + report['ftp-file'], ff.write)	
		ff.close()
		print(report_file_name + ' has been downloaded.\n')
		unzip_report(report['workgroup'], report['meetingno'], report['bis'])

os.chdir(current_dir)



