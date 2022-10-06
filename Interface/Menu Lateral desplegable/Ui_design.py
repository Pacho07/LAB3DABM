# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1009, 747)
        MainWindow.setMinimumSize(QSize(1000, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"\n"
"QFrame{\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"background-color:#ffccbc;\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(500, 0))
        self.bt_menu.setMaximumSize(QSize(200, 16777215))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: #ffffee;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../../../../../Menu Lateral desplegable/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_menu, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(35, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../Menu Lateral desplegable/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))
        self.bt_minimizar.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_minimizar, 0, Qt.AlignRight)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(35, 35))
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../Menu Lateral desplegable/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.bt_restaurar, 0, Qt.AlignRight)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(35, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../../Menu Lateral desplegable/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_maximizar, 0, Qt.AlignRight)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:red;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../../../Menu Lateral desplegable/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_cerrar, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(500, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet(u"\n"
"QFrame{\n"
"background-color:#ffffee;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: #ffffee;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 9pt \"Arial Narrow\";\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.bt_inicio.setFont(font)
        self.bt_inicio.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"../../../../../.designer/backup/nueva-base-de-datos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_uno = QPushButton(self.frame_lateral)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setMinimumSize(QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../.designer/backup/analisis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon6)
        self.bt_uno.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_uno)

        self.bt_dos = QPushButton(self.frame_lateral)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setMinimumSize(QSize(0, 40))
        self.bt_dos.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"../../../../../.designer/backup/grafico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_dos.setIcon(icon7)
        self.bt_dos.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_dos)

        self.bt_tres = QPushButton(self.frame_lateral)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setMinimumSize(QSize(0, 40))
        self.bt_tres.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"../../../../../.designer/backup/termometro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_tres.setIcon(icon8)
        self.bt_tres.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_tres)

        self.bt_tres_4 = QPushButton(self.frame_lateral)
        self.bt_tres_4.setObjectName(u"bt_tres_4")
        self.bt_tres_4.setMinimumSize(QSize(0, 40))
        self.bt_tres_4.setStyleSheet(u"")
        self.bt_tres_4.setIcon(icon8)
        self.bt_tres_4.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_tres_4)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.frame_contenedor.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../../../../.designer/backup/\u00edndice.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)

        self.verticalLayout_9.addWidget(self.label)

        self.stackedWidget.addWidget(self.page)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        self.page_uno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.page_uno)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.page_uno)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.refrescar = QPushButton(self.frame_2)
        self.refrescar.setObjectName(u"refrescar")
        self.refrescar.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.refrescar.setFont(font1)
        self.refrescar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.refrescar.setLayoutDirection(Qt.LeftToRight)
        self.refrescar.setIcon(icon5)
        self.refrescar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.refrescar)

        self.eliminadatos = QPushButton(self.frame_2)
        self.eliminadatos.setObjectName(u"eliminadatos")
        self.eliminadatos.setMinimumSize(QSize(0, 40))
        self.eliminadatos.setFont(font1)
        self.eliminadatos.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.eliminadatos.setLayoutDirection(Qt.LeftToRight)
        self.eliminadatos.setIcon(icon5)
        self.eliminadatos.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.eliminadatos)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.eliminadatos.raise_()
        self.refrescar.raise_()

        self.verticalLayout_4.addWidget(self.frame_2)

        self.tableDatos = QTableWidget(self.page_uno)
        self.tableDatos.setObjectName(u"tableDatos")

        self.verticalLayout_4.addWidget(self.tableDatos)

        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        self.page_dos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.page_dos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.grafiacaAnalisi = QFrame(self.page_dos)
        self.grafiacaAnalisi.setObjectName(u"grafiacaAnalisi")
        self.grafiacaAnalisi.setFrameShape(QFrame.StyledPanel)
        self.grafiacaAnalisi.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.grafiacaAnalisi)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 511, 291))
        self.graficaDatosAnalisis = QVBoxLayout(self.verticalLayoutWidget)
        self.graficaDatosAnalisis.setObjectName(u"graficaDatosAnalisis")
        self.graficaDatosAnalisis.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.grafiacaAnalisi)

        self.datosAnalisis = QFrame(self.page_dos)
        self.datosAnalisis.setObjectName(u"datosAnalisis")
        self.datosAnalisis.setFrameShape(QFrame.StyledPanel)
        self.datosAnalisis.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.datosAnalisis)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.botonDatomayor = QPushButton(self.datosAnalisis)
        self.botonDatomayor.setObjectName(u"botonDatomayor")
        self.botonDatomayor.setMinimumSize(QSize(0, 40))
        self.botonDatomayor.setStyleSheet(u"")
        self.botonDatomayor.setIcon(icon8)
        self.botonDatomayor.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.botonDatomayor)

        self.datosMayoresMenores = QLabel(self.datosAnalisis)
        self.datosMayoresMenores.setObjectName(u"datosMayoresMenores")

        self.verticalLayout_10.addWidget(self.datosMayoresMenores)

        self.botondatomenor = QPushButton(self.datosAnalisis)
        self.botondatomenor.setObjectName(u"botondatomenor")
        self.botondatomenor.setMinimumSize(QSize(0, 40))
        self.botondatomenor.setStyleSheet(u"")
        self.botondatomenor.setIcon(icon8)
        self.botondatomenor.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.botondatomenor)

        self.promedioDatosRecolectados = QLabel(self.datosAnalisis)
        self.promedioDatosRecolectados.setObjectName(u"promedioDatosRecolectados")

        self.verticalLayout_10.addWidget(self.promedioDatosRecolectados)


        self.verticalLayout_5.addWidget(self.datosAnalisis)

        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QWidget()
        self.page_tres.setObjectName(u"page_tres")
        self.verticalLayout_6 = QVBoxLayout(self.page_tres)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graficaRecoleccion = QVBoxLayout()
        self.graficaRecoleccion.setObjectName(u"graficaRecoleccion")

        self.verticalLayout_6.addLayout(self.graficaRecoleccion)

        self.seguirjeje = QPushButton(self.page_tres)
        self.seguirjeje.setObjectName(u"seguirjeje")
        self.seguirjeje.setMinimumSize(QSize(0, 40))
        self.seguirjeje.setStyleSheet(u"")
        self.seguirjeje.setIcon(icon8)
        self.seguirjeje.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.seguirjeje)

        self.DETENERTOMA = QPushButton(self.page_tres)
        self.DETENERTOMA.setObjectName(u"DETENERTOMA")
        self.DETENERTOMA.setMinimumSize(QSize(0, 40))
        self.DETENERTOMA.setStyleSheet(u"")
        self.DETENERTOMA.setIcon(icon8)
        self.DETENERTOMA.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.DETENERTOMA)

        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QWidget()
        self.page_cuatro.setObjectName(u"page_cuatro")
        self.page_cuatro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QVBoxLayout(self.page_cuatro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.graficaRecoleccionDatos = QVBoxLayout()
        self.graficaRecoleccionDatos.setObjectName(u"graficaRecoleccionDatos")

        self.verticalLayout_7.addLayout(self.graficaRecoleccionDatos)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.page_cuatro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.InicioMediciones = QPushButton(self.frame)
        self.InicioMediciones.setObjectName(u"InicioMediciones")
        self.InicioMediciones.setGeometry(QRect(20, 130, 398, 40))
        self.InicioMediciones.setMinimumSize(QSize(0, 40))
        self.InicioMediciones.setStyleSheet(u"")
        self.InicioMediciones.setIcon(icon7)
        self.InicioMediciones.setIconSize(QSize(32, 32))
        self.numeroMediciones = QLineEdit(self.frame)
        self.numeroMediciones.setObjectName(u"numeroMediciones")
        self.numeroMediciones.setGeometry(QRect(440, 140, 113, 20))
        self.EscribirProcesoMedicion = QLabel(self.frame)
        self.EscribirProcesoMedicion.setObjectName(u"EscribirProcesoMedicion")
        self.EscribirProcesoMedicion.setGeometry(QRect(270, 230, 47, 14))

        self.verticalLayout_12.addWidget(self.frame)


        self.verticalLayout_7.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        self.page_cinco.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cinco)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.page_cinco)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.bt_inicio_2 = QPushButton(self.frame_3)
        self.bt_inicio_2.setObjectName(u"bt_inicio_2")
        self.bt_inicio_2.setMinimumSize(QSize(0, 40))
        self.bt_inicio_2.setFont(font1)
        self.bt_inicio_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio_2.setLayoutDirection(Qt.LeftToRight)
        self.bt_inicio_2.setIcon(icon5)
        self.bt_inicio_2.setIconSize(QSize(32, 32))

        self.verticalLayout_14.addWidget(self.bt_inicio_2)

        self.limInfoH = QLineEdit(self.frame_3)
        self.limInfoH.setObjectName(u"limInfoH")

        self.verticalLayout_14.addWidget(self.limInfoH)

        self.bt_inicio_3 = QPushButton(self.frame_3)
        self.bt_inicio_3.setObjectName(u"bt_inicio_3")
        self.bt_inicio_3.setMinimumSize(QSize(0, 40))
        self.bt_inicio_3.setFont(font1)
        self.bt_inicio_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio_3.setLayoutDirection(Qt.LeftToRight)
        self.bt_inicio_3.setIcon(icon5)
        self.bt_inicio_3.setIconSize(QSize(32, 32))

        self.verticalLayout_14.addWidget(self.bt_inicio_3)

        self.limInfoN = QLineEdit(self.frame_3)
        self.limInfoN.setObjectName(u"limInfoN")

        self.verticalLayout_14.addWidget(self.limInfoN)

        self.bt_inicio_4 = QPushButton(self.frame_3)
        self.bt_inicio_4.setObjectName(u"bt_inicio_4")
        self.bt_inicio_4.setMinimumSize(QSize(0, 40))
        self.bt_inicio_4.setFont(font1)
        self.bt_inicio_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio_4.setLayoutDirection(Qt.LeftToRight)
        self.bt_inicio_4.setIcon(icon5)
        self.bt_inicio_4.setIconSize(QSize(32, 32))

        self.verticalLayout_14.addWidget(self.bt_inicio_4)

        self.limSupN = QLineEdit(self.frame_3)
        self.limSupN.setObjectName(u"limSupN")

        self.verticalLayout_14.addWidget(self.limSupN)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_cinco)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bt_menu.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"    MENU ", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"DATOS", None))
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"ANALISIS DE DATOS", None))
        self.bt_dos.setText(QCoreApplication.translate("MainWindow", u"MEDICION REAL GRAFICA", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"   MEDICION REAL N. DATOS", None))
        self.bt_tres_4.setText(QCoreApplication.translate("MainWindow", u"RANGOS DE MEDICION", None))
        self.label.setText("")
        self.refrescar.setText(QCoreApplication.translate("MainWindow", u"REFRESCAR", None))
        self.eliminadatos.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR DATOS", None))
        self.botonDatomayor.setText(QCoreApplication.translate("MainWindow", u"DATO MAYOR Y DATO MENOR", None))
        self.datosMayoresMenores.setText("")
        self.botondatomenor.setText(QCoreApplication.translate("MainWindow", u"PROMEDIO DE DATOS RECOLECTADOS", None))
        self.promedioDatosRecolectados.setText("")
        self.seguirjeje.setText(QCoreApplication.translate("MainWindow", u"REANUDAR PROCESAMIENTO", None))
        self.DETENERTOMA.setText(QCoreApplication.translate("MainWindow", u"DETENER TOMA DE TEMPERATURA", None))
        self.InicioMediciones.setText(QCoreApplication.translate("MainWindow", u"NUMERO DE MEDICIONES", None))
        self.EscribirProcesoMedicion.setText("")
        self.bt_inicio_2.setText(QCoreApplication.translate("MainWindow", u"LIMITE INFERIOR HIPOTERMIA", None))
        self.bt_inicio_3.setText(QCoreApplication.translate("MainWindow", u"LIMITE INFERIOR TEMPERATURA NORMAL", None))
        self.bt_inicio_4.setText(QCoreApplication.translate("MainWindow", u"LIMITE SUPERIOR TEMPERATURA NORMAL", None))
    # retranslateUi

