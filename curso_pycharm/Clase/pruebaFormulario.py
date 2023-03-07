from tkinter import *
from tkinter import ttk

base_window = Tk() #creamos la ventana principal

base_window.title('Formulario práctica3') #añadimos un título

base_window.geometry('350x400+1200+200') #establecemos el tamaño y la posición de la ventana

color_blanco = '#ffffff'
color_negro = '#000000'
color_titulo = '#081f4d'
fuente_etiquetas = ('Poppins 15 bold')

#nos definimos el frame para el título
frame_titulo = Frame (base_window, bg=color_titulo, width=350, height=100)

#nos creamos una rejilla para colocar elementos dentro
frame_titulo.grid(row=0, column=0)

#me creo mi primer label
label_titulo = Label(frame_titulo, text='Calculo edad', bg=color_titulo, fg=color_negro,justify=CENTER, font=('Poppins 18 bold'))

#posiciono el label
label_titulo.place(x=5,y=30)

#nos creamos otro frame
main_frame = Frame (base_window, width=350, height=300)
main_frame.grid(row=1, column=0)

#creo la etiqueta 'Sexo'
label_sexo = Label (main_frame, text='Sexo', font=fuente_etiquetas, justify= LEFT)
label_sexo.place(x=5, y=0)

#creo la etiqueta 'Asignaturas'
label_asignaturas = Label (main_frame, text='Asignatura favorita', font=fuente_etiquetas, justify = LEFT)
label_asignaturas.place(x=15, y=35)

#creo la etiqueta 'Edad'
label_edad = Label (main_frame, text='Edad', font=fuente_etiquetas, justify= LEFT)
label_edad.place(x=200, y=0)

#creo una lista desplegable para el sexo
valores_sexo = ['hombre','mujer']
combo_sexo = ttk.Combobox(main_frame, values= valores_sexo, font= fuente_etiquetas, width=9)
combo_sexo.place (x=5, y=32)

#creo una caja para la edad
caja_edad = Entry (main_frame, width=5,font=fuente_etiquetas)
caja_edad.place(x=200, y=32)


#definimos la funcion para el botón
def get_msm():
    edad = caja_edad.get()
    sexo = combo_sexo.get()
    cadena = ''
    if sexo == 'hombre': 
        cadena = 'Eres un ' + sexo + ' de una edad ' + edad
        label_msm = ttk.Label(main_frame, text=cadena)
        label_msm.place(x=10,y=150)
    else:
        cadena = 'Eres una ' + sexo + ' de una edad ' + edad
        label_msm = ttk.Label(main_frame, text=cadena)
        label_msm.place(x=10,y=150)
    
        
#ponemos un boton de calculo
boton = Button (main_frame, text='MSM', font=fuente_etiquetas, command=get_msm)
boton.place(x=130, y=200)



base_window.mainloop() #hace que la app se quede esperando hasta que la cerremos con la x

