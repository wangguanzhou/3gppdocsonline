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

from django.conf import settings
from tdocsonline.models import *

TDOCLIST_ROOT = '/home/tawayee/3gpp-docs/tdoclists/'

meeting = input('Please enter the 3GPP meeting number: ')

TDOCLIST_TABLES[meeting].objects.all().delete()

print('The Tdoclist for ' + meeting + ' has been cleared.\n')

