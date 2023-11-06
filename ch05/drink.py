from abc import ABC, abstractmethod

class BaseDrink(ABC):
    def prepare(self):
        self.add_powder()
        self.brew()
        self.pour_into_cup()
        self.add_condiments()

    @abstractmethod
    def add_powder(self):
        pass

    def brew(self):
        print('steeping')

    def pour_into_cup(self):
        print('pour drink into cup')

    @abstractmethod
    def add_condiments(self):
        pass

class Coco(BaseDrink):
    def add_powder(self):
        print('add coco powder')

    def add_condiments(self):
        print('add nothing')


class Coffee(BaseDrink):
    def add_powder(self):
        print('add coffee powder')

    def add_condiments(self):
        print('add sugar')