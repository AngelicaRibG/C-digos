#Author: Angelica Ribeiro de Goes
#Script para extração de tags das publicacoes da biblioteca digital ACM

import urllib3
import lxml.html
import re
from collections import OrderedDict
from lxml import etree

#Abre o arquivo com os links das publicacoes
arquivo = open('G:/Projeto_PIBIC/CodigosTeste/links_acm.txt', 'r')
#Realiza a leitura linha a linha do arquivo
arquivo.readline()
for linha in arquivo:
            url = linha.strip()
            http = urllib3.PoolManager()
#Consulta Xpath que extrai as palavras-chave
            consulta_xpath = "//script[contains(text(), 'boxed')]/text()"
            response = http.request('GET', url)
            document = lxml.html.document_fromstring(response.data)
            resultados = document.xpath(consulta_xpath)
            if len(resultados) > 0:
                    tabela_frequencia = {}
                    for resultado in resultados:
                            frase = re.findall(r'<a[^>]*?>(.*?)</a>', resultado)
#Gera histograma e ordena
                            if len(frase) > 0:
                                for palavra in frase:
                                        palavra = re.sub(r"[:.;,!?-]", " ", palavra)
                                        if palavra in tabela_frequencia:
                                                quantidade = tabela_frequencia[palavra]
                                                tabela_frequencia[palavra] = quantidade + 1
                                        else:
                                                tabela_frequencia[palavra] = 1
                    tabela_ordenada = OrderedDict(sorted(tabela_frequencia.items(), key=lambda t: t[1], reverse=True))
#Coloca todas as palavras-chave em maiscula
                    for palavra in tabela_ordenada:
                            print palavra.upper(), ': ', tabela_frequencia[palavra]
                            
  
arquivo.close()
