def exchange_money(amount, rate_from, rate_to):
    usd = amount / rate_from
    result = usd * rate_to
    return result


# Tasas basadas en: 1 USD = X moneda (valores aproximados)
rates = {
    "USD": 1.0,
    "DOP": 58.0,     # Peso dominicano
    "EUR": 0.92,     # Euro
    "JPY": 150.0,    # Yen japonés
    "MXN": 17.0,     # Peso mexicano
    "COP": 4000.0    # Peso colombiano
}

print("=== Calculadora de Divisas ===")
print("Monedas disponibles:", list(rates.keys()))

while True:
    # Entrada de datos
    from_currency = input("¿Qué moneda tienes?: ").upper()
    to_currency = input("¿A qué moneda quieres cambiar?: ").upper()

    # Validación de moneda
    if from_currency not in rates or to_currency not in rates:
        print("❌ Moneda no válida. Intenta de nuevo.\n")
        continue

    try:
        amount = float(input("¿Cuánto dinero tienes?: "))
    except:
        print("❌ Ingresa un número válido.\n")
        continue

    # Conversión
    result = exchange_money(amount, rates[from_currency], rates[to_currency])

    print(f"💰 Resultado: {round(result, 2)} {to_currency}\n")

    # Preguntar si desea continuar
    repeat = input("¿Quieres hacer otra conversión? (s/n): ").lower()
    if repeat != "s":
        print("👋 Gracias por usar la calculadora")
        break