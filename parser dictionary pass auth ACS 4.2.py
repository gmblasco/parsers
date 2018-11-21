import os
import pprint
file = open('C:\\Users\\gablasco.CENCOSUD\\Desktop\\ACS\\Passed1.csv') #abro archivo a leer
filec = file.readlines()
file = open('C:\\Users\\gablasco.CENCOSUD\\Desktop\\ACS\\Passed2.csv') #abro archivo a leer
filec = filec+file.readlines()
file = open('C:\\Users\\gablasco.CENCOSUD\\Desktop\\ACS\\Passed3.csv') #abro archivo a leer
filec = filec+file.readlines()
file = open('C:\\Users\\gablasco.CENCOSUD\\Desktop\\ACS\\Passed4.csv') #abro archivo a leer
filec = filec+file.readlines()
i = len(filec) #uso para iterar el archivo
output = {'Username,Group':'Conexiones'} #creo diccionario con sus contenidos para poder contar conexiones
path=('C:\\Users\\gablasco.CENCOSUD\\Desktop\\ACS\\')
print('Ingrese el nombre del archivo para guardar el resultado:')
fn = input()
fn = fn+'.csv' #agrego extension
fullpath = path+fn #agrego el path al archivo
newfile = open(fullpath, 'w')#creo el archivo
for j in range(0,i):
     if 'Wi-Fi' in filec[j]:
         index = filec[j].find('Auth')
         iip = filec[j].find('Wi-Fi')
         if index != -1:
             endi = filec[j].find(',',index+10)
             endj = filec[j].find(',',iip+22)
             username = filec[j][index + 10:endi]
             ip = filec[j][iip + 21:endj]
             username_ip = username +','+ ip
             output.setdefault(username_ip , 0)
             output[username_ip] = output[username_ip] + 1
             j = j+1
                          
     else:
         j = j+1
for e in output.keys():
	line1 = str(e)
	line2 = ','
	line3 = str(output[e])
	line4 = '\n'
	line = line1+line2+line3+line4
	newfile.write(line)
newfile.close()
print('Finalizado con éxito')
#pprint.pprint(output)
