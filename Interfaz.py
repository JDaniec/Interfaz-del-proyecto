from tkinter import *
from tkinter import messagebox
from PIL import Image
import datetime

def filtrar_libros():
    filtro = f.get()  # Obtener el texto ingresado en el entry

    # Obtener los valores de los checkbox de lenguaje
    python_selected = Python.get()
    java_selected = Java.get()
    csharp_selected = cx.get()
    cpp_selected = cxx.get()

    # Obtener los valores de los checkbox de precios
    price_20_selected = d20.get()
    price_40_selected = d40.get()
    price_60_selected = d60.get()
    price_80_selected = d80.get()

    # Obtener los valores de los checkbox de fechas
    date_2005_selected = a2005.get()
    date_2010_selected = a2010.get()
    date_2015_selected = a2015.get()
    date_2020_selected = a2020.get()

    # Crear una nueva lista para almacenar los libros filtrados
    libros_filtrados = []

    # Iterar sobre la lista de libros
    for libro in data:
        # Aplicar los filtros
        if filtro.lower() in libro["book_name"].lower():
            if (python_selected and libro["programming_language"] == "Python") or \
                    (java_selected and libro["programming_language"] == "Java") or \
                    (csharp_selected and libro["programming_language"] == "C#") or \
                    (cpp_selected and libro["programming_language"] == "C++"):

                price = libro["price"].replace('$', '')  # Obtener el precio sin el símbolo de dólar

                if (price_20_selected and float(price) <= 20) or \
                        (price_40_selected and float(price) <= 40) or \
                        (price_60_selected and float(price) <= 60) or \
                        (price_80_selected and float(price) <= 80):

                    release_date_str = libro["release_date"]
                    release_date = datetime.datetime.strptime(release_date_str, "%b %Y").year

                    if (date_2005_selected and release_date <= 2005) or \
                            (date_2010_selected and release_date <= 2010) or \
                            (date_2015_selected and release_date <= 2015) or \
                            (date_2020_selected and release_date <= 2020):

                        libros_filtrados.append(libro)

    # Abrir la ventana de resultados y mostrar los libros filtrados
    abrir_toplevel_resultados(libros_filtrados, toplevel_filtro)




def abrir_toplevel_filtro():
    global toplevel_filtro
    toplevel_filtro = Toplevel()
    toplevel_filtro.title("Filtro")
    toplevel_filtro.resizable(False, False)
    toplevel_filtro.geometry("510x330")
    toplevel_filtro.config(bg="#FFA07A")

    # etiqueta para la etiqueta de filtro
    lb_c = Label(toplevel_filtro, text="Filtro")
    lb_c.config(bg="#FFA07A", fg="black", font=("Helvetica", 18, "bold"))
    lb_c.place(x=20, y=20)

    # caja de texto para filtro
    entry_c = Entry(toplevel_filtro, textvariable=f)
    entry_c.config(bg="#E0E0E0", fg="black", font=("Arial", 14), relief="solid", borderwidth=1)
    entry_c.focus_set()
    entry_c.place(x=100, y=25)

    #Frame para lenguaje
    frame_lenguaje = Frame(toplevel_filtro)
    frame_lenguaje.config(bg="gray", width=200, height=200, relief="solid", borderwidth=2)
    frame_lenguaje.place(x=20, y=80)

    # etiqueta para el "lenguaje"
    lb_t = Label(frame_lenguaje, text="Lenguaje")
    lb_t.config(bg="gray", fg="black", font=("Helvetica", 15))
    lb_t.place(x=25, y=2)


    #Frame para precios
    frame_precios = Frame(toplevel_filtro)
    frame_precios.config(bg="gray", width=150, height=200, relief="solid", borderwidth=2)
    frame_precios.place(x=180, y=80)

    # etiqueta para  "Precio"
    lb_t = Label(frame_precios, text="Precios")
    lb_t.config(bg="gray", fg="black", font=("Helvetica", 15))
    lb_t.place(x=25, y=2)

    #Frame para fechas
    frame_fechas = Frame(toplevel_filtro)
    frame_fechas.config(bg="gray", width=150, height=200, relief="solid", borderwidth=2)
    frame_fechas.place(x=340, y=80)

    # etiqueta para  "Precio"
    lb_t = Label(frame_fechas, text="Fechas")
    lb_t.config(bg="gray", fg="black", font=("Helvetica", 15))
    lb_t.place(x=25, y=2)

    # chechbox para python
    cb_k = Checkbutton(frame_lenguaje, text="Python", variable=Python)
    cb_k.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_k.place(x=10, y=30)

    # checkbox para java
    cb_f = Checkbutton(frame_lenguaje, text="java", variable=Java)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=70)

    # chechbox para c#
    cb_k = Checkbutton(frame_lenguaje, text="C#", variable=cx)
    cb_k.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_k.place(x=10, y=110)

    # checkbox para c++
    cb_f = Checkbutton(frame_lenguaje, text="C++", variable=cxx)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=150)

    
    # checkbox para redondear precios
    cb_f = Checkbutton(frame_precios, text="$20", variable=d20)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=30)

    # checkbox para redondear precios
    cb_f = Checkbutton(frame_precios, text="$40", variable=d40)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=70)

     # checkbox para redondear precios
    cb_f = Checkbutton(frame_precios, text="$60", variable=d60)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=110)

     # checkbox para redondear precios
    cb_f = Checkbutton(frame_precios, text="$80", variable=d80)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=150)


    # boton para borrar
    bt_borrar = Button(toplevel_filtro, text="Borrar", command=borrar)
    bt_borrar.config(bg="gray", fg="Black", font=("Arial", 12, "bold"), relief="raised", borderwidth=3)
    bt_borrar.place(x=320, y=290)


    # boton para abrir Toplevel de los resultados
    # boton para abrir Toplevel de los resultados
    bt_buscar = Button(toplevel_filtro, text="Buscar", command=filtrar_libros)
    bt_buscar.config(bg="gray", fg="Black", font=("Arial", 12, "bold"), relief="raised", borderwidth=3)
    bt_buscar.place(x=420, y=290)

    # checkbox para redondear fechas
    cb_f = Checkbutton(frame_fechas, text="2005-10", variable=a2005)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=30)

    # checkbox para redondear fechas
    cb_f = Checkbutton(frame_fechas, text="2010-15", variable=a2010)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=70)

    # checkbox para redondear fechas
    cb_f = Checkbutton(frame_fechas, text="2015-20", variable=a2015)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=110)

    # checkbox para redondear fechas
    cb_f = Checkbutton(frame_fechas, text="2020-25", variable=a2020)
    cb_f.config(bg="gray", fg="black", font=("Helvetica", 18))
    cb_f.place(x=10, y=150)

#-----------------------------------------------------------------------------------------------    
def abrir_toplevel_resultados(libros_filtrados, toplevel):
    global toplevel_resultados
    toplevel_resultados = Toplevel()
    toplevel_resultados.title("Resultados")
    toplevel_resultados.resizable(False, False)
    toplevel_resultados.config(bg="#FFA07A")

    # Crear un Frame para contener las etiquetas de los libros
    frame_libros = Frame(toplevel_resultados)
    frame_libros.config(bg="gray", relief="solid", borderwidth=2)
    frame_libros.pack(fill=BOTH, expand=True)

    for i, libro in enumerate(libros_filtrados):
        # Crear etiquetas para mostrar los datos del libro
        label_nombre = Label(frame_libros, text="Nombre: " + libro["book_name"])
        label_nombre.config(fg="black", font=("Helvetica", 18, "bold"), padx=10, pady=5, relief="solid", borderwidth=2)
        label_nombre.pack(side=TOP)

        label_autor = Label(frame_libros, text="Autor: " + libro["author"])
        label_autor.config(fg="black", font=("Helvetica", 18, "bold"), padx=10, pady=5, relief="solid", borderwidth=2)
        label_autor.pack(side=TOP)

        # Agregar una línea separadora entre cada libro
        separator = Frame(frame_libros, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=10, pady=5)

    toplevel_resultados.mainloop()



#-------------------------------------------------------------------------------
def borrar():
    f.set("")
    Python.set(False)
    Java.set(False)
    cx.set(False)
    cxx.set(False)
    d20.set(False)
    d40.set(False)
    d60.set(False)
    d80.set(False)
    a2005.set(False)
    a2010.set(False)
    a2015.set(False)
    a2020.set(False)


#-------------------------------------------------------------------------------------------------
#Ventana principal
ventana_principal = Tk()
ventana_principal.title("Proyecto")
ventana_principal.geometry("700x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="#FFA07A")  

#---------------------------------------------------------------------------------------------------
#Variables
f = StringVar()
Python = BooleanVar(value=False)
Java = BooleanVar(value=False)
cx = BooleanVar(value=False)
cxx = BooleanVar(value=False)
d20 =BooleanVar(value=False)
d40 = BooleanVar(value=False)
d60 = BooleanVar(value=False)
d80 = BooleanVar(value=False)
a2005 = BooleanVar(value=False)
a2010 = BooleanVar(value=False)
a2015 = BooleanVar(value=False)
a2020 = BooleanVar(value=False)

data = [
    {
        "book_name": "Intel Galileo Networking Cookbook",
        "book_image": "www.packtpub.com/media/catalog/product/cache/5d165500a520a389deb95b325792ea25/1/1/1198os_intel20galileo20networking20cookbook.jpg",
        "author": "Marco Schwartz",
        "page": 174.0,
        "release_date": "Aug 2015",
        "short_description": "Over 50 recipes that will help you use the Intel Galileo board to build exciting network-connected p...",
        "price": "$23.99",
        "programming_language": "C#",
        "concept": "Networking",
        "tool": "Galileo"
    },
    {
        "book_name": "OpenVPN Cookbook - Second Edition",
        "book_image": "www.packtpub.com/media/catalog/product/cache/5d165500a520a389deb95b325792ea25/9/7/9781786463128.png",
        "author": "Jan Just Keijser",
        "page": 400.0,
        "release_date": "Feb 2017",
        "short_description": "Discover over 90 practical and exciting recipes that leverage the power of OpenVPN 2.4 to help you o...",
        "price": "$39.99",
        "programming_language": "C#",
        "concept": "Networking",
        "tool": "OpenVPN"
    },
    
]

#-----------------------------------------------------------------------------------------------------
#Frame para titulo
frame_titulo = Frame(ventana_principal)
frame_titulo.config(bg="gray", width=680, height=80, relief="solid", borderwidth=2)
frame_titulo.place(x=10, y=10)

# etiqueta para el titulo del proyecto
lb_t = Label(frame_titulo, text="App")
lb_t.config(bg="gray", fg="black", font=("Helvetica", 18, "bold"), padx=10, pady=5, relief="solid", borderwidth=2)
lb_t.place(x=310, y=20)

#Frame para titulo
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="gray", width=680, height=390, relief="solid", borderwidth=2)
frame_entrada.place(x=10, y=100)


# boton para abrir Toplevel del filtro
bt_filtro = Button(frame_entrada, text="Filtro", command=abrir_toplevel_filtro)
bt_filtro.config(width=15, height=3, bg="#FFA07A", fg="Black", font=("Arial", 12, "bold"), relief="raised", borderwidth=3)
bt_filtro.place(x=20, y=20)





ventana_principal.mainloop()
