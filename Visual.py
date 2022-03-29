import tkinter as tk
from tkinter import ttk
from tkinter import *
from Calculadora import numero_de_cartas_validas
from Calculadora import determinar_carta



#class Application(ttk.Frame):
   # def __init__(self, main_window):
       # super().__init__(main_window)
     #   main_window.title("Posicionar elementos en Tcl/Tk")
        
     #   main_window.configure(width=5, height=7)
        # Ignorar esto por el momento.
     #   self.place(relwidth=1, relheight=1)

      #  self.button1 = ttk.Button(self, text="Grupo 1")
      #  self.button1.place(x=100, y=550)

      #  self.button2 = ttk.Button(self, text="Grupo 2")
     #   self.button2.place(x=600, y=550)

   #     self.button3 = ttk.Button(self, text="Grupo 3", command=self.getTextInput)
      #  self.button3.place(x=1100, y=550)

      #  label = tk.Label(self, text="Welcome to StackHowTo!")
     #   label.config(bg="yellow")
     #   label.place(x=1100, y=300)

  #  def getTextInput(self): 
     #   pass

    


#main_window = tk.Tk()
#app = Application(main_window)
#app.mainloop()

class grupos():
    def __init__(self):
        self.a=numero_de_cartas_validas()
        

    def primer_grupo(self):
        self.a.grupo1
        for i in  self.a.grupo1: 
            print(i)
            print("#############")







    