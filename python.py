respuesta = "s" or "S"
while respuesta:
    print('---------NÓMINA---------')
    print("!DIGITE LOS DATOS SIN ESPACIOS¡")
    import re
    bander = True
    while bander:
        nombres = str(input("INGRESE LOS NOMBRES:"))
        d = re.findall("[^a-zñA-ZÑ]",nombres)
        if d:
            print("caracteres incorrectos intente de nuevo")
        elif not nombres:
            print("quedo en blanco")
        elif len (nombres)>35:
            print("se paso del maximo")
        elif len (nombres)<2:
            print("muy pocos caracteres")
        else:
            bander = False
    import re
    bander = True
    while bander:
        apellidos = str(input("INGRESE LOS APELLIDOS: "))
        d = re.findall("[^a-zñA-ZÑ]",apellidos)
        if d:
            print("caracteres incorrectos intente de nuevo")
        elif not apellidos:
            print("quedo en blanco")
        elif len (apellidos)>35:
            print("se paso del maximo")
        elif len (apellidos)<2:
            print("muy pocos caracteres")
        else:
            bander = False
    bander = True
    while bander:
        documento = (input("INGRESE EL NUMERO DE DOCUMENTO: "))
        if not documento.isdigit():
            print("caracteres incorrectos intente de nuevo")
        elif len (documento)>35:
            print("se paso del maximo")
        elif len (documento)<5:
            print("muy pocos caracteres")
        else:
            bander = False
        salario = int(input("INGRESE EL SALARIO: "))
    dias_trabajados = int(input("INGRESE LOS DIAS TRABAJADOS: "))
    while dias_trabajados>31:
        print("LOS DIAS DEBEN SER MENORES A 30")
        dias_trabajados = int(input("INGRESE LOS DIAS TRABAJADOS: "))
        if dias_trabajados<31:    
            print('----------------------')
    salario_d_t = (salario/30)*dias_trabajados
    salario_descuentos = (salario_d_t * 0.08)
    salario_subtotal = (salario_d_t - salario_descuentos)
    transporte = (117100/30)*dias_trabajados
    salario_total = (salario_subtotal + transporte)
    
    print('NOMBRES',nombres)
    print('APELLIDOS',apellidos)
    print('DOCUMENTO',documento)
    print('SALARIO',salario)
    print('DIAS_TRABAJADOS',dias_trabajados)
    print('SALARIO POR DIAS TRABAJADOS',salario_d_t)
    if salario > 2000000:
        salario_a=salario_subtotal
        print('SALARIO TOTAL CON DESCUENTOS POR SALUD Y PENSIÓN',salario_subtotal)
    else:
        salario_a=salario_total
        print('SALARIO TOTAL CON DESCUENTOS Y TRANSPORTE',salario_total)
    print('----------------------')
    print("DIGITE (S) O (s) PARA CONTINUAR")
    print("Y (N) O (n) PARA FINALIZAR")
    respuesta = input("¿DESEA REALIZAR OTRA NOMINA?: ")
    if respuesta == "N" or respuesta == "n":
        print('El proceso ha terminado')
    break