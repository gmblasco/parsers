import os
import pprint
file = open('C:\\Users\\gablasco.CENCOSUD\\Desktop\\calvocsv.csv') #abro archivo a leer
filec = file.readlines()
file.close()
suc=['Sucursal;Proveedor;Monto;Proveedor2;Monto;']
i = len(filec) #uso para iterar el archivo
sm = 'hola'
sm1 = 'NULL'
path=('C:\\Users\\gablasco.CENCOSUD\\Desktop\\')
print('Ingrese el nombre del archivo para guardar el resultado:')
fn = input()
fn = fn+'.csv' #agrego extension
fullpath = path+fn #agrego el path al archivo
newfile = open(fullpath, 'w')#creo el archivo
for j in range(0,i):
    index1 = filec[j].find('Proveedor')
    index2 = filec[j].find('Monto')
    index3 = filec[j].find('Fin')
    sm = filec[j][0:index1]
    prove = filec[j][index1+10:index2]
    monto = filec[j][index2+6:index3]
    if sm != sm1:
        sm1 = sm
        suc=suc+[sm+prove+monto]
    else:
        #index2 = filec[j].find('Monto')
        #index3 = filec[j].find('Fin')
        #prove = filec[j][index1+10:index2]        
        #monto = filec[j][index2+6:index3]
        suclen = len(suc)
        strsuc = suc[suclen-1]
        strsuc = strsuc+prove+monto
        suc[suclen-1] = strsuc
        
for e in range(0,len(suc)):
    line = suc[e]
    line = line + '\n'
    newfile.write(line)
newfile.close()
print('Finalizado con éxito')

        
