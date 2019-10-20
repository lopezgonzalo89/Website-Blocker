import time
from datetime import datetime as dt

#Hay que modificar el archivo host añadiendo las rutas que quiero bloquear

host = r"C:\Windows\System32\drivers\etc\hosts"

websites_list = {
    "www.facebook.com",
    "facebook.com",
}

from_hour = 9
to_hour = 18

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print("Bloqueado")
        with open(host, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write("127.0.0.1 " + website + "\n")
    else:
        print("Desactivado")
        with open(host, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()       
    time.sleep(1)