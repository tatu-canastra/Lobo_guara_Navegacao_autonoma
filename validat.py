# -*- coding: utf-8 -*-
import os
import time
import config as config
from openpyxl import load_workbook
files= os.listdir(config.downloadPatch)

arq = open("validacao "+str(time.time())+".csv", "w")
arq.write("id,status,familia,genero,especie\n")

def logTxt(idPlan,status,familia,genero,especie):
	arq.write(idPlan+','+status+','+familia+','+genero+','+especie+"\n")
	pass


def Validate(familia,genero,especie,filename):
	if familia==filename[1] and genero==filename[2] and especie==filename[3]:
		statusLog='ok'
		print(filename[0]+ ' ok')
	else:
		statusLog='erro'
		print (filename[0]+ ' erro ') 
	###########

	if familia== filename[1]:
		familiaLog='ok'
		print(filename[0]+ 'familia ok')
	else:
		familiaLog=familia+'=='+filename[1]
		print (filename[0]+ 'familia '+familiaLog+' erro ') 
	###########
		
	if genero==filename[2] :
		generoLog='ok'
		print(filename[0]+ 'genero ok')
	else:
		generoLog=genero+'=='+filename[2]
		print (filename[0]+ 'genero '+generoLog+' erro ')
	###########

	if especie== filename[3]:
		especieLog='ok'
		print(filename[0]+ 'especie ok')
	else:
		especieLog=especie+'=='+filename[3]
		print (filename[0]+ 'especie '+especieLog+' erro ') 
	###########
	logTxt(filename[0],statusLog,familiaLog,generoLog,especieLog)
	print (" ") 
	pass


for file in files:
	if 'xlsx' in file and '-' in file:
		wb = load_workbook(filename = config.downloadPatch+file)
		sheet_ranges = wb[u'Relatório']
		if sheet_ranges['I2'].value is None:
			print('Erro sem dado')
			logTxt(filename[0],'null','null','null','null')
			print(" ")
		else:
			familia=sheet_ranges['I2'].value.replace(' ','').lower()
			genero=sheet_ranges['J2'].value.replace(' ','').lower()
			especie=sheet_ranges['K2'].value.replace(' ','').lower()
			
			filename=file.replace(' ','').lower().split('-')



			Validate(familia,genero,especie,filename)
		

 

print('Finalisado')
arq.close()