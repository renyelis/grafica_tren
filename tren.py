from tkinter import *

#...................
# variables globales
#...................
x = 560
y = 560

#..................
# ventana principal
#..................
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("600x600")
ventana_principal.config(bg="white")

#.....................
# frame de graficacion
#.....................
frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg="pink",width=580, height=580)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion,width=x, height=y)
c.config(bg="black")
c.place(x=10,y=10)

# dibujo del tren
paso_g = c.create_oval(x/2-200,y/2+100,x/2-160,y/2+40, fill= "pink")
paso_g = c.create_oval(x/2-200,y/2+110,x/2-160,y/2+40, fill= "pink")
paso_1 = c.create_rectangle(x/2-35,y/2-30,x/2+30,y/2+30, fill= "MediumOrchid4")
paso_2 = c.create_rectangle(x/2-25,y/2-18,x/2+20,y/2+18, fill= "MediumOrchid2")
paso_3 = c.create_rectangle(x/2-50,y/2-40,x/2+45,y/2-20, fill= "PaleGreen1")
paso_4 = c.create_rectangle(x/2-45,y/2-50,x/2+40,y/2-40, fill= "SeaGreen3")
paso_5 = c.create_rectangle(x/2-150,y/2+30,x/2+40,y/2+120, fill= "SeaGreen4")
paso_6=c.create_rectangle(x/2-130,y/2-10,x/2-100, y/2+30, fill="red")
paso_7=c.create_rectangle(x/2-135,y/2-10,x/2-95, y/2-20, fill="blue")
paso_8 = c.create_rectangle(x/2-160,y/2+35,x/2-150,y/2+115, fill= "orange")
paso_9 = c.create_rectangle(x/2-180,y/2+30,x/2-160,y/2+120, fill= "green")
texto_4 = c.create_text(x/2-50, y/2+70, anchor="center", tex="Renyelis Luyando", font=("Arial", 10, "bold"), fill="blue", activefill="yellow")
paso_g1 = c.create_oval(x/2-25,y/2+100,x/2+25,y/2+150, fill= "blue")
paso_g2 = c.create_oval(x/2-85,y/2+100,x/2-35,y/2+150, fill= "blue")
paso_g3 = c.create_oval(x/2-145,y/2+100,x/2-95,y/2+150, fill= "blue")
paso_chiq = c.create_oval(x/2-30,y/2-18,x/2+25,y/2+18, fill= "white")


ventana_principal.mainloop()