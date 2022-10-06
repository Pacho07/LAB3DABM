
import puert
import Reporte

class controlador:



    def Todo(self):

        opcion=0



        reportador=Reporte.report('../baseDatos/Temperatura.csv')



        while(opcion!=4):

            opcion = primerapantalla()

            if opcion==1:

                opcion=segundaPantalla()

                if opcion==1:
                    import plototo
                    grafica=plototo.plotic()
                    grafica.piplot()

                    print('Estos fueron los datos recolectados: ')

                    reportador.mostrarValores()

                elif opcion==2:

                    print('introducir cantidad de datos que se requieren')
                    opcion=int(input())
                    import puert

                    guardado=puert.Puertico('COM3',9600)
                    guardado.abrir()
                    guardado.leerCantidadDatos(opcion)

                    print('Estos fueron los datos recolectados: ')

                    reportador.mostrarValores()

            if opcion ==2:

                while(opcion!=5):

                    manejo=Reporte.report('../baseDatos/Temperatura.csv')

                    opcion=terceraPantalla()

                    if opcion==1:
                        manejo.mostrarValores()

                    elif opcion==2:
                        manejo.valorMaximoFecha()

                    elif opcion==3:
                        manejo.valorPromedio()







def primerapantalla():
    print('SENSOR RECOLECTOR DE DATOS DE TEMPERATURA')

    print('1. RECOLECTAR DATOS')

    print('2.ANALISIS')

    print('4.SALIR')

    opcion = int(input())

    return opcion

def segundaPantalla():
    print('''RECOLECCION DE DATOS''')
    print('1.GRAFICA')
    print('2.NUMERO DE DATOS A RECOLECTAR')
    print('3.DEVOLVERSE')

    opcion = int(input())

    return opcion

def terceraPantalla():
    print('ANALISIS DE DATOS')

    print('1.MOSTRAR DATOS RECOLECTADOS')
    print('2.MAYOR Y MENOR DATOS RECOLECTADOS')
    print('3.PROMEDIO DE LOS VALORES RECOLECTADOS')
    print('5.DEVOLVERSE PANTALLA DE INICIO')

    opcion=int(input())

    return opcion



