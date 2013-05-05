# Create your views here.

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template import RequestContext

import session_manager
import gnucash


def index(request):
    s = session_manager.get_session()
    root_account = s.book.get_root_account()
    accounts = root_account.get_children()
    account_names = []
    for a in accounts:
        account_names.append(gnucash.gnucash_core_c.xaccAccountGetName(a))
    parameters = {'account_names': account_names}
    session_manager.close_session()
    return render_to_response('index.html', parameters)

