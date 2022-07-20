import ipaddress
Id_red=input("Entre la direccion de red y prefijo: ")
ip=ipaddress.IPv4Network(Id_red)
print("La mascara de Subred es:",ip.netmask)
print("La mascara Wildcard es:" ,ip.hostmask)
print("La primera valida o usable es:" ,ip.network_address+1)
print("La ultima valida o usable es:" ,ip.broadcast_address-1)
print("La direccion de Broadcast es:" ,ip.broadcast_address)
print("Es una direccion Privada:" ,ip.is_private)
print("Total de direcciones IP Validas o usables:" ,ip.num_addresses-2)
X=input("Quieres conocer cuales son las IP Validas: ")
if X=='si' or X=='SI' or X=='Si':
    for y in ip.hosts():
        print(y)
