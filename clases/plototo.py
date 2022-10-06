import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import clases.manejoDatos
import clases.Parametros
import time

puerto = serial.Serial('COM3', 9600)
ydata = []

fig, ax = plt.subplots()
parametrizaje = clases.Parametros.GenerarControlParameters1(10,20,30)

pause = False




class plotic:





    def piplot(self):
        try:



            puerto.close()
            puerto.open()

            print('port is open')




        except:

            print('problemas abriendo puerto')

        fig.canvas.mpl_connect('button_press_event', onclick)
        time.sleep(2)
        ani = animation.FuncAnimation(fig, update_data)
        plt.show()


def onclick(event):
 global pause
 print('pause')
 pause=True








def update_data(i):
     if not pause:
        punto = puerto.readline().decode().strip()
        ydata.append(punto)
        ax.clear()
        ax.plot(ydata)
        leed=parametrizaje.controlTemp(punto)


     else:
        guardado = clases.manejoDatos.ManejoData()
        guardado.GuardandoExep(ydata)




