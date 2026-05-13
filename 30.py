class animal:
    def sound(self, name):
        print(f"{name} makes a sound")
    
class dog(animal):
    def sound(self, name):
        print(f"{name} barks")

a1 = animal()
d1 = dog()
a1.sound("Generic Animal")
d1.sound("lion")