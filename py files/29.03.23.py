class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class ExpensiveCarFactory(CarFactory):
    def create_car(self):
        return Bugagi(*)
