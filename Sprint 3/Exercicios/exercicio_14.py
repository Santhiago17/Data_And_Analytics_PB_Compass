def print_params(*args, **kwargs):

    for arg in args:
        print(arg)

    for value in kwargs.values():
        print(value)


print_params(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
