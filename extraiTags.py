#Author: Angelica Ribeiro de Goes
#Script para extração de tags

import urllib3
import lxml.html
import re
from collections import OrderedDict
from lxml import etree
import re

print 'Começando processo de web scraping...\n'
url = 'http://dl.acm.org/citation.cfm?id=2684442&CFID=629363762&CFTOKEN=55148295'
consulta_xpath = "//script[contains(text(), 'boxed')]/text()"
http = urllib3.PoolManager()
response = http.request('GET', url)
document = lxml.html.document_fromstring(response.data) 
resultados = document.xpath(consulta_xpath) 
if len(resultados) > 0:
	for resultado in resultados:
		tags = re.findall(r'<a[^>]*?>(.*?)</a>', resultado)
		if len(tags) > 0:
			for tag in tags:
				print tag
