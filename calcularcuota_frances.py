# Definición de la función calcular_cuota_francesa
def calcular_cuota_francesa(principal, tasa_interes_anual, plazo_en_meses):
    tasa_interes_mensual = tasa_interes_anual / 12
    cuota = (principal * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual)**(-plazo_en_meses))
    return cuota

# Parámetros del préstamo
principal = 1000000  # Monto del préstamo
tasa_interes_anual = 0.54  # Tasa de interés anual (54%)
plazo_en_meses = 60  # Plazo del préstamo en meses

# Calcular la cuota mensual
cuota_mensual = calcular_cuota_francesa(principal, tasa_interes_anual, plazo_en_meses)

# Imprimir la cuota mensual
print(f"La cuota mensual para un préstamo de {principal} con una tasa de interés del {tasa_interes_anual*100}% a {plazo_en_meses} meses es: {cuota_mensual:.2f}")
