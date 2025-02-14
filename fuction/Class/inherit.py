class animal:
    def sound(self):
        print("all animals make sound ")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(animal):
    def sound(self):
        print("cat meows")
d=dog()
c=cat()
d.sound()
c.sound()

