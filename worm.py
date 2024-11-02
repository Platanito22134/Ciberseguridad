import os
import shutil
contador = 0

while contador <= 50:
    shutil.copy2("script.py",f"script-gusano{contador}.py")


#Eliminar archivos que cumplan un patron
for archivo in os.listdir():
    if archivo.startswith("script-gusano") == True:
        os.remove(archivo)