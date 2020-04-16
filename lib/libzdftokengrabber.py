# -*- coding: utf-8 -*-
import re
import requests

def grepToken():
	response = requests.get('https://www.zdf.de/')
	tokenMenu = re.compile("apiToken: '(.+?)'", re.DOTALL).findall(response)[0]
	tokenPlayer = re.compile('"apiToken": "(.+?)"', re.DOTALL).findall(response)[0]
	
	libMediathek.f_mkdir(libMediathek.pathUserdata(''))
	libMediathek.f_write(libMediathek.pathUserdata('tokenMenu'), tokenMenu)
	libMediathek.f_write(libMediathek.pathUserdata('tokenPlayer'), tokenPlayer)
	return
	
def grepToken2():
	response = requests.get('http://hbbtv.zdf.de/zdfm3/index.php')
	tokenMenu = re.compile('GLOBALS.apikey = "Bearer (.+?)"', re.DOTALL).findall(response)[0]
	tokenPlayer = re.compile('GLOBALS.apikey = "Bearer (.+?)"', re.DOTALL).findall(response)[0]
	libMediathek.f_mkdir(libMediathek.pathUserdata(''))
	libMediathek.f_write(libMediathek.pathUserdata('tokenMenu'), tokenMenu)
	libMediathek.f_write(libMediathek.pathUserdata('tokenPlayer'), tokenPlayer)
	return