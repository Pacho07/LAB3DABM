import time

import pandas as pd
import matplotlib.pyplot as plt

class report:

    def __init__(self,nombreCsv):
        self.Bd=pd.read_csv(nombreCsv)


    def mostrarValores(self):
        temp=self.Bd['TEMPERATURA']
        plt.plot(temp)
        plt.title('tiempo vs temperatura')
        plt.show()
        plt.close()





    def valorMaximoFecha(self):

        print('el valor maximo y el valor minimo son:'
              ''
              ''
              '')

        valorMax=self.Bd['TEMPERATURA'].max()
        valorMin=self.Bd['TEMPERATURA'].min()
        posMin=self.Bd.index [self.Bd['TEMPERATURA'] == self.Bd['TEMPERATURA'].min()].tolist()
        posMax=self.Bd.index [self.Bd['TEMPERATURA'] == self.Bd['TEMPERATURA'].max()].tolist()


        print('Valor maximo: '+str(valorMax)+' y su fecha: '+str(self.Bd['FECHA'].get(posMin[0])))
        print('Valor minimo: '+str(valorMin)+' y su fecha: '+str(self.Bd['FECHA'].get(posMax[0])))


    def valorPromedio(self):

        print('El promedio de temperaturas es: '
              ''
              ''
              ''
              '')

        print(str(self.Bd['TEMPERATURA'].mean())+' grados')


