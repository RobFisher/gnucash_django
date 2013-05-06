# Create your views here.

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template import RequestContext

import session_manager
import gnucash


def append_accounts(accounts, accounts_list):
    for a in accounts:
        full_name = gnucash.gnucash_core_c.gnc_account_get_full_name(a)
        name = gnucash.gnucash_core_c.xaccAccountGetName(a)
        accounts_list.append((name, full_name))
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


def safe_account(request, full_name):
    s = session_manager.get_session()
    root_account = s.book.get_root_account()
    account = root_account.lookup_by_full_name(full_name)
    parameters = {'full_name': full_name,
                  'name': account.GetName(),
                  'balance': account.GetBalance().to_double()}
    return render_to_response('account.html', parameters)


def account(request, full_name):
    return safe_call(safe_account, request, full_name)