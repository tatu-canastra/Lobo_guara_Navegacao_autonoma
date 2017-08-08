
import os
import time
dirdownload='C:\\Users\\savanizacao\\Downloads\\'
name='RelatorioConsultaTestemunho.xlsx'

baixados=[]
for file in files:
	if 'xlsx' in file and '-' in file:
		baixados.append(file.split('-')[0])
	pass
print(baixados)