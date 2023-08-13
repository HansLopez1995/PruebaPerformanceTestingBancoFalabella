# Archivo Python para Generación de Data de Prueba
import csv
import random
import string

# Se crea un método para generar strings aleatorios que recibe como parámetros largo mínimo y máximo
def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Se crea un método para generar strings alfanumericos aleatorios que recibe como parámetros el largo
def generate_random_alphanumeric_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Se crean y se instancian las variables con las funciones definidas previamente 
def generate_data():
    id = random.randint(1, 1000000)
    username = generate_random_string(3, 15)
    first_name = generate_random_string(3, 15)
    last_name = generate_random_string(3, 15)
    email = f"{username}{first_name}@gmail.com"
    password = generate_random_alphanumeric_string(10)
    phone = random.randint(100000000, 999999999)
    userStatus = 0
    
    # Se retorna todo dentro de una lista
    return [id, username, first_name, last_name, email, password, phone, userStatus]

# Función que pregunta por consola, la cantidad de registros que se quieren generar
def main():
    cantidad_registros = int(input("Ingrese la cantidad de registros que desea crear: "))

    # 
    file_name = "data.csv"
    
    # Se utiliza el método nativo de python para abrir archivos, pasandole el parámetro mode="w" de Write (Escritura)
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Se definen las cabeceras en la primera fila
        writer.writerow(["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"])
        
        # Ciclo que recibe como parámetro la cantidad de registros a generar
        for _ in range(cantidad_registros):
            data = generate_data()
            writer.writerow(data)
    
    print(f"Se han generado {cantidad_registros} registros en el archivo '{file_name}'.")

if __name__ == "__main__":
    main()