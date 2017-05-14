#!/usr/bin/env python3

import configparser
import os
import time

def absolute_path(file):
	 script = os.path.realpath(__file__)
	 script_path_elements = script.split('/')
	 script_path_elements = script_path_elements [:-1]
	 script_path_elements.append(file)
	 return '/'.join(script_path_elements)

def printer(message):
	print('%s' % message)

if os.path.exists(absolute_path('config.ini')):
	config = configparser.ConfigParser()
	config.read(absolute_path('config.ini'))
else:
	printer('No config.ini exists. Make sure you edit and rename config.ini.default')
	exit(1)

def content_hash(site):
	pass

def hash_match(hash, hash_store):
	pass

def notify(method, recipients, message):
	pass

try:
	hash_store = config.get('Site', 'HashFile')
	site = config.get('Site', 'URL')
	check_time = config.get('Site', 'CheckInterval')
	content_hash = content_hash(site)
	notify_method = config.get('Notifications', 'Method')
	notify_recipients = config.get('Notifications', 'Recipients')
except Exception:
	printer('Required config items not defined. See readme for details')
	exit(1)

update_message = 'Site content has changed. Please check %s' % site


while True:
	if not hash_match(content_hash, hash_store):
		notify(notify_method, notify_recipients, update_message)
	time.sleep (check_time)