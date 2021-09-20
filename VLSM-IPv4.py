import ipaddress
import ipaddress

def datosp():
    host = []
    correct = False
    while(not correct):
        try:
            Id_red=input("Entre la direccion de red y prefijo: ")
            IPinicial=ipaddress.IPv4Network(Id_red)
            correct = True
        except (RuntimeError, TypeError, NameError, IndexError, ValueError):
            print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
                       
    print("IP guardada....")
    print(IPinicial)
    print('\n')

    correct = False
    while(not correct):
        try:
            j = int(input("Cuantos hosts desea ingresar: "))
            if j > 0:
                correct = True
            else:
                print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
        except (RuntimeError, TypeError, NameError, IndexError, ValueError):
            print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")

    for i in range(j):
        correct = False
        while(not correct):
            try:
                h = int(input(f"Host {i+1}: "))
                if h >= 0:
                    correct = True
                    host.append(h)
                else:
                    print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
            except (RuntimeError, TypeError, NameError, IndexError, ValueError):
                print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")                

    host.sort(reverse=True)
    print("Ordenando de mayor a menor quedaría de la siguiente forma....")
    print(host)
    print("\n")
    prefijo = int(Id_red.split("/")[-1])
    calculos(host, prefijo, IPinicial)

def calculos(host, prefijo, IPinicial):
    IP = [128, 64, 32, 16, 8, 4, 2]
    hm = []
    exp = []

    for i in range(len(host)):
        for j in range(len(IP)):
            if IP[j] > host[i]:
                x = pow(2, 7-j) - 2
                e = 7-j
        hm.append(x)
        exp.append(e)

    IPv4 = IPinicial.network_address
    for i in range(len(exp)):

        t = 8-exp[i]+prefijo
        ip = ipaddress.IPv4Network(str(IPv4) + "/" + str(t))

        print(f"Para {host[i]} hosts necesito {exp[i]} bits")
        print(f"Los hosts máximos serían: 2^{exp[i]} - 2 (red inicial y broadcast) = ", hm[i])
        #
        print("Su dirección inicial es: ", ip.network_address)
        #
        print("La primera valida o usable es:" ,ip.network_address+1)
        print("La ultima valida o usable es:" ,ip.broadcast_address-1)
        #
        print("La direccion de Broadcast es:" ,ip.broadcast_address)
        #
        print(f"el prefijo de la máscara es: 8 - {exp[i]} + {prefijo} = {t} ")
        print('\n')

        IPv4 = ip.broadcast_address+1
        
datosp()