class Coco():
    def prepare(self):
        self.add_powder()
        self.brew()
        self.pour_into_cup()

    def add_coco_powder(self):
        print('add coco powder')

    def brew(self):
        print('steeping')

    def pour_coco_into_cup(self):
        print('pour drink into cup')


class Coffee():
    def prepare(self):
        self.add_powder()
        self.brew()
        self.pour_into_cup()
        self.add_condiments()

    def add_coffee_powder(self):
        print('add coffee powder')

    def brew(self):
        print('steeping')

    def pour_coffee_into_cup(self):
        print('pour drink into cup')

    def add_condiments(self):
        print('add sugar')