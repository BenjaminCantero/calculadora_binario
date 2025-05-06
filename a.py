"""
Calculadora binaria hecha manualmente con funciones para sumar, restar, multiplicar
y convertir entre binario y decimal sin usar funciones automáticas.
"""

from typing import Dict, List, Union


def suma_binaria_manual(a: str, b: str) -> str:
    """
    Realiza la suma manual de dos números binarios.

    Args:
        a (str): Primer número binario.
        b (str): Segundo número binario.

    Returns:
        str: Resultado de la suma binaria.

    Raises:
        ValueError: Si los números no son binarios.
    """
    # Calcula la longitud máxima entre los dos números binarios
    max_len = max(len(a), len(b))

    # Rellena con ceros a la izquierda para igualar las longitudes de ambos números
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Inicializa el resultado como una cadena vacía y el acarreo como '0'
    resultado = ''
    acarreo = '0'

    # Imprime los números binarios que se van a sumar
    print(f"\nSuma binaria: {a} + {b}")

    # Recorre los números binarios de derecha a izquierda
    for i in range(max_len - 1, -1, -1):
        # Suma los bits actuales y el acarreo
        total = int(a[i]) + int(b[i]) + int(acarreo)

        # Calcula el bit resultante (0 o 1) usando el módulo 2
        bit = str(total % 2)

        # Calcula el nuevo acarreo (0 o 1) usando la división entera por 2
        acarreo = str(total // 2)

        # Agrega el bit resultante al inicio del resultado
        resultado = bit + resultado

        # Imprime el estado actual del cálculo en este paso
        print(f"Paso {max_len - i}: bit1={a[i]}, bit2={b[i]}, acarreo={acarreo}, resultado parcial={resultado}")

    # Si al final hay un acarreo, se agrega al inicio del resultado
    if acarreo == '1':
        resultado = '1' + resultado
        print(f"Acarreo final: {acarreo}, resultado final={resultado}")

    # Devuelve el resultado eliminando ceros iniciales, o '0' si el resultado está vacío
    return resultado.lstrip('0') or '0'


def complemento_dos(binario: str) -> str:
    """
    Calcula el complemento a dos de un número binario.

    Args:
        binario (str): Cadena binaria.

    Returns:
        str: Complemento a dos del binario.
    """
    # Invierte los bits del número binario (complemento a uno)
    invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
    print(f"\nComplemento a dos: binario original={binario}, invertido={invertido}")

    # Suma 1 al complemento a uno para obtener el complemento a dos
    resultado = suma_binaria_manual(invertido, '1')
    print(f"Resultado del complemento a dos: {resultado}")

    return resultado


def resta_binaria_manual(a: str, b: str) -> str:
    """
    Realiza la resta binaria manual de a - b.

    Args:
        a (str): Minuendo en binario.
        b (str): Sustraendo en binario.

    Returns:
        str: Resultado de la resta binaria.
    """
    # Calcula la longitud máxima entre los dos números binarios
    max_len = max(len(a), len(b))

    # Rellena con ceros a la izquierda para igualar las longitudes de ambos números
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Imprime los números binarios que se van a restar
    print(f"\nResta binaria: {a} - {b}")

    # Calcula el complemento a dos del sustraendo
    b_comp2 = complemento_dos(b)

    # Suma el minuendo con el complemento a dos del sustraendo
    suma = suma_binaria_manual(a, b_comp2)

    # Si el resultado tiene más bits que el minuendo, descarta el bit extra
    if len(suma) > max_len:
        resultado = suma[-max_len:].lstrip('0') or '0'
    else:
        # Si no hay bit extra, calcula el complemento a dos del resultado
        resultado = '-' + complemento_dos(suma.zfill(max_len))

    # Imprime el resultado final de la resta
    print(f"Resultado de la resta: {resultado}")
    return resultado


def multiplicacion_binaria_manual(a: str, b: str) -> str:
    """
    Realiza la multiplicación binaria manual.

    Args:
        a (str): Primer número binario.
        b (str): Segundo número binario.

    Returns:
        str: Resultado de la multiplicación binaria.
    """
    # Elimina ceros iniciales de ambos números binarios
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'

    # Inicializa el resultado como '0'
    resultado = '0'

    # Invierte el segundo número binario para recorrerlo de derecha a izquierda
    b_reversed = b[::-1]

    # Imprime los números binarios que se van a multiplicar
    print(f"\nMultiplicación binaria: {a} * {b}")

    # Recorre cada bit del segundo número binario
    for i, bit in enumerate(b_reversed):
        if bit == '1':
            # Desplaza el primer número binario a la izquierda según la posición del bit actual
            parcial = a + '0' * i
            print(f"Paso {i + 1}: parcial={parcial}")

            # Suma el resultado acumulado con el parcial
            resultado = suma_binaria_manual(resultado, parcial)
            print(f"Resultado acumulado: {resultado}")

    # Imprime el resultado final de la multiplicación
    print(f"Resultado final de la multiplicación: {resultado}")
    return resultado


def binario_a_decimal(binario: str) -> int:
    """
    Convierte un número binario a decimal.

    Args:
        binario (str): Cadena binaria.

    Returns:
        int: Representación decimal.
    """
    # Inicializa el resultado decimal en 0
    decimal = 0

    # Imprime el número binario que se va a convertir
    print(f"\nTransformación de binario a decimal: {binario}")

    # Recorre cada bit del número binario de derecha a izquierda
    for i, bit in enumerate(binario[::-1]):
        if bit == '1':
            # Calcula el valor del bit actual como una potencia de 2
            valor = 2 ** i
            decimal += valor
            print(f"Bit: {bit} (posición {i}) -> 2^{i} = {valor}, suma parcial = {decimal}")
        else:
            print(f"Bit: {bit} (posición {i}) -> 0, suma parcial = {decimal}")

    # Imprime el resultado final en decimal
    print(f"Resultado final en decimal: {decimal}")
    return decimal


def decimal_a_binario(decimal: int) -> str:
    """
    Convierte un número decimal a binario.

    Args:
        decimal (int): Número decimal.

    Returns:
        str: Representación binaria.
    """
    # Inicializa el resultado binario como una cadena vacía
    binario = ''

    # Imprime el número decimal que se va a convertir
    print(f"\nTransformación de decimal a binario: {decimal}")

    # Divide el número decimal sucesivamente entre 2
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        print(f"Residuo: {residuo}, cociente: {decimal // 2}, binario parcial: {binario}")
        decimal //= 2

    # Imprime el resultado final en binario
    print(f"Resultado final en binario: {binario}")
    return binario or '0'


def es_binario(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número binario válido.

    Args:
        cadena (str): Cadena a verificar.

    Returns:
        bool: True si es binaria, False en caso contrario.
    """
    # Verifica que todos los caracteres de la cadena sean '0' o '1'
    return all(bit in '01' for bit in cadena)


def calculadora_binaria() -> None:
    """
    Muestra un menú interactivo para realizar operaciones con números binarios.
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
                print(f"Resultado en binario: {binario}")
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
