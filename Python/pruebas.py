#Item 1
def ganadores_tipo_torneo(nombre_archivo, tipo, año):
     archivo= open(nombre_archivo)
     d={}
     for linea in archivo:
          l=linea.strip().split(";")
     #año;perdedor;sets_perdedor;ronda;tipo;torneo;ganador;sets_ganador.
          if l[4]==tipo:
               if l[3]== "The Final":
                    if l[0]== str(año):
                         marca="{0}-{1}"
                         marcador=marca.format(l[7],l[2])
                         if l[6] not in d:
                              d[l[6]]=[]
                         d[l[6]].append([l[1],l[5],marcador])#lista de lista al hacer append
     archivo.close()
     return d
#Ejemplo tarea
print(ganadores_tipo_torneo("datos_atp.csv","Grand Slam",2010))
#print(ganadores_tipo_torneo("datos_atp.csv","Masters",2005))

#Item 2
def construir_resumen(nombre_archivo, año1, año2):
     archivo= open(nombre_archivo)
     d1={}
     d2={}
     arch= "resumen_ATP_"+str(año1)+"-"+str(año2)+".txt"
     arch= open(arch,"w")
     arch.write("Asosiación de Tenis de Pythonia"+"\n")
     arch.write("Resumen "+str(año1)+"-"+str(año2)+"\n")
     arch.write("\n")
     arch.write("Jugadores con más partidos ganados en "+str(año1)+":\n")
     arch.write("\n")
     for linea in archivo:
          l=linea.strip().split(";")
     #año;perdedor;sets_perdedor;ronda;tipo;torneo;ganador;sets_ganador.
          partidos1=[]
          triunfoslista1=[]
          partidos2=[]
          triunfoslista2=[]
          if l[0]==str(año1):
               if l[6] not in d1:
                    d1[l[6]]=0
               d1[l[6]]+=1
         #d1= {'Gasquet R.': 2, 'Krajicek R.': 11, .....
          if l[0]==str(año2):
               if l[6] not in d2:
                    d2[l[6]]=0
               d2[l[6]]+=1
         #d2= {'Spadea V.': 39, 'Dent T.': 28,
               
     for llave1 in d1: #Gasquet
          conteo1=d1[llave1]
          triunfoslista1.append([d1[llave1],llave1]) #[['Gasquet',2], ['Krajicek R.',11],...
          triunfoslista1.sort()
          triunfoslista1.reverse() #[[73, 'Federer R.'], [71, 'Roddick A.']
          triunfoslista1=triunfoslista1[:10]
     for llave2 in d2:
          conteo2=d2[llave2]
          triunfoslista2.append([d2[llave2],llave2])
          triunfoslista2.sort()
          triunfoslista2.reverse()
          triunfoslista2=triunfoslista2[:10]
     j=1
     i=1
     cantidadjugadores=[]
     while i<10: 
          for partidos1 in triunfoslista1:
               s="{0}. {1} con {2} triunfos"
               f=s.format(i,partidos1[1],partidos1[0])
               i+=1
               arch.write(f+"\n")
               if partidos1[1] not in cantidadjugadores:
                    cantidadjugadores.append(partidos1[1])
     arch.write("\n")
     arch.write("Jugadores con más partidos ganados en "+str(año2)+":\n")
     arch.write("\n")
     while j<10:
          for partidos2 in triunfoslista2: #[73, 'Federer R.']
               s="{0}. {1} con {2} triunfos"
               f=s.format(j,partidos2[1],partidos2[0])
               j+=1
               arch.write(f+"\n")
               if partidos2[1] not in cantidadjugadores:
                    cantidadjugadores.append(partidos2[1])
     
     cantidadjugadores=len(cantidadjugadores)
     archivo.close()
     arch.close()
     return cantidadjugadores
#Ejemplo tarea
print(construir_resumen("datos_atp.csv", 2003, 2004))



                
            
            
        

        
                
                
    

      
        
