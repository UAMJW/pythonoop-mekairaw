class Marcador(object):
    def __init__ (self, color, marca):
        self.c = color
        self.m = marca
    def agregarColor(self,color):
        self.c=color
    def devolverColor(self):
        return self.c
    def agregarMarca(self,marca):
        self.m = marca
    def devolverMarca(self):
        return self.m

x = Marcador("","")
x.agregarColor("negro")
x.agregarMarca("Scribe")
print x.devolverColor()+" "+x.devolverMarca()
