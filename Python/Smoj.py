recomendaciones = [
 ["Pad thai", "Costillar cantones", "Lasagna"],
 ["Ceviche", "Lomo saltado", "Pastel de choclo"],
 ["Pastel de choclo", "Cazuela", "Ceviche"],
 ["Lasagna"],
 ["Fettuccine al pesto", "Lasagna"],
 ["Ceviche", "Pastel de choclo", "Lasagna", "Cazuela"]
 ]

#Item 1
def mas_popular(lista):
     plato_lista=[]
     for elemento in lista:
          for plato in elemento:
               plato_lista.append(plato)

     plato_lista.sort()
     contador=0
     for comida in plato_lista:
          popular=plato_lista.count(comida)
          #El if guarda el más recomendado
          if popular>contador:
               contador=popular
               plato_popular=comida
     return [plato_popular,contador]
#Print de la tarea
print(mas_popular(recomendaciones))

#Item 2
def similares(plato_base, recomendaciones):
     similitud=[]
     for elemento in recomendaciones:#recorrer matriz y dejar como listas
          if plato_base in elemento: #si el plato base esta en las listas     
               for plato_similar in elemento: #para dejar los platos solos y dejarlos en una sola lista nueva
                    similitud.append(plato_similar)
                    if plato_base in similitud:#para eliminar si el plato base esta en la nueva lista
                         similitud.remove(plato_base)
     similitud.sort()
     contador=0
     similitudes=[]
     for comida in similitud:
          popular=similitud.count(comida)
          if popular>contador:
               contador=popular
               plato_popular=comida
               similitudes.append(plato_popular)
          contador=1 #Para no considerar casos de 1 recomendacion 
          popular=1
          for rep in similitudes:
               while rep in similitud:
                    similitud.remove(rep)
          else:
               resto=[]
               for resto_platos in similitud:
                    if resto_platos not in similitudes:
                         resto.append(resto_platos)
     resto.reverse()
     for n in resto:
          similitudes.insert(0,n)                 
          
     similitudes.reverse()
     return similitudes

#Print de la tarea
print(similares("Ceviche", recomendaciones))

