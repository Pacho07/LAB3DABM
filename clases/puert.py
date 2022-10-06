import serial
import datetime
import clases.manejoDatos
import time
import clases.Parametros


class Puertico:

    def __init__(self,port,baudrate):
        self.port=port
        self.baudrate =baudrate



    def abrir(self):
        puerto= serial.Serial(self.port,self.baudrate)
        self.puerto = puerto


    def leer(self):
        dato=self.puerto.readline().decode().strip()
        return dato



    def leerGuardando(self):
        dato = self.puerto.readline().decode().strip()
        datos=";".join(dato+datetime.datetime.time())
        file=open('Temperatura.csv','a')
        file.write(datos+'\n')
        file.close()

    def escribir(self):
        dato = self.puerto.readline().decode().strip()
        serial.Serial.write(dato.encode())

    def leerCantidadDatos(self,numero):

        self.abrir()


        ydata=[]
        parametrizaje = clases.Parametros.GenerarControlParameters1(10,20,30)
        for i in range(numero):
            hola=self.puerto.readline().decode().strip()
            print('se estan tomando los datos')
            ydata.append(hola)
            leed=parametrizaje.controlTemp(hola)
            self.puerto.write(leed)


        guardado= clases.manejoDatos.ManejoData()
        guardado.GuardandoExep(ydata)

        self.puerto.close()





