import matplotlib.pyplot as plt

def generar_grafica(name,letras,valores):
  figura, cordenadas = plt.subplots()
  cordenadas.bar(letras,valores)
  plt.savefig(f"./img/{name}.png")
  plt.close()

def generar_grafica_pastel(letras,valores):
  figura, cordenada=plt.subplots()
  cordenada.pie(valores,labels=letras)
  cordenada.axis("equal")
  plt.savefig("pie.png")
  plt.close()

if __name__ == "__main__":
  letras=["a","b","c"]
  valores=[20,80,800]
  generar_grafica(letras,valores)
  generar_grafica_pastel(letras,valores)