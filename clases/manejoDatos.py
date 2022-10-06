import datetime


class ManejoData:

    def GuardandoExep(self, para):
        file = open("../../baseDatos/Temperatura.csv", 'a')

        for i in para:
            fecha = datetime.datetime.today()
            hora = datetime.datetime.now()
            horafi = hora.strftime("%H:%M:%S")
            fechafi = fecha.strftime("%D/%M/%A")
            file.write(str(i) + ',' + fechafi + ',' + horafi + '\n')


        file.close()

