# 1.Write a Python program to show single inheritance using classes Animal and Dog. 
print("Enrollment No :- 92600565007")
print("Name :- Vasu Parmar")
print("-" * 50)

class animal:
    def speak(self):
        print("animal speacking")
class dog(animal):
    def bark(self):
        print("dog is barking")

d1=dog()
d1.speak()
d1.bark()                