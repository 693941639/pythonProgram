# class A(object):
#     val = None

#     # def __init__(self, val):
#     #     self.set_val = val

#     # @property
#     # def get_val(self):
#     #     return self.val
    
#     # @get_val.setter
#     # def set_val(self, val):
#     #     self.__class__.val = val

#     def __new__(cls, *arg, **kwargs):
#         if cls.val is None:
#             cls.val = object.__new__(cls, *arg, **kwargs)

#         return cls.val
    
#     def __init__(self, val):
#         self.val = val
    
# a = A(1)
# b = A(1)

# print(id(a), id(b))

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class Test():
    def __init__(self):
        pass

b1 = Test()
b2 = Test()

print(id(b1) == id(b2))
