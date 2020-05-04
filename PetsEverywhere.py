# class PlayerCharacter:
# 	membership = True

# 	def __init__(self,name,age):
# 		if (self.membership):
# 			self._name = name
# 			self._age = age
		    

# 	def run(self):
# 		print ('run')

# 	def shout(self):
# 		print(f"my name is {self._name} and my age is {self._age}")
# 		return "Shouted"
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Smokey(Cat):
    def sing(self,sounds):
      return f"{sounds}"

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
kitten_one = Simon('CoCo', 1)
kitten_two = Sally('Smokey',2)
kitten_three = Smokey('Midnight',3)
my_cats = [kitten_one,kitten_two,kitten_three]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets([kitten_one, kitten_two, kitten_three])
#4 Output all of the cats walking using the my_pets instance
my_pets.walk()