usuarios = {"Pablo", "Daniel", "Ruben", "Ale", "Sara"}
administradores = {"Ruben", "Ale"}

administradores.discard("Ruben")
administradores.add("Pablo")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es administrador")
    else:
        print(usuario, "no es administrador")
