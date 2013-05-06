"""
Manage the GnuCash API Session object. Open it when needed and close it when
finished so that the GnuCash GIU or other API users can access the file or
database.
"""

import gnucash_config
import gnucash


s = None


def get_session():
    global s
    if not s:
        s = gnucash.Session(gnucash_config.uri, is_new=False)
    return s


def close_session():
    global s
    if s:
        s.end()
        s.destroy()
        s = None

