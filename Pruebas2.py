def procesar_entregas(nombre_archivo):
     archivo=open(nombre_archivo)
     d={}


     for linea in archivo:
          l=linea.strip().split(";")
          #equipo;problema;entregas;veredicto;tiempo_de_resolucion
          equipo=l[0]
          problema=l[1]
          entregas=int(l[2])
          veredicto=l[3]

          
          if veredicto=="yes":
               tiempo=int(l[4])
               if equipo not in d:
                    d[equipo]=[]
               d[equipo].append([problema,tiempo])
               d[equipo].sort()
     
     
     archivo.close()

     return d

#print(procesar_entregas('entregas.txt'))

def resumen(nombre_archivo):
     archivo=open(nombre_archivo)
     d={}
     f={}
     lorden=[]
     for linea in archivo:
          l=linea.strip().split(";")
          #equipo;problema;entregas;veredicto;tiempo_de_resolucion
          equipo=l[0]
          problema=l[1]
          entregas=int(l[2])
          veredicto=l[3]
     
          if veredicto=="yes":
               tiempo=int(l[4])
               if equipo not in d:
                    d[equipo]=[]
               d[equipo].append([problema,tiempo])
               d[equipo].sort()

          
          if problema not in f:
               f[problema]=0
          f[problema]+=1
               
          
     tt=0
     for llaved in d:
          resumen="{}.txt".format(llaved)
          hechos=len(d[llaved])
          salida=open(resumen,"w")
          salida.write("Resueltos: "+str(hechos)+"\n")
          for problema, tiempo in d[llaved]:
               tt+=tiempo
          salida.write("Tiempo total: "+str(tt)+"\n")    
          for problema, tiempo in d[llaved]:
               salida.write(problema+" "+str(tiempo)+"\n")
               
     for problema in f:
          lorden.append([f[problema],problema])
     lorden.sort()
     lorden.reverse()
     
     texto="El problema {} fue resuelto por {} equipos.\n"
     resumenf=open("estadisticas.txt","w")
     for l in lorden:
          resumenf.write(texto.format(l[1],l[0]))
     archivo.close()
     resumenf.close()
          
     return lorden
print(resumen("entregas.txt"))
               
               






















               
          
