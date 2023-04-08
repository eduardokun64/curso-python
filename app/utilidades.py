#FUNCION DENTRO DEL ARCHIVO MOD.PY

#FUNCION
def get_population(pais):
  poblacion_dic={
    "2022":int(pais["2022 Population"]),
    "2020":int(pais["2020 Population"]),
    "2015":int(pais["2015 Population"]),
    "2010":int(pais["2010 Population"]),
    "2000":int(pais["2000 Population"]),
    "1990":int(pais["1990 Population"]),
    "1980":int(pais["1980 Population"]),
    "1970":int(pais["1970 Population"])
  }
  
  return poblacion_dic.keys(), poblacion_dic.values()

def population_by_country(datos,pais):
  result=list(filter(lambda item : item["Country/Territory"]==pais,datos))
  return result
  

#VARIABLES
variable="hola"