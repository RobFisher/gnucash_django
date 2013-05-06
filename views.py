# Create your views here.

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template import RequestContext

import session_manager
import gnucash


def append_accounts(accounts, accounts_list):
    for a in accounts:
        accounts_list.append(gnucash.gnucash_core_c.xaccAccountGetName(a))
        children = gnucash.gnucash_core_c.gnc_account_get_children(a)
        if len(children) > 0:
            accounts_list.append('+++')
            append_accounts(children, accounts_list)
            accounts_list.append('---')


def safe_call(function_call, *args):
    """
    Call function with args, closing the session no matter what.
    """
    result = None
    try:
        result = function_call(*args)
        session_manager.close_session()
    except Exception as e:
        session_manager.close_session()
        raise e
    else:
        session_manager.close_session()
        return result


def safe_index(request):
    s = session_manager.get_session()
    root_account = s.book.get_root_account()
    accounts = root_account.get_children()
    accounts_list = []
    append_accounts(accounts, accounts_list)
    parameters = {'accounts_list': accounts_list, 'title': 'Accounts'}
    return render_to_response('index.html', parameters)


def index(request):
    return safe_call(safe_index, request)

