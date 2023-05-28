class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print("This is MyMeta __call__")

class A(metaclass=MyMeta):
    pass

class B():
    def __call__(cls, *args, **kwargs):
        print("This may be type __call__")
        super.__call__(cls, *args, **kwargs)
        print("This is B __call__")


a = A()
b = B()
