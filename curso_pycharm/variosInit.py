
'''
    santi
    24/01/2022
    
    La especificacion de diferentes constructores, lo haremos
    con los argumentos pasados con valores predeterminados.
    Os pongo un ejemplo.
    
    Por cierto, cuando queremos concatenar una cadena con un objeto,
    si intentamos hacer un 
                            int("mensaje" + objeto)
    nos da un error de que no podemos concatenar str con objeto, solo con str. 
    Lo solucionamos llamando explicitamente al __str__()
'''
    
class E:   
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        
    def __str__(self):
        ret = ""
        if (self.a):     #Si existe, lo incluimos
            ret = "Atributo a: " + str(self.a) + " "
            
        if (self.b):    #Si existe, lo incluimos a lo que ya teniamos.
            ret += " Atributo b: " + str(self.b)
            
        return ret
    
    
if __name__ == "__main__":
    
    #Llamamos al constructor por defecto
    e = E()
    
    #Llamamos al constructor con un solo argumento
    b = E(1)
    
    #Llamamos al constructor con dos argumentos.
    c = E(1, 2)
 
    print (e)
    print ("El objeto b es " + b.__str__())
    print ("El objeto c es " +  c.__str__())
 