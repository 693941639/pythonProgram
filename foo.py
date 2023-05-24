#pythran export foo()
#pythran export a

a = "This is change to c++ test"

def foo():
    print(a)
    return a
