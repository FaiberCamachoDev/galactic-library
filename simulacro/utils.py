#def para sumar cualquier cantidad de numeros (sumar args)
def sum_args(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
def show_kwargs(data):
    for key, value in data.item():
        print(f"{key}: {value}")