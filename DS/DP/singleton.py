### Not Singleton

# class Tiger:
    
#     def __str__(self) -> str:
#         return "1 tiger"
#     def roar(self):
#         return "roar"
    
# a = Tiger()
# b = Tiger()

# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')

### Singleton
 
# class _Tiger: # Create a protected class
    
#     def __str__(self) -> str:
#         return "1 tiger"
#     def roar(self):
#         return "roar"
# _instance = None  # instantiate a protected variable

# def tiger():    # Tiger ---> function to control the instantiation of class _Tiger()
#     global _instance # ---> declare variable 
#     if _instance is None: # -- check if variable is None
#         _instance = _Tiger() # instantiate the Class
#     return _instance # return the object with singleton class object

# this is to 
# a = tiger()
# b = tiger()

# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')

# as everything in python is treated as an object, we can del
# that instance before stepping into another one
class Tiger:
    def __init__(self) -> None:
        self.tig = "tig"
    def __str__(self):
        return print(self.tig)
    def fire(self):
        return "lol"
    # def __delattr__(self, name: str) -> None:
    #     return super().__delattr__(name)
# del Tiger
    
a = Tiger()
print(f'ID(a) = {id(a)}')
del a
b = Tiger()
print(f'ID(b) = {id(b)}')