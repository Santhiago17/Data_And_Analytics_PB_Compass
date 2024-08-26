
def my_map(lst,f):
    return [f(x) for x in lst]

def square(x):
    return x ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = my_map(lista,square)
print(result)
