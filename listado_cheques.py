#defino librerias 
import csv
import datetime as ti
#constantes y variables 
opciones="""
Bienvenido
__________________________
seleccione una opcion
1.Ingresar datos

2.salir

"""

runTime=True
datetime = ti.date.today()
#funciones
"""Recive el nombre del archivo atraves de un input de usuario y si el archivo existe convierte los datos a valores dentro
de un diccionario donde definimos las claves.
""" 
def readFile(urlfile):
    cheques=[]
    file=open(urlfile+".csv","r")
    csvfile=csv.reader(file)
    for row in csvfile:
        if row != []:
            data = {"Nrocheque":row[0],"codigoBanco":row[1],
            "codigoSucursal":row[2],"ctaOrigen":row[3],"ctaDestino":row[4],
            "valor":row[5],"fechaOrigen":row[6],"fechaPago":row[7],"DNI":row[8],"tipo":row[9],"estado":row[10],}
            cheques.append(data)
    file.close
    return cheques 

"""Funcion hecha para devolver los datos requeridos por el usuario, que son filtrados por el dni y el tipo de cheque
solicitado a traves de un input que son verificados en torno a las claves y valores del diccionario realizado en la funcion anterior"""
def buscarDni(dni, tipo):
    busqueda=[]
    cantidad = 0
    cheques = readFile(urlfile)
    for cheque in cheques:
        if cheque["DNI"]==dni and cheque["tipo"]==tipo:
            cantidad += 1
            print("cheque encontrado\n")
            busqueda.append(cheque)
    repetidos = []
    for i in busqueda:

        repetidos = map(lambda x:x["Nrocheque"], busqueda)
        if i["Nrocheque"] in busqueda:
            repetidos.append(i["Nrocheque"])
    if repetidos !=[]:
        print("Error cheques duplicados")
    else:        
        print(f"se encontraron {cantidad} cheques")
        print(busqueda)


def CSVDES(dni, busqueda):
    file = open(dni+"__"+datetime+"csv","w")
    csvfile=csv.writer(file)
    for row in busqueda:
        csvfile.writerow([row["Nrocheque"],row["codigoBanco"],row[
            "codigoSucursal"],row["ctaOrigen"],row["ctaDestino"],row[
            "valor"],row["fechaOrigen"],row["fechaPago"],row["DNI"],row["tipo"],row["estado"]])
    file.close
    print("csv grabado")

#metodo principal





if __name__=="__main__":
    while runTime:
        print(opciones)
        op = input()
        if op == "1":
            urlfile = input("ingrese el nombre del archivo: \n")
            dni = input("ingrese el DNI del usuario a consultar: \n")
            tipo = input("tipo de cheque a buscar EMITIDO o DEPOSITADO: \n")
            salida = input("desea la salida por pantalla o csv: \n")
            print(urlfile,dni,tipo,salida)
            try:
                resultado = buscarDni(dni, tipo)
                if salida =="PANTALLA":
                    print(resultado)
                elif salida == "CSV":
                    CSVDES(resultado)
                else:
                    print("invalido")
            except:
                print("invalido")
       
        elif op =="2":
            runTime = False 
        else:
            runTime = False


