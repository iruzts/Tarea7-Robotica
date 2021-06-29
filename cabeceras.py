cabecera = {
    "Atlántida":"La Ceiba",
    "Colón":"Trujillo",
    "Comayagua":"Comayagua",
    "Copán":"Santa Rosa de Copán",
    "Cortés":"San Pedro Sula",
    "Choluteca":"Choluteca",
    "El Paraíso":"Yuscarán",
    "Francisco Morazán":"Tegucigalpa",
    "Gracias a Dios":"Puerto Lempira",
    "Intibucá":"La Esperanza",
    "Islas de la Bahía": "Roatán",
    "La Paz":"La Paz",
    "Lempira":"Gracias",
    "Ocotepeque":"Ocotepeque",
    "Olancho":"Juticalpa",
    "Santa Bárbara":"Santa Bárbara",
    "Valle":"Nacaome",
    "Yoro":"Yoro"
}

try:
    print ("Cabeceras de Honduras")
    print ("Ingrese Nombre de Un Departamento para Ver la Cabecera Correspondiente")
    departamento = input("Ingresar: ")
    print("La Cebecera de {} es  {} .".format(departamento, format(cabecera[departamento],)))
except KeyError:
    print("El Pais no existe")