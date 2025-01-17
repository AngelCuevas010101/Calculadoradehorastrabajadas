print('Bienvenido al software de calculo de horas')

while True:
    # Solicitar horas trabajadas y horas extra
    horas = int(input('Horas Trabajadas: '))
    tarifa = 19.0 
    extra = int(input('Horas Extra: '))
    tarifa_extra = 28.0

    # Calcular salarios
    salario = horas * tarifa
    salario_extra = extra * tarifa_extra
    salario_total = salario + salario_extra

    # Calcular salario después de impuestos
    impuestos = 20 / 100  # Convertir porcentaje a decimal
    salario_neto = salario_total * (1 - impuestos)

    # Mostrar resultados
    print(f'Salario bruto: ${salario_total:.2f}')
    print(f'Salario después de impuestos: ${salario_neto:.2f}')

    # Preguntar si el usuario desea realizar otro cálculo
    continuar = input('¿Desea realizar otro cálculo? (s/n): ').strip().lower()
    if continuar != 's':
        print('Gracias por usar el software. ¡Adiós!')
        break
