import json
import csv

def preparar_datos_dynamo(ruta_txt, ruta_json):
    datos_json = []
    
    try:
        # Abrimos el archivo de texto
        with open(ruta_txt, mode='r', encoding='utf-8') as archivo_txt:
            # DictReader mapea automáticamente cada fila con los encabezados
            lector = csv.DictReader(archivo_txt)
            
            for fila in lector:
                # Construimos el item casteando los valores numéricos
                item = {
                    "Estado": fila["Estado"], 
                    "Temperatura": float(fila["Temperatura"]),
                    "Humedad": float(fila["Humedad"]),
                    "Costo_Alojamiento": float(fila["Costo_Alojamiento"]),
                    "Costo_Transporte": float(fila["Costo_Transporte"]),
                    "Dias_Promedio": int(fila["Dias_Promedio"]),
                    "Tiempo_Traslado": float(fila["Tiempo_Traslado"])
                }
                datos_json.append(item)
                
        # Guardamos el resultado en un JSON
        with open(ruta_json, 'w', encoding='utf-8') as archivo_json:
            json.dump(datos_json, archivo_json, indent=4, ensure_ascii=False)
            
        print(f"¡Listo! Se generó el archivo '{ruta_json}' con {len(datos_json)} registros listos para DynamoDB.")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_txt}'. Asegúrate de que esté en la misma carpeta.")
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")

# Ejecutamos la función
if __name__ == "__main__":
    preparar_datos_dynamo('Estados.txt', 'estados_dynamodb.json')