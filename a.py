"""
Calculadora binaria hecha manualmente con funciones para sumar, restar, multiplicar
y convertir entre binario y decimal sin usar funciones automáticas.
"""

def suma_binaria_manual(a, b):
    """
    Realiza la suma manual de dos números binarios.
    Se igualan las longitudes de los binarios, se suman bit a bit de derecha a izquierda,
    teniendo en cuenta el acarreo. Se muestra cada paso de la suma.
    """
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    resultado = ''
    acarreo = '0'

    print(f"\nSuma binaria: {a} + {b}")
    for i in range(max_len - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + int(acarreo)
        bit = str(total % 2)
        acarreo = str(total // 2)
        resultado = bit + resultado
        print(f"Paso {max_len - i}: bit1={a[i]}, bit2={b[i]}, acarreo={acarreo}, resultado parcial={resultado}")

    if acarreo == '1':
        resultado = '1' + resultado
        print(f"Acarreo final: {acarreo}, resultado final={resultado}")

    return resultado.lstrip('0') or '0'


def complemento_dos(binario):
    """
    Calcula el complemento a dos de un número binario.
    Primero invierte cada bit (0 por 1 y 1 por 0), y luego le suma 1.
    """
    invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
    print(f"\nComplemento a dos: binario original={binario}, invertido={invertido}")
    resultado = suma_binaria_manual(invertido, '1')
    print(f"Resultado del complemento a dos: {resultado}")
    return resultado


def resta_binaria_manual(a, b):
    """
    Realiza la resta binaria manual de a - b.
    Convierte b a complemento a dos y lo suma a a.
    Si el resultado tiene más bits que los originales, es positivo.
    Si no, el resultado es negativo y se convierte a su complemento a dos.
    """
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    print(f"\nResta binaria: {a} - {b}")
    b_comp2 = complemento_dos(b)
    suma = suma_binaria_manual(a, b_comp2)

    if len(suma) > max_len:
        resultado = suma[-max_len:].lstrip('0') or '0'
    else:
        resultado = '-' + complemento_dos(suma.zfill(max_len))

    print(f"Resultado de la resta: {resultado}")
    return resultado


def multiplicacion_binaria_manual(a, b):
    """
    Realiza la multiplicación binaria manual.
    Por cada bit 1 en b (de derecha a izquierda), se suma a desplazamientos del valor de a.
    Se muestra el proceso paso a paso.
    """
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'
    resultado = '0'
    b_reversed = b[::-1]

    print(f"\nMultiplicación binaria: {a} * {b}")
    for i, bit in enumerate(b_reversed):
        if bit == '1':
            parcial = a + '0' * i
            print(f"Paso {i + 1}: parcial={parcial}")
            resultado = suma_binaria_manual(resultado, parcial)
            print(f"Resultado acumulado: {resultado}")

    print(f"Resultado final de la multiplicación: {resultado}")
    return resultado


def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal recorriendo de derecha a izquierda,
    sumando potencias de 2 en las posiciones donde el bit es 1.
    """
    decimal = 0
    print(f"\nTransformación de binario a decimal: {binario}")
    for i, bit in enumerate(binario[::-1]):
        if bit == '1':
            valor = 2 ** i
            decimal += valor
            print(f"Bit: {bit} (posición {i}) -> 2^{i} = {valor}, suma parcial = {decimal}")
        else:
            print(f"Bit: {bit} (posición {i}) -> 0, suma parcial = {decimal}")
    print(f"Resultado final en decimal: {decimal}")
    return decimal


def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario dividiendo sucesivamente entre 2
    y tomando los residuos hasta que el cociente sea 0.
    """
    binario = ''
    print(f"\nTransformación de decimal a binario: {decimal}")
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        print(f"Residuo: {residuo}, cociente: {decimal // 2}, binario parcial: {binario}")
        decimal //= 2
    print(f"Resultado final en binario: {binario}")
    return binario or '0'


def es_binario(cadena):
    """
    Verifica si una cadena representa un número binario válido (solo contiene 0s y 1s).
    """
    return all(bit in '01' for bit in cadena)


def calculadora_binaria():
    """
    Muestra un menú interactivo para realizar operaciones con números binarios.
    Permite sumar, restar, multiplicar y convertir entre binario y decimal.
    """
    print("\n=== Calculadora de Números Binarios ===\n")

    while True:
        print("\nSeleccione la operación a realizar:")
        print("1) Suma de binarios")
        print("2) Resta de binarios")
        print("3) Multiplicación de binarios")
        print("4) Convertir binario a decimal")
        print("5) Convertir decimal a binario")

        opcion = input("Opción (1/2/3/4/5): ").strip()

        if opcion in ['1', '2', '3']:
            bin1 = input("Ingrese el primer número binario: ").strip()
            if not es_binario(bin1):
                print("Error: Solo se permiten dígitos 0 y 1.\n")
                continue

            bin2 = input("Ingrese el segundo número binario: ").strip()
            if not es_binario(bin2):
                print("Error: Solo se permiten dígitos 0 y 1.\n")
                continue

            if opcion == '1':
                resultado = suma_binaria_manual(bin1, bin2)
                print(f"Resultado (Suma): {resultado}")
            elif opcion == '2':
                resultado = resta_binaria_manual(bin1, bin2)
                print(f"Resultado (Resta): {resultado}")
            elif opcion == '3':
                resultado = multiplicacion_binaria_manual(bin1, bin2)
                print(f"Resultado (Multiplicación): {resultado}")

        elif opcion == '4':
            binario = input("Ingrese el número binario a convertir: ").strip()
            if not es_binario(binario):
                print("Error: Solo se permiten dígitos 0 y 1.\n")
                continue
            decimal = binario_a_decimal(binario)
            print(f"Resultado en decimal: {decimal}")

        elif opcion == '5':
            try:
                decimal = int(input("Ingrese el número decimal a convertir: ").strip())
                if decimal < 0:
                    print("Error: Solo se permiten números decimales positivos.\n")
                    continue
                binario = decimal_a_binario(decimal)
                print(f"✅ Resultado en binario: {binario}")
            except ValueError:
                print("Error: Entrada no válida. Ingrese un número decimal.\n")
                continue

        else:
            print("Opción no válida. Intenta nuevamente.")
            continue

        repetir = input("¿Desea realizar otra operación? (si/no): ").strip().lower()
        if repetir != 's':
            print("\n¡Gracias por usar la calculadora binaria!")
            break


if __name__ == "__main__":
    calculadora_binaria()
