import math
def add(a , b):


    return a+b

def subtract(a,b):


    return math.fabs(a-b)


def multiply(a,b):
    return a*b

def divide(a,b):


    try:
        c=a/b
        return c
    except Exception as e:
        print('exception has occured',e)




if __name__ == '__main__':
    print("this script will execute the main program")
