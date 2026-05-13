from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car is starting")

c1 = car()
c1.start()
