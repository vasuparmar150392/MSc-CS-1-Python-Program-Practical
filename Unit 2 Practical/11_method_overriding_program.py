print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 21: Demonstrate Method Overriding using Animal and Dog")
print("-" * 50)

# Parent Class (Super Class / Base Class)
class Animal:
    def __init__(self, species="Unknown Animal"):
        self.species = species

    # Method to be overridden in child class
    def sound(self):
        print("   Animal sound : Generic animal sound")

    def display_info(self):
        print(f"   Species      : {self.species}")


# Child Class (Sub Class / Derived Class) inheriting from Animal
class Dog(Animal):
    def __init__(self, breed="Labrador"):
        # Calling parent constructor using super()
        super().__init__(species="Canine (Dog)")
        self.breed = breed

    # Overriding the sound() method of parent class Animal
    def sound(self):
        print(f"   Dog sound    : Bark! Woof Woof! (Breed: {self.breed})")

    # Additional child-specific method
    def fetch(self):
        print("   Dog action   : Fetching the ball...")


# 1. Creating an object of Parent Class (Animal)
print("1. Parent Class (Animal) Object:")
generic_animal = Animal()
generic_animal.display_info()
generic_animal.sound()

# 2. Creating an object of Child Class (Dog)
print("\n2. Child Class (Dog) Object (Method Overridden):")
my_dog = Dog(breed="German Shepherd")
my_dog.display_info()  # Inherited method from Animal
my_dog.sound()         # Overridden method in Dog
my_dog.fetch()         # Child's own method

# 3. Demonstrating Polymorphism via iteration
print("\n3. Polymorphic behavior:")
animals = [Animal(), Dog(breed="Golden Retriever")]
for idx, a in enumerate(animals, 1):
    print(f"   Object {idx}:")
    a.sound()
