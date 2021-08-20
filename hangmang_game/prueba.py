def agregar(letra, letrasTotales):
    # # debe comparar cada elemento de la lista con la letra añadir, si la letra es diferente a todas, añadirla, sino no
    for i in letrasTotales:
        if letra == i:
            print('Ya usaste esta letra, usa otra')
            continue