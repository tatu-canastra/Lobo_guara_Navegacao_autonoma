# -*- coding: utf-8 -*-
from splinter import Browser
import time
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import csv
import config as config
import os
erroN=0
nTentativa=0
os.system("cls")
#
#Config do Bot
#
browser = Browser('chrome')
browser.driver.set_page_load_timeout(config.timeout)
arq = open("log "+str(time.time())+".csv", "w")
arq.write("name,status\n")
if(config.debug):
	url_base=config.urldebug
	replace='_'
else:
	url_base=config.urlbase
	replace='+'

# Metodo de escrever log
def logTxt(texto,tipo):
	arq.write(texto+','+tipo+"\n")
	pass
def click():
	global erroN
	code=browser.status_code.code
	if(code!=200):
		print('Eroo code '+str(code))
		if erroN<120:
			time.sleep(3)
			erroN=erroN+1
			atividade(name,ordem,urlq)
		else:
			time.sleep(3)
			print('Todas tentativas acabaram '+ordem+' '+name)
			logTxt(ordem+' '+name,'atigiu o numero maximo de tentativa para baixar')
			erroN=0
	else:
		browser.find_by_id('btn-gerarRelatorio').click()	
	pass
#Atividade do bot
def atividade(name,ordem='',urlq=''):
	try:
		print('Tentando baixar dados de '+ordem+' '+name)
		browser.visit(url_base+urlq)
		click()
		pass
	except TimeoutException as e:
		print('Erro ao baixar dados de '+ordem+' '+name)
		logTxt(ordem+' '+name,'error')
		pass	
 	else:
 		print('Foram baixado dados de '+ordem+' '+name)
 		logTxt(ordem+' '+name,'success')
 		rename(config.downloadPatch,config.fileName, name,ordem,urlq)	
 		pass
	pass

def rename(dirdownload,name,newname,ordem='',urlq=''):
	onLoop=True
	i=0
	global nTentativa
	while(onLoop):
		time.sleep(3)
		i=i+1
		print('Carregando ... ')
		if(os.path.isfile(dirdownload+name)==True):
			print('Arquivo achado')
			onLoop=False

		if(i>15):
			onLoop=False
	pass
	if os.path.isfile(dirdownload+name)==True:
		print(ordem+' '+newname+'criando file')
		logTxt(ordem+' '+newname,'Arquivo criado')
		os.rename(dirdownload+name,dirdownload+ordem+'-'+newname+'-'+name)
	else:
		logTxt(dirdownload+name,'Erro no arquivo')
		print(dirdownload+name+' erro arquivo nao pode ser encontrado')
		if nTentativa < 2:
			nTentativa=nTentativa+1
			atividade(name,ordem,urlq)
		else:
			nTentativa=0
	pass
#lista de pesquisa
with open(config.lista) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if int(row['ordem1'])>config.iniciar:
			urlq='&nomeFamilia='+row['familia']+'&genero='+row['genero']+'&especie='+row['especie']
			namePlat=row['familia']+'-'+row['genero']+'-'+row['especie']
			atividade(namePlat,row['ordem1'],urlq)
			#print('trabalho')
		else:
			print('Pular')

print('Finalisado')
arq.close()
browser.quit()