import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import manejoDatos
import Parametros
import time

puerto = serial.Serial('COM3', 9600)
ydata = []

fig, ax = plt.subplots()
parametrizaje = Parametros.GenerarControlParameters()

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
        puerto.write(leed)

     else:
        guardado = manejoDatos.ManejoData()
        guardado.GuardandoExep(ydata)




