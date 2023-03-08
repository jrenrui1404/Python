from tkinter import *
from tkinter import ttk

base_window = Tk() #creamos la ventana principal

base_window.title('Formulario Python') #añadimos un título

base_window.geometry('350x400+1200+200') #establecemos el tamaño y la posición de la ventana

color_blanco = '#ffffff'
color_negro = '#000000'
color_frame_1 = '#3B77AB'
color_frame_2 = '#F6CC12'
fuente_etiquetas = ('Poppins 10 bold')

#nos definimos el frame para el título
frame_titulo = Frame (base_window, bg=color_frame_1, width=350, height=80)

#nos creamos una rejilla para colocar elementos dentro
frame_titulo.grid(row=0, column=0)

#me creo mi primer label
label_titulo = Label(frame_titulo, text='Formulario Python ( ͡❛ ͜ʖ ͡❛)✊', bg=color_frame_1, fg=color_frame_2, justify=CENTER, font=('Poppins 15 bold'))

#posiciono el label
label_titulo.place(x=35,y=20)

#nos creamos otro frame
main_frame = Frame (base_window, bg=color_frame_2, width=350, height=300)
main_frame.grid(row=1, column=0)

#creo la etiqueta 'Sexo'
label_sexo = Label (main_frame, text='Sexo', font=fuente_etiquetas, justify= LEFT)
label_sexo.place(x=170, y=8)

#creo la etiqueta 'Nombre'
label_sexo = Label (main_frame, text='Nombre', font=fuente_etiquetas, justify= LEFT)
label_sexo.place(x=30, y=8)

#creo la etiqueta 'Asignaturas'
label_asignaturas = Label (main_frame, text='Asignatura favorita', font=fuente_etiquetas, justify = LEFT)
label_asignaturas.place(x=25, y=90)

#creo la etiqueta 'Edad'
label_edad = Label (main_frame, text='Edad', font=fuente_etiquetas, justify= LEFT)
label_edad.place(x=280, y=8)

#creo una lista desplegable para el sexo
valores_sexo = ['hombre','mujer']
combo_sexo = ttk.Combobox(main_frame, values= valores_sexo, font= fuente_etiquetas, width=9)
combo_sexo.place (x=150, y=42)

#creo una caja para las asignaturas
caja_asignaturas = Entry (main_frame, width=12,font=fuente_etiquetas)
caja_asignaturas.place(x=50, y=130)

#creo una caja para la edad
caja_edad = Entry (main_frame, width=4,font=fuente_etiquetas)
caja_edad.place(x=282, y=42)

#creo una caja para la el nombre de la persona
caja_nombre = Entry (main_frame, width=12,font=fuente_etiquetas)
caja_nombre.place(x=20, y=42)


#definimos la funcion para el botón
def get_msm():

    nombre = caja_nombre.get()
    edad = caja_edad.get()
    sexo = combo_sexo.get()
    asig = caja_asignaturas.get()

    cadena = ''
    if sexo == 'hombre':
        cadena = nombre + ' es un ' + sexo + ' le gusta ' + asig + ' y tiene ' + edad + ' años.'
        label_msm = ttk.Label(main_frame, text=cadena)
        label_msm.place(x=30,y=220)
    else:
        cadena = 'Eres una ' + sexo + ' de una edad ' + edad
        label_msm = ttk.Label(main_frame, text=cadena)
        label_msm.place(x=80,y=220)
    
        
#ponemos un boton de calculo
boton = Button (main_frame, text='Enviar', font=fuente_etiquetas, command=get_msm)
boton.place(x=150, y=250)



base_window.mainloop() #hace que la app se quede esperando hasta que la cerremos con la x

