import serial
import datetime
import manejoDatos
import time
import Parametros


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
        ydata=[]

        parametrizaje = Parametros.GenerarControlParameters()

        for i in range(numero):
            hola=self.puerto.readline().decode().strip()
            time.sleep(1)
            print('la medicion es cada 1 segundo')
            ydata.append(hola)
            leed=parametrizaje.controlTemp(hola)
            self.puerto.write(leed)


        guardado=manejoDatos.ManejoData()
        guardado.GuardandoExep(ydata)

        self.puerto.close()





