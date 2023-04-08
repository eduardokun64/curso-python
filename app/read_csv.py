import csv 

def leer_csv(fuente):
  with open(fuente,"r") as filecsv:
    lector = csv.reader(filecsv,delimiter=",")
    claves = next(lector)
    datos=[]
    for fila in lector:
      iterable = zip(claves,fila)
      diccionario={llave:valor for llave,valor in iterable} 
      datos.append(diccionario)
    return datos  
if __name__ == "__main__":
  datos=leer_csv("data.csv")
  print(datos[0])