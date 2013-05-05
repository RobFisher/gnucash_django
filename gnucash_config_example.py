"""
Copy this file to gnucash_config.py and edit it.
"""

username='gnucash'
password='8H3V97cXA9gg'
database_host='localhost'
database_name='gnucash'

gnucash_api_path='/usr/local/lib/python2.7/site-packages'

import sys

if not gnucash_api_path in sys.path:
    sys.path.append(gnucash_api_path)

from gnucash import Session

username='gnucash'
password='8H3V97cXA9gg'
uri = 'mysql://' + username + ':' + password + '@' + database_host + '/' + database_name

