
class parameters:

    def __init__(self,hbajo,nbajo,nalto):

        self.hbajo=hbajo
        self.nbajo=nbajo
        self.nalto=nalto


    def controlTemp(self,dato):



        if int(dato) >= int(self.hbajo) and int(dato) <= int(self.nbajo):
            temp = 'H'
        elif int(dato) >= int(self.nbajo) and int(dato) <= int(self.nalto):
            temp = 'N'
        else :
            temp = 'F'

        return temp.encode()




def GenerarControlParameters():

    print('DEFINIR RANGOS DE TEMPERATURA')

    print('ingrese valor limite inferior hipotermina')
    hbajo = int(input())
    print('ingrese valor limite inferior normalidad')
    nbajo = int(input())
    print('ingrese valor limite superior normalidad')
    nalto = int(input())

    hola=parameters(hbajo,nbajo,nalto)

    return hola


def GenerarControlParameters1(hbajo,nbajo,nalto):


    hola=parameters(hbajo,nbajo,nalto)

    return hola