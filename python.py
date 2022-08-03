respuesta = "s" 
while respuesta == "s":
    print('---------NÓMINA---------')
    print("!DIGITE LOS DATOS SIN ESPACIOS¡")
    import re
    bander = True
    while bander:
        nombres = str(input("INGRESE LOS NOMBRES: "))
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
    import re
    bander = True
    while bander:
        documento = str(input("INGRESE EL NÚMERO DE DOCUMENTO: "))
        d = re.findall("[^0-9]",documento)
        if d:
            print("caracteres incorrectos intente de nuevo")
        elif not documento:
            print("quedo en blanco")
        elif len (documento)>35:
            print("se paso del maximo")
        elif len (documento)<5:
            print("muy pocos caracteres")
        else:
            bander = False
    import re
    bander = True
    while bander:
        salario = str(input("INGRESE EL SALARIO: "))
        d = re.findall("[^0-9]",salario)
        if d:
            print("caracteres incorrectos intente de nuevo")
        elif not salario:
            print("quedo en blanco")
        elif len (salario)>15:
            print("se paso del maximo")
        elif len (salario)<5:
            print("muy pocos caracteres")
        else:
            salario = int(salario)
            bander = False
    import re
    bander = True
    while bander:
        dias_trabajados = str(input("INGRESE LOS DIAS TRABAJADOS: "))
        d = re.findall("[^0-9]", dias_trabajados)
        if d:
            print("caracteres incorrectos intente de nuevo")
        elif not dias_trabajados:
            print("quedo en blanco")
        else:
            dias_trabajados = int(dias_trabajados)
            if dias_trabajados>30:
                print("LOS DIAS DEBEN SER MENORES A 30")
            else:
                bander = False
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
    print("Y CUALQUIER OTRA LETRA PARA FINALIZAR")
    respuesta = input("¿DESEA REALIZAR OTRA NOMINA?: ")
file = open("Nomina.txt", "a")
file.write("Bienvenido usuario \n")
file.write("Empleado: " + nombres + apellidos + "\n")
file.write("Documento: " + documento + "\n")
file.write("Su salario es: " + str(salario) + "\n")
file.write("Sus dias trabajados son: " + str(dias_trabajados) + "\n")
file.write("--------------------------------------------------------------------")
