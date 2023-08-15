from functools import wraps
def main_decorator(func):

    @wraps(func)
    def function(*args,**kargs):
        print("in main decorator")
        obj = my_class()
        function_call = getattr(obj, args[0])
        result = function_call(**kargs)
        print("end of wrapper")
        return func(*args, result=result, **kargs)

    return function


@main_decorator
def decorator_function(animal,*args,**kargs):
    print("in decorator function")
    return kargs['result']

class my_class:
    def dog(self, number):
        print("im a dog : "+str(number))
        return "from dog"

    def cat(self, number):
        print("im a cat : "+str(number))

    def lion(self, age):
        print("im a lion : "+str(age))

if __name__=='__main__':
    result = decorator_function("dog", number=3)
    print(result)
    # print("&&&&&&&&&&")
    # decorator_function("cat", number=5)
    # print("&&&&&&&&&&")
    # decorator_function("lion", age=45)