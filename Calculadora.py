
from tkinter import *
from tkinter import ttk

class numero_de_cartas_validas:
    def __init__(self):
        self.grupo1 =[]
        self.grupo2 =[] 
        self.grupo3 =[]
        self.grupo1_activado=False
        self.grupo2_activado=False
        self.grupo3_activado=False
        self.cartas=0
        


        #print(self.grupo3)
       # print(self.grupo2)
       # print(self.grupo1) 

       #int(self.cartas)%3==0:

    def cartas_validas(self):
        self.cartas=input("Escoja un numero valido de cartas: ")
        if (int(self.cartas)%3==0 and ((int(self.cartas)/6)-(1/2))%2==1) or int(self.cartas)==3 :
            self.agrupacion()
            #print("numero de cartas valido")
        else:
            print("Numero de cartas fuera del dominio: "+self.cartas)

    def agrupacion(self):
        self.grupo1_activado=True
        for num in range(int(self.cartas)):
            num=num+1
            if  self.grupo3_activado==True:
                self.grupo3_activado=False
                self.grupo3.append(num)
               # print(self.grupo3)
                if num == self.cartas:
                    break
                else:
                    self.grupo1_activado=True
            elif  self.grupo2_activado==True:
                self.grupo2_activado=False
                self.grupo2.append(num)
               # print(self.grupo2)
                self.grupo3_activado=True
            elif self.grupo1_activado ==True:
                self.grupo1_activado=False
                self.grupo1.append(num)
               # print(self.grupo1)
                self.grupo2_activado=True
        a=determinar_carta(self.grupo1,self.grupo2,self.grupo3,self.cartas)
        num=0

class determinar_carta:
    def __init__(self,grupo1,grupo2,grupo3,cartas):
        self.grupo1=grupo1
        self.grupo2=grupo2
        self.grupo3=grupo3
        self.grupo1_activado=False
        self.grupo2_activado=False
        self.grupo3_activado=False
        self.cartas=cartas
        self.repeticion=0
        self.lista=[]
        self.string=""
        print("grupo 1")
        print(self.grupo1)
        print("grupo 2")
        print(self.grupo2)
        print("grupo 3")
        print(self.grupo3)
        #print(self.cartas)

        self.num_lanzamientos()
        self.ejecucion()
        self.restulado()

    

    


    def restulado(self):
       x=len(self.lista)/2+0.5
       #print(x)
       print("Tu carta es el numero: "+str(self.lista[int(x-1)]))

    def ejecucion(self):
        for i in range(self.repeticion-1):
            self.lanzamiento()
        self.lanzamiento_final()
    
    def lanzamiento(self):
        #print("###############    Lanzamiento   ###################")
        x=input("¿en que grupo esta su carta?")
        if int(x) == 1:
            self.lista=self.grupo2+self.grupo1+self.grupo3
           # print(self.lista)
        if int(x) == 2:
            self.lista=self.grupo1+self.grupo2+self.grupo3
            #print(self.lista)
        if int(x) == 3:
            self.lista=self.grupo2+self.grupo3+self.grupo1
            #print(self.lista)
        self.agrupacion_lista()
    
    def agrupacion_lista(self):
        print("###############    Lanzamiento   ###################")
        self.grupo1=[]
        self.grupo2=[]
        self.grupo3=[]
        self.grupo1_activado=True
        
        for num in self.lista:
            if  self.grupo3_activado==True:
                self.grupo3_activado=False
                self.grupo3.append(num)
                #print(self.grupo3)
                if num == self.cartas:
                    break
                else:
                    self.grupo1_activado=True
            elif  self.grupo2_activado==True:
                self.grupo2_activado=False
                self.grupo2.append(num)
               # print(self.grupo2)
                self.grupo3_activado=True
            elif self.grupo1_activado ==True:
                self.grupo1_activado=False
                self.grupo1.append(num)
                #print(self.grupo1)
                self.grupo2_activado=True
        print("grupo 1")
        print(self.grupo1)
        print("grupo 2")
        print(self.grupo2)
        print("grupo 3")
        print(self.grupo3)



    def num_lanzamientos(self):
        if int(self.cartas) ==3:
            self.repeticion=1
            print("************se realizara "+str(self.repeticion)+" lanzamientos************ ")
        elif int(self.cartas) >3  and int(self.cartas) <=9:
            self.repeticion=2
            print("************se realizara "+str(self.repeticion)+" lanzamientos************ ")
        elif int(self.cartas) >9  and int(self.cartas) <=27:
            self.repeticion=3
            print("************se realizara "+str(self.repeticion)+" lanzamiento************s ")
        elif int(self.cartas) >27  and int(self.cartas) <=81:
            self.repeticion=4
            print("************se realizara "+str(self.repeticion)+" lanzamientos************ ")

    def lanzamiento_final(self):
        print("###############    Lanzamiento   ###################")
        x=input("¿en que grupo esta su carta?: ")
        if int(x) == 1:
            self.lista=self.grupo2+self.grupo1+self.grupo3
            #print(self.lista)
        if int(x) == 2:
            self.lista=self.grupo1+self.grupo2+self.grupo3
            #print(self.lista)
        if int(x) == 3:
            self.lista=self.grupo2+self.grupo3+self.grupo1
            #print(self.lista)



    


    

    


    


    



    
    


             
                

            





        


