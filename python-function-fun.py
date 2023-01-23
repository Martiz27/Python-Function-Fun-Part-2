#Function 1
def arb_args(*args):
    for a in args:
        print(a)

def inner_func(x, y):
    def math1():
        return x + y
    def math2():
        return x - y
    print (math1() + math2())

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

def sum_n_product(a, b):
    def product():
        return a*b
    def sum():
        return a+b
    print(product(), sum())

alias_arb_args = arb_args

def arb_mean(*integers):
    total = 0
    for a in integers:
        total += a
    print(a/len(integers))

def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest


arb_args(1, 2, 3)
inner_func(3, 5)
lunch_lady("Micky")
sum_n_product(2, 3)
arb_mean(1, 4, 5, 6) 
print(arb_longest_string("Leon","Michael", "Michelle", "Laura", "Denise", "Nancy"))  