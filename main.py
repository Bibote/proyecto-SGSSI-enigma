import rotor
import enigma
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

#Authors of the original code (enigma.py and rotor.py)
__author__ = "Christophe Goessen, Cedric Bonhomme"
__version__ = "0.4.0"
__date__ = "$Date: 2010/01/29 $"
__revision__ = "$Date: 2020/05/17 $"
__copyright__ = "Copyright (c) Christophe Goessen, Cedric Bonhomme"
__license__ = "GPLv3"

print("Enigma machine simulator")

maquina = enigma.Enigma(rotor.ROTOR_Reflector_B, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AV BS CG DL FU HZ IN KM OW RX")



def encriptar():
    #Encripta el texto introducido en la caja de texto.
    texto = caja_texto.get()
    texto_encriptado = maquina.encipher(texto)
    etiqueta_texto_encriptado.config(text="Texto encriptado: " + texto_encriptado)

def encriptarArchivo():
    #Encripta el archivo seleccionado.
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    archivo = fd.askopenfilename(filetypes=filetypes)
    f=open(archivo, "r")
    archivo_encriptado = maquina.encipher(f.read())
    
    tx=f.read()
    ventana2 = tk.Tk()
    ventana2.title("Archivo encriptado")
    ventana2.config(width=400, height=400)
    etiqueta_archivo_encriptado = tk.Label(ventana2, text=archivo_encriptado)
    etiqueta_archivo_encriptado.pack()
    ventana2.mainloop()

def cambioMaquina():

    #Cambia los ajustes de la máquina.
    reflectorCambio = rotor.__dict__[reflector.get()]
    rotor1 = rotor.__dict__[rotorI.get()]
    rotor2 = rotor.__dict__[rotorII.get()]
    rotor3 = rotor.__dict__[rotorIII.get()]
    key = keyI.get()+keyII.get()+keyIII.get()
    plugs = caja_plugs.get().upper()
    if comprobarPlugs():
        maquina = enigma.Enigma(reflectorCambio, rotor1,
                                rotor2, rotor3, key=key,
                                plugs=plugs)
        etiqueta_maquina.config(text="Maquina: " + str(maquina))



def comprobarPlugs():
    #Comprueba que el texto introducido en la caja de texto de los plugs sea correcto
    #Comprueba que todas las letras estén en el array de letras
    #Comprueba que haya un espacio entre cada par de letras
    #Comprueba que haya un número par de letras
    #Comprueba que haya 10 pares de letras
    #Comprueba que no haya letras repetidas
    texto= caja_plugs.get().upper()
    if len(texto) != 29:
        etiqueta_resultado.config(text="Longitud incorrecta")
        return False
    if  texto[2] != " " or texto[5] != " " or texto[8] != " " or texto[11] != " " or texto[14] != " " or texto[17] != " " or texto[20] != " " or texto[23] != " " or texto[26] != " ": 
        etiqueta_resultado.config(text="No son duos")
        return False
    for letra in texto.replace(" ", ""):
        if letra not in letras:
            etiqueta_resultado.config(text="No existe la letra " + letra)
            return False
    
    for letra in letras:
        if texto.count(letra) > 1:
            etiqueta_resultado.config(text="Letra "+letra+" repetida")
            return False
    etiqueta_resultado.config(text="Plugs correctos")
    return True

    #poner un mensaje de error si no es correcto

rotores = ["ROTOR_I", "ROTOR_II", "ROTOR_III", "ROTOR_IV", "ROTOR_V","ROTOR_VI", "ROTOR_VII", "ROTOR_VIII"]
reflectores = ["ROTOR_Reflector_A", "ROTOR_Reflector_B", "ROTOR_Reflector_C"]
letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


ventana = tk.Tk()
ventana.title("Enigma")
ventana.config(width=800, height=500)
etiqueta_ini = ttk.Label(text="Texto a encriptar:")
etiqueta_ini.place(x=20, y=20)

boton_encriptar_archivo = ttk.Button(text="Encriptar archivo", command=encriptarArchivo)
boton_encriptar_archivo.place(x=100, y=60)


caja_texto = ttk.Entry()
caja_texto.place(x=140, y=20, width=200)

boton_convertir = ttk.Button(text="Convertir", command=encriptar)
boton_convertir.place(x=20, y=60)

etiqueta_texto_encriptado = ttk.Label(text="Texto encriptado:")
etiqueta_texto_encriptado.place(x=20, y=100)


etiqueta_reflector = ttk.Label(text="Reflector:")
etiqueta_reflector.place(x=20, y=150)
reflector= tk.StringVar()
reflector.set(reflectores[1])
drop_reflector = tk.OptionMenu(ventana,reflector, *reflectores)
drop_reflector.place(x=120, y=150)


etiqueta_rotor = ttk.Label(text="Rotores:")
etiqueta_rotor.place(x=20, y=190)

rotorI= tk.StringVar()
rotorI.set(rotores[0])
rotorII= tk.StringVar()
rotorII.set(rotores[1])
rotorIII= tk.StringVar()
rotorIII.set(rotores[2])
drop_rotor_1 = tk.OptionMenu(ventana,rotorI, *rotores)
drop_rotor_1.place(x=20, y=220)
drop_rotor_2 = tk.OptionMenu(ventana,rotorII, *rotores)
drop_rotor_2.place(x=120, y=220)
drop_rotor_3 = tk.OptionMenu(ventana,rotorIII, *rotores)
drop_rotor_3.place(x=220, y=220)


keyI= tk.StringVar()
keyI.set(letras[0])
keyII= tk.StringVar()
keyII.set(letras[1])
keyIII= tk.StringVar()
keyIII.set(letras[2])

etiqueta_key = ttk.Label(text="Key:")
etiqueta_key.place(x=20, y=270)
drop_key_1 = tk.OptionMenu(ventana,keyI, *letras)
drop_key_1.place(x=20, y=300)
drop_key_2 = tk.OptionMenu(ventana,keyII, *letras)
drop_key_2.place(x=70, y=300)
drop_key_3 = tk.OptionMenu(ventana,keyIII, *letras)
drop_key_3.place(x=120, y=300)



etiqueta_plugs = ttk.Label(text="Plugs:")
etiqueta_plugs.place(x=20, y=350)
caja_plugs = ttk.Entry()
caja_plugs.insert(0, "AV BS CG DL FU HZ IN KM OW RX")
caja_plugs.place(x=20, y=380, width=200)
boton_plugs = ttk.Button(text="Comprobar", command=comprobarPlugs)
boton_plugs.place(x=220, y=378)
etiqueta_resultado = ttk.Label(text="Plugs correctos")
etiqueta_resultado.place(x=20, y=410)



etiqueta_maquina = ttk.Label(text="Maquina: " + str(maquina))
etiqueta_maquina.place(x=500, y=20)


boton_rotores = ttk.Button(text="Reconfigurar Máquina", command=cambioMaquina)
boton_rotores.place(x=20, y=440)

ventana.mainloop()