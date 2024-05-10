
from decimal import Decimal, ROUND_HALF_UP

def calcular_cuota_francesa(principal, tasa_interes_anual, plazo_en_meses):
    tasa_interes_mensual = Decimal(tasa_interes_anual) / 12
    cuota = (principal * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual)**(-plazo_en_meses))
    return cuota

def generar_tabla_amortizacion(principal, tasa_interes_anual, plazo_en_meses):
    saldo_pendiente = Decimal(principal)
    cuota_mensual = calcular_cuota_francesa(principal, tasa_interes_anual, plazo_en_meses)
    tasa_interes_mensual = Decimal(tasa_interes_anual) / 12
    tabla = []

    for mes in range(1, plazo_en_meses + 1):
        intereses = saldo_pendiente * tasa_interes_mensual
        amortizacion = cuota_mensual - intereses
        saldo_pendiente -= amortizacion
        fila = [mes, cuota_mensual.quantize(Decimal('.01'), rounding=ROUND_HALF_UP), 
                intereses.quantize(Decimal('.01'), rounding=ROUND_HALF_UP), 
                amortizacion.quantize(Decimal('.01'), rounding=ROUND_HALF_UP), 
                saldo_pendiente.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)]
        tabla.append(fila)
    
    return tabla

# Aqui se ingresan los montos a calcular, primero como principal el monto del prestamo
#luego la tasa de interes y por ultimo la cantidad de meses 
principal = 6330000  
tasa_interes_anual = 0.54  
plazo_en_meses = 60  

tabla = generar_tabla_amortizacion(principal, tasa_interes_anual, plazo_en_meses)

# Imprimir la tabla de amortización
print("Mes\tCuota\tIntereses\tAmortización\tSaldo Pendiente")
for fila in tabla:
    print("\t".join(map(str, fila)))



