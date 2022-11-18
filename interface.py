from tkinter import *
from tkinter import messagebox


metricas=[1,2,3,4,5,6,7]
Cal_juez=0

######################################################interfaz
def pueblasGT(valores):
	raiz = Tk()
	raiz.title("Puebla's got talent")

	my_frame=Frame(raiz,width=800, height=600, bg="black")
	
	#logo
	logo=PhotoImage(file="images/logo_talent.png")
	logotipo=Label(my_frame,image=logo).place(x="200",y="50")

	##values 
	
	Cal_juez=Promedio(valores,metricas)
	Calificacion=Label(my_frame, text=Cal_juez, foreground="white", background="black",font=("Arial", 17)).place(x="600",y="300")

	#boton
	boton1 = Button(raiz,text="--------Iniciar------",padx=304,pady=0, foreground="white", background="black",font=("Arial", 17), command=click_boton)

	#feddback
	jugment=show_image(my_frame,Cal_juez)
	simon=Label(my_frame,image=jugment).place(x="50",y="275")

	my_frame.pack()
	boton1.pack()

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

def click_boton():
	Cal_juez=10


if __name__ == '__main__':
	calificaciones=[1,2,3,4,5,6,7]
	
	pueblasGT(calificaciones)	
    
