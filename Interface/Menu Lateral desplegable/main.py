
import serial
import clases.puert
#import clases.puert
#import clases.Parametros
import clases.Reporte
import sys
import pandas as pd
import math
import clases.Parametros
from Ui_design import *
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import pandas as pd
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from random import randint

#puerto = serial.Serial('COM3', 9600)
import clases.manejoDatos

guardado=clases.manejoDatos.ManejoData()
parametrizaje = clases.Parametros.GenerarControlParameters1(10, 20, 30)
df=pd.read_csv('../../baseDatos/Temperatura.csv')



class MiApp(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		#para graficar creamos nuevas variables
		self.grafica = Analisis_grafica()
		self.ui.graficaDatosAnalisis.addWidget(self.grafica)
		self.ui.botonDatomayor.clicked.connect(lambda: self.ui.graficaDatosAnalisis.addWidget(self.grafica) )
		self.ui.bt_uno.clicked.connect(lambda: self.ui.graficaDatosAnalisis.addWidget(self.grafica))
		self.ui.bt_uno.clicked.connect(lambda: self.parametrizaje())

		#colocamos la media en sus labels
		report=clases.Reporte.report('../../baseDatos/Temperatura.csv')
		self.ui.bt_uno.clicked.connect(lambda: self.ui.datosMayoresMenores.setText(report.valorMaximoFecha()))
		self.ui.bt_uno.clicked.connect(lambda: self.ui.promedioDatosRecolectados.setText(report.valorPromedio()))

		#para la otra forma de obtener los datos
		self.ui.InicioMediciones.clicked.connect(lambda: self.parametrizaje())
		self.ui.InicioMediciones.clicked.connect(lambda: self.MedicionesNumero())









		#para la animacion
		self.graRecole= recolec_grafica()
		self.ui.bt_dos.clicked.connect(lambda: self.ui.graficaRecoleccion.addWidget(self.graRecole))
		self.ui.DETENERTOMA.clicked.connect(lambda: self.graRecole.guardar())
		self.ui.seguirjeje.clicked.connect(lambda: self.graRecole.Continuar())

		#aqui termina animacion



		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

		#acceder a las paginas coloca
		self.ui.stackedWidget.setCurrentWidget(self.ui.page)
		self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
		self.ui.bt_inicio.clicked.connect(lambda: self.tabla())
		self.ui.eliminadatos.clicked.connect(lambda: self.reinBD())
		self.ui.refrescar.clicked.connect(lambda: self.tabla())


		self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))
		self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
		self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))
		self.ui.bt_tres_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))


		#control barra de titulos
		self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.bt_cerrar.clicked.connect(lambda: self.close())

		self.ui.bt_restaurar.hide()

		#menu lateral
		self.ui.bt_menu.clicked.connect(self.mover_menu)

	def control_bt_minimizar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.bt_restaurar.hide()
		self.ui.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.bt_maximizar.hide()
		self.ui.bt_restaurar.show()

	def mover_menu(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 500
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <= 20:
			self.showMaximized()
		else:
			self.showNormal()




	def tabla(self):
		file = pd.read_csv('../../baseDatos/Temperatura.csv')


		numRows = file.shape[0]

		self.ui.tableDatos.setColumnCount(file.shape[1])
		self.ui.tableDatos.setRowCount(numRows)
		self.ui.tableDatos.setHorizontalHeaderLabels(file.columns)

		for i in range(numRows):
			for j in range(file.shape[1]):
				self.ui.tableDatos.setItem(i,j,QTableWidgetItem(str(file.iat[i,j])))

	def reinBD(self):
		file=open("../../baseDatos/Temperatura.csv","w")
		file.close()
		file=open("../../baseDatos/Temperatura.csv","a")
		file.write('TEMPERATURA,FECHA,HORA')
		file.close()
		self.tabla()

	def parametrizaje(self,limH=10,limiN=20,linsN=30):
		self.ui.limInfoH.setText('10')
		self.ui.limInfoN.setText('20')
		self.ui.limSupN.setText('30')

		if limH != 10 and limiN !=20 and linsN!=30:
			limH = float(self.ui.limInfoH.text())
			limiN = float(self.ui.limInfoN.text())
			linsN = float(self.ui.limSupN.text())
		hola= clases.Parametros.GenerarControlParameters1(limH,limiN,linsN)




	def MedicionesNumero(self):
		puert=clases.puert.Puertico('COM3',9600)
		puert.leerCantidadDatos(int(self.ui.numeroMediciones.text()))
		self.ui.graficaRecoleccionDatos.addWidget(self.grafica)






	def Canvas_grafica_analisis(self):
		x=self.df['TEMPERATURA']
		plt.plot(x)
		self.ui.graficaDatosAnalisis.set


class Analisis_grafica(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(Analisis_grafica,self).__init__(*args, **kwargs)
		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)
		temp=df['TEMPERATURA']

		new=[]
		for i in temp:

			if math.isnan(i):
				new.append(0)
			else:
				new.append(i)


		self.graphWidget.plot(new)

class recolec_grafica(QtWidgets.QMainWindow):


	def __init__(self, *args, **kwargs):
		self.puerto = serial.Serial('COM3', 9600)
		super(recolec_grafica, self).__init__(*args, **kwargs)
		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)

		self.ydata = []
		self.x = list(range(200))  # 100 time points
		self.y = [randint(0, 300) for _ in range(200)]  # 100 data points

		self.graphWidget.setBackground('w')

		pen = pg.mkPen(color=(255, 0, 0))
		self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

		self.timer = QtCore.QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.update_plot_data)
		self.timer.start()


	def datoNuevo(self):
		return self.puerto.readline().decode().strip()

	def Continuar(self):
		self.puerto.open()
		self.timer.start()

	def update_plot_data(self):
		self.x = self.x[1:]  # Remove the first y element.
		self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
		self.y = self.y[1:]  # Remove the first
		self.y.append(float(self.datoNuevo()))
		self.ydata.append(self.datoNuevo())
		leed=parametrizaje.controlTemp(self.datoNuevo())
		self.puerto.write(leed)
		self.data_line.setData(self.x, self.y)  # Update the data.

	def guardar(self):
		guardado.GuardandoExep(self.ydata)
		self.timer.stop()
		#self.puerto.close()
		self.ydata=[]
		self.puerto.close()











if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())
