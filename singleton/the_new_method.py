class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("Creating Instance", 'args', args, 'kwargs', kwargs )
        if not hasattr(cls,'_inst'):
            print(cls)
            cls._inst = super(Foo, cls).__new__(cls)
        return cls._inst
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def bar(self):
        return f'A:{self.a} && B:{self.b}'


class Boo(object):
    def __new__(cls, *args, **kwargs):
        print("Creating Instance", 'args', args, 'kwargs', kwargs )
        return super(Boo, cls).__new__(cls)
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def bar(self):
        return f'A:{self.a} && B:{self.b}'