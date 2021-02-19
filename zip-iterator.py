## MANUEL GUILLERMO GIL 14-10397 - 14-10397@usb.ve

## Funcion que toma dos listas y las une en un lista uniendo sus elementos en una dupla
## @param a - primera lista
## @param b - segunda lista
def zip(a, b):
    if a and b:
        yield (a[0], b[0])
        for p in zip(a[1:], b[1:]):
            yield p

## Funcion que toma dos listas y una funcion, aplicando la funcion para un elemento de la primera lista y otro de la segunda
## siguiendo el mismo orden con el indice
## @param a - primera lista
## @param b - segunda lista
## @param func - funcion
def zipWith(a, b, func):
    if a and b:
        yield func(a[0], b[0])
        for p in zipWith(a[1:], b[1:], func):
            yield p

print("Resultado de aplicar zip a [1, 2, 3] y ['a', 'b', 'c']: ")
for p in zip([1, 2, 3], ['a', 'b', 'c']):
    print p

print("\n")
print("Resultado de aplicar zipWith a [0, 1, 2, 1] y [1, 2, 1, 0] y aplicando la funcion lambda x, y: x + y: ")
for p in zipWith([0, 1, 2, 1], [1, 2, 1, 0], lambda x, y: x + y):
    print p