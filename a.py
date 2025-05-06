# =========================
# CALCULADORA BINARIA MANUAL CON CONVERSIÓN A DECIMAL
# =========================

def suma_binaria_manual(a, b):
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
    invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
    print(f"\nComplemento a dos: binario original={binario}, invertido={invertido}")
    resultado = suma_binaria_manual(invertido, '1')
    print(f"Resultado del complemento a dos: {resultado}")
    return resultado


def resta_binaria_manual(a, b):
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


def comparar_binarios(a, b):
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'
    if len(a) > len(b): return 1
    elif len(a) < len(b): return -1
    return 1 if a > b else (-1 if a < b else 0)


def division_binaria_manual(dividendo, divisor):
    if divisor == '0':
        return 'Error: División por cero', None
    dividendo = dividendo.lstrip('0') or '0'
    divisor = divisor.lstrip('0') or '0'
    cociente = ''
    residuo = ''
    print(f"\nDivisión binaria: {dividendo} ÷ {divisor}")
    for bit in dividendo:
        residuo += bit
        residuo = residuo.lstrip('0') or '0'
        if comparar_binarios(residuo, divisor) >= 0:
            residuo = resta_binaria_manual(residuo, divisor)
            cociente += '1'
        else:
            cociente += '0'
        print(f"Residuo parcial: {residuo}, cociente parcial: {cociente}")

    print(f"Resultado final de la división: cociente={cociente}, residuo={residuo}")
    return cociente.lstrip('0') or '0', residuo.lstrip('0') or '0'


def binario_a_decimal(binario):
    decimal = 0
    for i, bit in enumerate(binario[::-1]):
        if bit == '1':
            decimal += 2 ** i
    return decimal


def es_binario(cadena):
    return all(bit in '01' for bit in cadena)


def calculadora_binaria():
    print("\n=== Calculadora de Números Binarios ===\n")

    while True:
        bin1 = input("Ingrese el primer número binario: ").strip()
        if not es_binario(bin1):
            print(" Error: Solo se permiten dígitos 0 y 1.\n")
            continue

        bin2 = input("Ingrese el segundo número binario: ").strip()
        if not es_binario(bin2):
            print(" Error: Solo se permiten dígitos 0 y 1.\n")
            continue

        print("\nSeleccione la operación a realizar:")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")

        opcion = input("Opción (1/2/3/4): ").strip()

        if opcion == '1':
            resultado = suma_binaria_manual(bin1, bin2)
            print(f" Resultado (Suma): {resultado}")
        elif opcion == '2':
            resultado = resta_binaria_manual(bin1, bin2)
            print(f" Resultado (Resta): {resultado}")
        elif opcion == '3':
            resultado = multiplicacion_binaria_manual(bin1, bin2)
            print(f" Resultado (Multiplicación): {resultado}")
        elif opcion == '4':
            cociente, residuo = division_binaria_manual(bin1, bin2)
            if cociente == 'Error: División por cero':
                print(" No se puede dividir entre cero.")
                continue
            print(f" Resultado (División): Cociente = {cociente}, Residuo = {residuo}")
        else:
            print(" Opción no válida. Intenta nuevamente.")
            continue

        # Conversión a decimal
        convertir = input("¿Desea ver el resultado en decimal? (si/no): ").strip().lower()
        if convertir == 's':
            if opcion == '4':
                print(f"➡️ Cociente en decimal: {binario_a_decimal(cociente)}")
                print(f"➡️ Residuo en decimal: {binario_a_decimal(residuo)}")
            else:
                if resultado.startswith('-'):
                    resultado_decimal = binario_a_decimal(resultado[1:])
                    print(f"➡️ Resultado en decimal: -{resultado_decimal}")
                else:
                    print(f"➡️ Resultado en decimal: {binario_a_decimal(resultado)}")

        repetir = input("¿Desea realizar otra operación? (si/no): ").strip().lower()
        if repetir != 's':
            print("\n¡Gracias por usar la calculadora binaria!")
            break


# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora_binaria()
