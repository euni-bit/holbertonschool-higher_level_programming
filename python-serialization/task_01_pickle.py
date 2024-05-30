import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error occurred while serializing:", e)
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, CustomObject):
                    return obj
                else:
                    print("Invalid object type loaded from file.")
                    return None
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError as e:
            print("Error occurred while deserializing:", e)
            return None
