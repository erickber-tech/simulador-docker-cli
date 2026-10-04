import random

imagenes = []
contenedores = {}

def generar_id():
    return ''.join(random.choice('abcdef0123456789') for _ in range(6))

print("=== Simulador Docker CLI ===")
print("Escriba 'exit' para salir")

while True:

    comando = input("docker> ").strip()

    if comando == "exit":
        break

    partes = comando.split()

    if len(partes) < 2:
        print("Comando no válido")
        continue

    accion = partes[1]

    if accion == "pull":

        if len(partes) < 3:
            print("Debe indicar una imagen")
            continue

        imagen = partes[2]

        print("Downloading layer...")
        print("Digest: sha256:123456")
        print("Status: Downloaded")

        if imagen not in imagenes:
            imagenes.append(imagen)

    elif accion == "run":

        if len(partes) < 3:
            print("Debe indicar una imagen")
            continue

        imagen = partes[2]

        cid = generar_id()

        contenedores[cid] = {
            "image": imagen,
            "status": "Up"
        }

        print(cid)

    elif accion == "ps":

        print("CONTAINER ID\tIMAGE\tSTATUS")

        for cid, datos in contenedores.items():
            print(f"{cid}\t{datos['image']}\t{datos['status']}")

    elif accion == "stop":

        if len(partes) < 3:
            continue

        cid = partes[2]

        if cid in contenedores:
            contenedores[cid]["status"] = "Exited"
            print(cid)
        else:
            print("Contenedor no existe")

    elif accion == "rm":

        if len(partes) < 3:
            continue

        cid = partes[2]

        if cid not in contenedores:
            print("Contenedor no existe")

        elif contenedores[cid]["status"] == "Up":
            print("Debe detener el contenedor primero")

        else:
            del contenedores[cid]
            print("Contenedor eliminado")

    elif accion == "logs":

        if len(partes) < 3:
            continue

        cid = partes[2]

        if cid in contenedores:
            print("[INFO] Server started")
            print("[INFO] Container running")
        else:
            print("Contenedor no encontrado")

    else:
        print("Comando no soportado")