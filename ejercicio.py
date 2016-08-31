#! usr/bin/python

#tarea de clases en python
class Humano:
    def INICIO (self,nom):
        self.name=nom

    def apantalla(self):
        print 'Name:'
        print self.name
        print '<br>'

persona1=Humano()
persona1.INICIO('lOTERIA')
persona1.apantalla()

persona2=Humano()
persona2.INICIO('rIGOBERTO')
persona2.apantalla()
