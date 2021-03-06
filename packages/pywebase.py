# -*- coding: utf-8 -*-
#
#   pywebase core
#

# TODO HTTPS support?

import logging
import settings

from packages import bottle
from packages import pyservice

# monkey patching for BaseHTTPRequestHandler.log_message
def log_message(obj, format, *args):
    logging.info("%s %s" % (obj.address_string(), format%args))

# -----------------------------------------------
# Process to run
# -----------------------------------------------

class PywebaseProcess(pyservice.Process):

    pidfile = settings.PYWEBASE_PIDFILE
    logfile = settings.PYWEBASE_LOGFILE

    def __init__(self):
        super(PywebaseProcess, self).__init__()
        
        from BaseHTTPServer import BaseHTTPRequestHandler
        BaseHTTPRequestHandler.log_message = log_message
            
    def run(self):
        logging.info('pywebase/bootle-{} server starting up'.format(bottle.__version__))
        bottle.TEMPLATE_PATH.append(settings.TEMPLATE_PATH)
        bottle.run(host='localhost', port=8080, debug=settings.DEBUG_MODE)

# TODO reloader – Start auto-reloading bottle.py server? (default: False)
# TODO interval – Bottle.py auto-reloader interval in seconds (default: 1)

# -----------------------------------------------
# utils
# -----------------------------------------------
def add_routes(*routes):
    ''' add static/dynamic routes for bottle process'''
    for url, method, handler in routes:
        bottle.route(url, method, handler)

# -----------------------------------------------
# Request handlers
# -----------------------------------------------

# TODO add authentication

# favicon.ico handling
def handle_favicon():
    return bottle.static_file('images/favicon.ico', root=settings.STATIC_PATH)

# static files handling
def handle_static(filepath):
    return bottle.static_file(filepath, root=settings.STATIC_PATH)
    
# main/index page
def handle_index():
    return bottle.template('index', dict(name='pywebase'))

# login form
# TODO https://github.com/bbrodriges/bottlepy-user-auth/blob/master/bottlepy_user_auth.py
# TODO https://github.com/linsomniac/bottlesession
def handle_login():
    return 
    
# logout
# TODO https://github.com/bbrodriges/bottlepy-user-auth/blob/master/bottlepy_user_auth.py
# TODO https://github.com/linsomniac/bottlesession
def handle_logout():
    return     
    
    
    
