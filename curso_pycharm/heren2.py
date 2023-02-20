class Animal:
	def __init__(self, especie, edad):
		self.especie = especie
		self.edad = edad

	def hablar(self):
		pass

	def moverse(self):
		pass

	def describeme(self):
		print ("Soy un animal del tipo ",type(self).__name__)




class Perro(Animal):

	def __init__(self, especie, edad, raza):
		super().__init__(especie,edad)
		self.raza =  raza
	
	def hablar(self):
		print ("Guauuuuuu")

	def moverse(self):
		print ("Corro")





class Pez(Animal):
	
	def __init__(self, especie, edad, tipo):
		super().__init__(especie,edad)
		self.tipo = tipo

	def hablar(self):
		print ("Glu, glu, glu")


	def moverse(self):
		print ("Nado")

	def tipoAgua(self):
		print ("Soy de agua ",self.tipo)



class Insecto(Animal):
	def hablar(self):
		print ("ZZZZZZZZZZZZZZZZ")
	
	def moverse(self):
		print ("Vuelo")





if __name__=="__main__":
	iris = Perro("mamifero",2,"Caniche")
	hanibal = Pez("sardina", 1,"salada")
	bicho = Insecto("mosca asquerosa",0.01)


	iris.hablar()
	iris.describeme()

	hanibal.hablar()
	hanibal.describeme()

	bicho.hablar()
	bicho.describeme()

	print ("Ahora explicaré el polimorfismo\n")
	animales=[Perro("mamifero",5,"Lobo"), Pez("Tiburon", 2,"salada"), Insecto("arania",0.05)]
	for animal in animales:
		print (animal.describeme())
		animal.hablar()
		if type(animal).__name__ == "Pez":
			animal.tipoAgua()
