#ARCHIVO MAIN.PY DONDE IMPORTAREMOS LA FUNCION DEL  MODULO MOD

'''#FUNCIONES
import utilidades
llaves,valores=utilidades.get_population()
print(llaves,valores)


#VARIABLES
import utilidades
print(utilidades.variable)

#FUNCIONES
import utilidades
BD=[
  {
    "country":"mexico",
    "population":500
  },
  {
    "country":"colombia",
    "population":300
  }
]

resultado=utilidades.population_by_country(BD,"mexico")
print(resultado)'''

#MISMA FUNCION DE MANERA DINAMICA
import utilidades
import charts
import read_csv

def run():
  datos=read_csv.leer_csv("data.csv")
  datos=list(filter(lambda x:x["Continent"]=="South America",datos))
  paises=list(map(lambda x:x["Country/Territory"],datos))
  porcentaje=list(map(lambda x:x["World Population Percentage"], datos))
  charts.generar_grafica_pastel(paises,porcentaje)
  
  
  pais=input("que pais buscas: ")
  resultado=utilidades.population_by_country(datos,pais)
    
  if len(resultado)>0:
    pais=resultado[0]
    llaves,valores=utilidades.get_population(pais)
    charts.generar_grafica(pais["Country/Territory"],llaves,valores)

if __name__ == "__main__":
  run()
