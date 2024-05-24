# Define SwimMixin
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Define FlyMixin
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Define Dragon inheriting from SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
