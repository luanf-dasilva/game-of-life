from time import time
from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)
    
    def __set__(self, obj,  value):
        self.validate(value)

    @abstractmethod
    def validate(self, value):
        pass

class Integer(Validator):
    def __init__(self, minsize=None, maxsize=None, input_name=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.input_name = input_name

    def validate(self, value):
        if self.maxsize is not None and value > self.maxsize:
            raise ValueError(f"Excpected value of {self.input_name}: {value} to be less than {self.maxsize}.")
        if self.minsize is not None and value < self.minsize:
            raise TypeError(f"Excpected value of {self.input_name}: {value} to be more than {self.minsize}.")

class RGB(Validator):
    def __init__(self, input_name=None):
        self.tuple_length = 3
        self.tuple_min = 0
        self.tuple_max = 255
        self.input_name = input_name

    def validate(self, value):
        for i in value:
            if i < self.tuple_min or i > self.tuple_max:
                raise ValueError(f"RGB tuple for {self.input_name}: {value} entries must be integers between 0 and 255") 

def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("%s took {:0.2f} seconds to complete".format(after - before), end=" ")
        return rv
    return wrapper