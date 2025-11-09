# Programa para aproximar la disminución de un contaminante en un cuerpo de agua
# Usando el método numérico de Euler para la ecuación:
#       dC/dt = -k * C
#
# Este código permite usar tiempos totales y tamaños de paso arbitrarios.


def main():
    try:
        C0 = float(input("Ingrese la concentración inicial C0 (mg/L) [ej. 80]: "))
        k = float(input("Ingrese la constante de degradación k (1/día) [ej. 0.12]: "))
        totalDays = float(input("Ingrese el tiempo total a simular (días) [ej. 30]: "))
        dt = float(input("Ingrese el tamaño de paso dt (días) [ej. 1 o 0.5]: "))

    except ValueError:
        print("Error: entrada inválida. Use números reales (ej. 0.12).")
        return

    # Validaciones básicas
    if C0 < 0 or k < 0 or totalDays <= 0 or dt <= 0:
        print("Error: asegúrese de que C0 >= 0, k >= 0, tiempo total > 0 y dt > 0.")
        return

    if dt > totalDays:
        print("Aviso: dt es mayor que el tiempo total. Se realizará una sola iteración.")

    # Número de pasos enteros
    steps = int(totalDays // dt)

    # Resto para completar exactamente totalDays
    remainder = totalDays - steps * dt
    hasRemainder = remainder > 1e-12

    print("\nSimulación Método de Euler")
    print("--------------------------")
    print(f"C0 = {C0:.6f} mg/L, k = {k:.6f} 1/día, tiempo total = {totalDays:.6f} días, dt = {dt:.6f} días\n")

    print("Tiempo (días)\tConcentración (mg/L)")
    print("-------------------------------------")

    C = C0
    t = 0.0
    print(f"{t:.6f}\t\t{C:.6f}")

    # Iteraciones regulares
    for i in range(1, steps + 1):
        C = C - (k * C * dt)
        t = i * dt
        print(f"{t:.6f}\t\t{C:.6f}")

    # Paso final ajustado si el tiempo no es múltiplo exacto de dt
    if hasRemainder:
        C = C - (k * C * remainder)
        t = totalDays
        print(f"{t:.6f}\t\t{C:.6f}")

if __name__ == "__main__":
    main()
