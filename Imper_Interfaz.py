import sys
import os
import customtkinter as ctk
from customtkinter import CTkFont 
from PIL import Image
from IA_Implement.objetos import Terreno, Construida

# Función para obtener la ruta del archivo de recursos
def resource_path(relative_path):
    """Obtiene la ruta de los recursos empaquetados dentro del archivo .exe."""
    try:
        # PyInstaller crea una carpeta temporal para el archivo empaquetado
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


root = ctk.CTk()
font_path = resource_path("Prompt-Regular.ttf")
root.iconbitmap("icono.ico")
try:
    custom_font = ctk.CTkFont(family="Prompt-Regular", size=16) 
    custom_bold_font=ctk.CTkFont(family="Prompt-Bold.ttf", size=18)# Usar la fuente con CTkFont
except Exception as e:
    print(f"Error cargando la fuente: {e}")
    custom_font = ctk.CTkFont(family="Arial", size=16)
    custom_bold_font=ctk.CTkFont(family="ArialBlack", size=18)

# Configuración inicial
ctk.set_appearance_mode("Dark")  # Modo oscuro por defecto
ctk.set_default_color_theme("blue")  # Tema de color
# Ventana principal


root.title("PropTech")
root.geometry("600x700")

# Función para alternar entre modos oscuro y claro
def toggle_dark_mode():
    if dark_mode_switch.get():
        ctk.set_appearance_mode("Dark")
        fg_color = "gray20"
    else:
        ctk.set_appearance_mode("Light")
        fg_color = "#C0C0C0"
        
    big_label.configure(fg_color = fg_color)


# Panel izquierdo
left_frame = ctk.CTkFrame(root, width=300)
left_frame.pack(side="left", fill="y", padx=20, pady=10)

label_left = ctk.CTkLabel(left_frame, text="PropTech", font=custom_bold_font)
label_left.pack(pady=10)
image_path = "logo.jpg"
imagen = ctk.CTkImage(Image.open(image_path), size=(150, 150))
image_label = ctk.CTkLabel(left_frame, text="", image=imagen)
image_label.pack(pady=10,padx=10)

btn1 = ctk.CTkButton(left_frame, text="Menu Principal",command=lambda: mostrar_interfaz(1))
btn1.pack(pady=10)
btn2 = ctk.CTkButton(left_frame, text="Calcular Terreno",command=lambda: mostrar_interfaz(2))
btn2.pack(pady=10)
btn3 = ctk.CTkButton(left_frame, text="Calcular Propiedad\nConstruida",command=lambda: mostrar_interfaz(3))
btn3.pack(pady=10)

spacelabel = ctk.CTkLabel(left_frame, text="")
spacelabel.pack(pady=90)

dark_mode_switch = ctk.CTkSwitch(left_frame, text="Dark Mode", command=toggle_dark_mode)
dark_mode_switch.select()
dark_mode_switch.pack(pady=10)

# Panel principal
main_frame = ctk.CTkFrame(root)
main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

def actualizar_color():
    if dark_mode_switch.get():
        fg_color = "gray20"
    else:
        fg_color = "C0C0C0"


title = CTkFont(family=custom_bold_font.cget("family"),size=25, weight=custom_bold_font.cget("weight")) 
# Etiqueta grande
big_label = ctk.CTkLabel(main_frame,text="Calcular Propiedad Construida",font=title)
image_path2 = "Leonardo_Phoenix_A_vibrant_and_attentiongrabbing_banner_promot_3.jpg"
imagen2 = ctk.CTkImage(Image.open(image_path2), size=(342, 170))
image_label2 = ctk.CTkLabel(main_frame, text="", image=imagen2)
image_label2.pack(pady=10,padx=10)
big_label.pack(pady=10)

def mostrar_interfaz(interface_num):
    # Primero, ocultamos todos los widgets de la interfaz anterior
    for widget in main_frame.winfo_children():
        widget.pack_forget()  # Ocultar todos los widgets
    # Luego, mostramos los widgets correspondientes a la interfaz seleccionada
    if interface_num == 1:
        mostrar_menu_principal()
    elif interface_num == 2:
        mostrar_calcular_terreno()
    elif interface_num == 3:
        mostrar_calcular_propiedad()

def mostrar_menu_principal():
    big_label = ctk.CTkLabel(main_frame,text="Calcular Precio de un terreno",font=title)
    image_path2 = "Leonardo_Phoenix_A_vibrant_and_attentiongrabbing_banner_promot_3.jpg"
    imagen2 = ctk.CTkImage(Image.open(image_path2), size=(342, 170))
    image_label2 = ctk.CTkLabel(main_frame, text="", image=imagen2)
    image_label2.pack(pady=10,padx=10)
    big_label.pack(pady=10)
    
    slogan_label = ctk.CTkLabel(
    main_frame, 
    text="Evalúa tu espacio, mejora tu inversión", 
    font=("Arial", 16, "italic"),
    text_color="gray"
    )
    slogan_label.pack(pady=10)

    # Bienvenida
    welcome_label = ctk.CTkLabel(
        main_frame, 
        text="¡Bienvenido a nuestra aplicación!", 
        font=("Arial", 18, "bold")
    )
    welcome_label.pack(pady=20)

    # Botones
    btn_terreno_sin_construir = ctk.CTkButton(
        main_frame, 
        text="Terreno sin construir", 
        command=lambda:mostrar_interfaz(2)
    )
    btn_terreno_sin_construir.pack(pady=10)

    btn_terreno_construido = ctk.CTkButton(
        main_frame, 
        text="Terreno construido", 
        command=lambda:mostrar_interfaz(3)
    )
    btn_terreno_construido.pack(pady=10)

def mostrar_calcular_terreno():
    big_label = ctk.CTkLabel(main_frame,text="Calcular Precio de un terreno",font=title)
    image_path2 = "Leonardo_Phoenix_A_vibrant_and_attentiongrabbing_banner_promot_3.jpg"
    imagen2 = ctk.CTkImage(Image.open(image_path2), size=(342, 170))
    image_label2 = ctk.CTkLabel(main_frame, text="", image=imagen2)
    image_label2.pack(pady=5,padx=10)
    big_label.pack(pady=5)

    text = CTkFont(family=custom_bold_font.cget("family"),size=15, weight=custom_bold_font.cget("weight")) 

    Etiqueta1=ctk.CTkLabel(main_frame,text="Seleccione un tipo de suelo:",
    font=text,
    width=100, 
    height=50, 
    corner_radius=10, 
    fg_color="gray20", 
    justify="center")
    Etiqueta1.pack(pady=3)
    

    # Crear una lista de opciones para el menú desplegable
    opciones = ["Suelo Rustico", "Suelo Urbano", "Suelo Industrial"]
    
    opcion_seleccionada = ctk.StringVar(value=opciones[0])

    # Crear el menú desplegable
    menu_desplegable = ctk.CTkOptionMenu(main_frame, values=opciones)
    menu_desplegable.pack(pady=3)
    
    def obtener_valor():
        if(opcion_seleccionada.get() == "Suelo Rustico"):
            print(1)
            return 1
        elif(opcion_seleccionada.get() == "Suelo Industrial"):
            print(2)
            return 2
        else:
            print(3)
            return 3

    def validar_entrada(texto):
        try:
            valor = int(texto.get())
            if(999999 < valor < 4000001):
                error_label.configure(text="", text_color="green")
                return valor
            else:
                error_label.configure(text="Numero fuera de rango", text_color="red")
                return False
        except ValueError as e:
            print(e)
            error_label.configure(text="Solo se aceptan numeros", text_color="red")
            return False

    def validar_entrada2(texto):
        try:
            valor = int(texto.get())
            if(9 < valor < 101):
                error_label2.configure(text="", text_color="green")
                return valor
            else:
                error_label2.configure(text="Numero fuera de rango", text_color="red")
                return False
        except ValueError as e:
            print(e)
            error_label2.configure(text="Solo se aceptan numeros", text_color="red")
            return False


    # Etiqueta grande
    Etiqueta2 = ctk.CTkLabel(main_frame,
    text = "Ingrese el precio del predio, sin puntos ni comas\n(Min: 1.000.000 Max: 4.000.000):",
    font=text,
    width=100, 
    height=50, 
    corner_radius=10, 
    fg_color="gray20", 
    justify="center")
    Etiqueta2.pack(pady=3)

    # Entrada de texto
    entry = ctk.CTkEntry(main_frame, placeholder_text="Ingresa el precio...")
    entry.pack(pady=3)

    #Error label
    error_label = ctk.CTkLabel(main_frame,text="")
    error_label.pack(pady=0.5)

    Etiqueta3 = ctk.CTkLabel(main_frame, text = "Ingrese el area total del predio en m2\n(Min: 10 Max: 100):",
    font=text,
    width=100, 
    height=50, 
    corner_radius=10, 
    fg_color="gray20", 
    justify="center")
    Etiqueta3.pack(pady=2)

    entry2 = ctk.CTkEntry(main_frame, placeholder_text="Ingresa el area m2...")
    entry2.pack(pady=3)

    #Error label
    error_label2 = ctk.CTkLabel(main_frame,text="")
    error_label2.pack(pady=0.5)
    
    def call_all(entry,entry2):
        tiposuelo=obtener_valor()
        valor=validar_entrada(entry)
        tamano=validar_entrada2(entry2)
        terreno = Terreno(tiposuelo,valor,tamano)
        label_response2.configure(text=f"${int(terreno.predecirconstruccion())}")

    # Botones adicionales
    btn_ctk = ctk.CTkButton(main_frame, text="Enviar",command=lambda:call_all(entry,entry2))
    btn_ctk.pack(pady=3)
    
    frame_response = ctk.CTkFrame(main_frame,width=450,height=200)
    frame_response.pack(pady=3)
    
    label_response = ctk.CTkLabel(frame_response,text="La Valorizacion de la vivienda segun nuetra red neuronal es:")
    label_response.pack(pady=10,padx=10)
    
    label_response2= ctk.CTkLabel(frame_response,text="",font=title)
    label_response2.pack(pady=10,padx=10)

def mostrar_calcular_propiedad():
    title = CTkFont(family=custom_bold_font.cget("family"),size=25, weight=custom_bold_font.cget("weight")) 
    # Etiqueta grande
    big_label = ctk.CTkLabel(main_frame,text="Calcular Propiedad Construida",font=title)
    image_path2 = "Leonardo_Phoenix_A_vibrant_and_attentiongrabbing_banner_promot_3.jpg"
    imagen2 = ctk.CTkImage(Image.open(image_path2), size=(342, 170))
    image_label2 = ctk.CTkLabel(main_frame, text="", image=imagen2)
    image_label2.pack(pady=10,padx=10)
    big_label.pack(pady=10)


    l_main_frame = ctk.CTkFrame(main_frame)
    l_main_frame.pack(fill="both")

    text = CTkFont(family=custom_bold_font.cget("family"),size=15, weight=custom_bold_font.cget("weight")) 

    text_label1=ctk.CTkLabel(l_main_frame,text="Seleccione un tipo de suelo:",font=text)
    text_label1.pack(pady=1,padx=25)
    # Crear una lista de opciones para el menú desplegable
    opciones = ["Suelo Rustico", "Suelo Urbano", "Suelo Industrial"]
    
    opcion_seleccionada = ctk.StringVar(value=opciones[0])
    
    # Crear el menú desplegable
    menu_desplegable = ctk.CTkOptionMenu(l_main_frame,variable=opcion_seleccionada, values=opciones)
    menu_desplegable.pack(pady=10)
    def obtener_valor():
        if(opcion_seleccionada.get() == "Suelo Rustico"):
            print(1)
            return 1
        elif(opcion_seleccionada.get() == "Suelo Industrial"):
            print(2)
            return 2
        else:
            print(3)
            return 3

    entrada_texto=ctk.StringVar()
    
    def validar_entrada(*args):
        try:
            valor = int(entrada_texto.get())
            if(999999 < valor < 4000001):
                print("todo okey mi crack")
                error_label.configure(text="", text_color="green")
                return valor
            else:
                error_label.configure(text="Numero fuera de rango", text_color="red")
                return False
        except ValueError as e:
            print(e)
            error_label.configure(text="Recuerde que solo se aceptan numeros", text_color="red")
            return False

    text_label2=ctk.CTkLabel(l_main_frame,text="Dijite valor del suelo por metro cuadrado\n(Min: 1.000.000 Max: 4.000.000):",font=text)
    text_label2.pack(pady=1,padx=25)
    
    # Asociar la función de validación a la variable StringVar
    entrada_texto.trace_add("write", validar_entrada)

    
    # Entrada de texto
    entry = ctk.CTkEntry(l_main_frame, placeholder_text="Escribe el valor aquí...",textvariable=entrada_texto,width=200)
    entry.pack(pady=5,padx=10)

    #Error label
    error_label = ctk.CTkLabel(l_main_frame,text="")
    error_label.pack(pady=0.5)

    #boton label
    btn_label = ctk.CTkLabel(l_main_frame,text="Seleccione ubicaciones cerca de la vivienda",font=text)
    btn_label.pack(padx=25)
    #Botones de seleccion Multiple
    def contar_seleccionador():
        seleccionados = 0.0
        if check_var1.get()==1:
            seleccionados += 0.1
        if check_var2.get()==1:
            seleccionados += 0.1
        if check_var3.get()==1:
            seleccionados += 0.1
        if check_var4.get()==1:
            seleccionados += 0.1
        if check_var5.get()==1:
            seleccionados += 0.1
        if check_var6.get()==1:
            seleccionados += 0.1
        if check_var7.get()==1:
            seleccionados += 0.1
        if check_var8.get()==1:
            seleccionados += 0.11
        if check_var9.get()==1:
            seleccionados += 0.1
        if check_var10.get()==1:
            seleccionados += 0.1
        print(seleccionados)
        return seleccionados


    check_var1 = ctk.IntVar(value=0)
    check_var2 = ctk.IntVar(value=0)
    check_var3 = ctk.IntVar(value=0)
    check_var4 = ctk.IntVar(value=0)
    check_var5 = ctk.IntVar(value=0)
    check_var6 = ctk.IntVar(value=0)
    check_var7 = ctk.IntVar(value=0)
    check_var8 = ctk.IntVar(value=0)
    check_var9 = ctk.IntVar(value=0)
    check_var10 = ctk.IntVar(value=0)

    check_label = ctk.CTkFrame(l_main_frame)
    check_label.pack(pady=5)

    # Crear los checkboxes y organizarlos en dos filas de 5
    checkboxes = [
        ("Conjuntos residenciales", check_var1), ("Hospitales", check_var2), ("Parques", check_var3),
        ("Avenidas", check_var4), ("Zona de Comercio", check_var5),
        ("Escuelas", check_var6), ("Transporte Publico", check_var7), ("Zona turistica", check_var8),
        ("Areas Recreativas", check_var9), ("Seguridad Alta", check_var10)
    ]

    # Usar grid para organizar los checkboxes
    for i, (text, var) in enumerate(checkboxes):
        fila = i % 5  # Calcula la fila (de 0 a 4)
        columna = i // 5  # Calcula la columna (de 0 a 1)
        
        checkbox = ctk.CTkCheckBox(check_label, text=text, variable=var)
        checkbox.grid(row=fila, column=columna, padx=5, pady=5,sticky="ew")
        

    def call_all(entry):
        tiposuelo = obtener_valor()
        valorcasa=validar_entrada(entry)
        seleccionados=contar_seleccionador()
        roud_seleccionados= round(seleccionados,1)
        print(tiposuelo)
        print(valorcasa)
        print(roud_seleccionados)
        if(roud_seleccionados==0.0):
            print("Error")
        else:
            calcular_propiedad(tiposuelo,valorcasa,roud_seleccionados)
    
    
    # Botones adicionales
    btn_ctk = ctk.CTkButton(l_main_frame, text="Siguiente",command=lambda:call_all(entry))
    btn_ctk.pack(pady=5)

def calcular_propiedad(tiposuelo,valorcasa,selecionados):
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    title = CTkFont(family=custom_bold_font.cget("family"),size=25, weight=custom_bold_font.cget("weight")) 
    # Etiqueta grande
    big_label = ctk.CTkLabel(main_frame,text="Calcular Propiedad Construida",font=title)
    image_path2 = "Leonardo_Phoenix_A_vibrant_and_attentiongrabbing_banner_promot_3.jpg"
    imagen2 = ctk.CTkImage(Image.open(image_path2), size=(342, 170))
    image_label2 = ctk.CTkLabel(main_frame, text="", image=imagen2)
    image_label2.pack(pady=10,padx=10)
    big_label.pack(pady=10)
    l_main_frame = ctk.CTkFrame(main_frame)
    l_main_frame.pack(fill="both")

    text = CTkFont(family=custom_bold_font.cget("family"),size=15, weight=custom_bold_font.cget("weight")) 



    text_label2=ctk.CTkLabel(l_main_frame,text="Dijite los metros cuadrados de la propiedad\n(Min: 10 Max: 100):",font=text)
    text_label2.pack(pady=10,padx=25)
    # Entrada de texto
    entry = ctk.CTkEntry(l_main_frame, placeholder_text="Escribe el valor aquí...",width=200)
    entry.pack(pady=5,padx=10)

    #Error label
    error_label = ctk.CTkLabel(l_main_frame,text="")
    error_label.pack(pady=0.5)

    text_label1=ctk.CTkLabel(l_main_frame,text="Seleccione el tipo de construccion:",font=text)
    text_label1.pack(pady=1,padx=25)
    # Crear una lista de opciones para el menú desplegable
    opciones = ["Bodega", "Apartamento", "Casa"]
    
    opcion_seleccionada = ctk.StringVar(value=opciones[0])
    
    def obtener_valor():
        if(opcion_seleccionada.get() == "Bodega"):
            print(1)
            return 1
        elif(opcion_seleccionada.get() == "Apartamento"):
            print(2)
            return 2
        else:
            print(3)
            return 3
    
    # Crear el menú desplegable
    menu_desplegable = ctk.CTkOptionMenu(l_main_frame,variable=opcion_seleccionada ,values=opciones)
    menu_desplegable.pack(pady=10)
    


    def validar_entrada(texto):
        try:
            valor = int(texto.get())
            if(9 < valor < 101):
                print("todo okey mi crack")
                error_label.configure(text="", text_color="green")
                return valor
            else:
                error_label.configure(text="Numero fuera de rango", text_color="red")
                return False
        except ValueError as e:
            print(e)
            error_label.configure(text="Recuerde que solo se aceptan numeros", text_color="red")
            return False



    def call_all(entry):
        medida=validar_entrada(entry)
        tipo=obtener_valor()
        construccion = Construida(tiposuelo,valorcasa,medida,selecionados,tipo)
        label_response2.configure(text=f"${int(construccion.predecirconstruccion())}")
        
    # Botones adicionales
    btn_ctk = ctk.CTkButton(l_main_frame, text="Calcular Valor",command=lambda:call_all(entry))
    btn_ctk.pack(pady=5)
    
    frame_response = ctk.CTkFrame(l_main_frame,width=450,height=200)
    frame_response.pack(pady=20)
    
    label_response = ctk.CTkLabel(frame_response,text="La Valorizacion de la vivienda segun nuetra red neuronal es:")
    label_response.pack(pady=10,padx=10)
    
    label_response2= ctk.CTkLabel(frame_response,text="",font=title)
    label_response2.pack(pady=10,padx=10)

mostrar_interfaz(1)
# Bucle principal
root.mainloop()
