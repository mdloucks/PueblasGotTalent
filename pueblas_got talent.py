from tkinter import *
from tkinter import messagebox


metricas=[1,2,3,4,5,6,7]
Cal_juez=0

def pueblasGT(valores):
	raiz = Tk()
	raiz.title("Puebla's got talent")



	my_frame=LabelFrame(raiz,text="Buscador", bg="black",)
	my_frame.grid(row=0,column=0)

	logo=PhotoImage(file="images/logo_talent.png")
	logotipo=Label(my_frame,image=logo).grid(row=0, column=2,padx=1, pady=1)

	Cal_juez=Promedio(valores,metricas)
	Label(my_frame, text="", background="black" ).grid(row=1, column=2)
	Label(my_frame, text="aasssssssssssss", font=("Arial", 17),background="black" ).grid(row=1, column=8)
	
	Label(my_frame, text="BIENVENIDO A PUEBLAS GOT TALENT", foreground="white", background="black",font=("Arial", 17)).grid(row=2, column=2)
	Calificacion=Label(my_frame, text=Cal_juez, foreground="white", background="black",font=("Arial", 17)).grid(row=3, column=2)

	jugment=show_image(my_frame,Cal_juez)
	simon=Label(my_frame,image=jugment).grid(row=6, column=0,padx=1, pady=1)

	raiz.mainloop()

############################################################Funcion de calificacion de los datos 
def Promedio(original, comparar):
	cal=original[1]
	contador=0
	for x in range(7):
		if original[x]==comparar[x]:
			contador=contador+1

	return contador
##########################calificacion grafica 

def show_image(raiz, cal):
	if cal==1:
		simon_mood=PhotoImage(file="images/simons_reaction/1.png")
	elif cal==0:
		simon_mood=PhotoImage(file="images/simons_reaction/1.png")
	elif cal==2:
		simon_mood=PhotoImage(file="images/simons_reaction/2.png")
	elif cal==3:
		simon_mood=PhotoImage(file="images/simons_reaction/3.png")
	elif cal==4:
		simon_mood=PhotoImage(file="images/simons_reaction/4.png")
	elif cal==5:
		simon_mood=PhotoImage(file="images/simons_reaction/5.png")
	elif cal==6:
		simon_mood=PhotoImage(file="images/simons_reaction/6.png")
	elif cal==7:
		simon_mood=PhotoImage(file="images/simons_reaction/7.png")

	else:
		simon_mood=PhotoImage(file="images/simons_reaction/0.png")

	return simon_mood





if __name__ == '__main__':
	calificaciones=[1,2,3,4,5,6,7]
	pueblasGT(calificaciones)	