from cure_gps_data import CureGPS

def main():
    # 1. Crear instancia
    gps = CureGPS()
    
    # 2. Limpiar cualquier dato previo
    gps.clean_data()
    
    # 3. Obtener y setear datos desde los servicios gRPC
    gps.set_data()
    
    # 4. Calcular buckets de carga (shovels → buckets)
    gps.generate_buckets()
    
    # 5. Interpolar rutas de los camiones y obtener el máximo conteo
    max_count = gps.generate_truck_gps()
    print(f"Máximo de puntos interpolados por camión: {max_count}")

if __name__ == "__main__":
    main()
