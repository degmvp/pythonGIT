print('✅' * 50)
print('''
#-------------------------------------------------------
# ✅ advR004
# ✅ Python 3.6 alterado: 2017/10/07
# ✅ Objetivo:cmd avançado mediaplayer mp.txt,mptime.txt
# ✅ Comandos:import pygame,random,time,timeit,messagebox,from tkinter
# ✅ Funções :open(),close(),readline(),get(),set(),place(),Entry()
#-------------------------------------------------------''')
print('✅' * 50)
from tkinter import *
from tkinter import messagebox
import pygame
import tkinter.messagebox
import random
from tkinter import ttk
import time
import timeit
#----------------------------
from functools import partial
#----------------------------

lista = []
listaH = []
def cargarH():
    archivoH = open('mptime.txt','r')
    lineaH = archivoH.readline()
    if lineaH:
        while lineaH:
            if lineaH[-1] == '\n':
                lineaH = lineaH[:-1]
            listaH.append(lineaH)
            lineaH = archivoH.readline()
    archivoH.close()

def guardar():
    n = nombre.get()
    lista.append(n)
    escribirContacto()
    messagebox.showinfo('Gravado','Gravou no catalogo de musicas')
    nombre.set('')
    consultar()
    
def eliminar():
    i = int(conteliminar.get())
    lista.pop(i)  
    escribirContacto()
    consultar()
    messagebox.showinfo('Deletado o item -->: ',i)
        


def iniciarArchivo():
    archivo = open('mp.txt','a')
    archivo.close()

def cargar():
    archivo = open('mp.txt','r')
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open('mp.txt','w')
    #lista.sort()
    for elemento in lista:
        archivo.write(elemento+'\n')
    archivo.close()




def consultar():
    r = Text(ventana, width=80, height=15)
    #lista.sort()
    valores = []
    r.insert(INSERT,'Playlist-Catalog: ProgressBar : Vertical is System : Horizontal is Music\n')
    for elemento in lista:
        arreglo = elemento.split(',')
        #valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+'\t\n')
        r.place(x=20,y=230)
        spinTelefono = Spinbox(ventana,value=(valores),textvariable=conteliminar).place(x=450,y=50)
        if lista ==[]:
            spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)
        r.config(state=DISABLED)
        
def ver():
    r = Text(ventana, width=80, height=15)
    #lista.sort()
    valores = []
    r.insert(INSERT,'Playlist-Catalog: ProgressBar : Vertical is System : Horizontal is Music\n')
    for elemento in lista:
        arreglo = elemento.split('$')
        #valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+'\t\n')
        r.place(x=20,y=230)
    cargarH()
     
def fim():
    ventana.destroy() 

def mix():
    random.shuffle(lista)
    escribirContacto()
    consultar()

def bt_click(xarg):
    if (xarg['text']) == 'M0':
        playmusic(0)
    if (xarg['text']) == 'M1':
        playmusic(1)
    if (xarg['text']) == 'M2':
        playmusic(2)
    if (xarg['text']) == 'M3':
        playmusic(3)
    if (xarg['text']) == 'M4':
        playmusic(4)
    if (xarg['text']) == 'M5':
        playmusic(5)
    if (xarg['text']) == 'M6':
        playmusic(6)
    if (xarg['text']) == 'M7':
        playmusic(7)
    if (xarg['text']) == 'M08':
        playmusic(8)
    if (xarg['text']) == 'M09':
        playmusic(9)
    if (xarg['text']) == 'M10':
        print(xarg['text'])
        playmusic(10)
    if (xarg['text']) == 'M11':
        playmusic(11)
    if (xarg['text']) == 'M12':
        playmusic(12)
    if (xarg['text']) == 'M13':
        pb = ttk.Progressbar(ventana, orient="horizontal", length=400,mode="indeterminate")
        pb.place(x=100,y=430)
        pb.stop()
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo('Vc Clicou! ',radioValue)

  
def playmusic(i):
    mp = lista[i] + '.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(mp)
    pygame.mixer.music.play()
    pb = ttk.Progressbar(ventana, orient="horizontal", length=400,mode="indeterminate")
    pb.place(x=150,y=430)
    pb.start()
    pb1 = ttk.Progressbar(ventana, orient="vertical", length=120,mode="determinate")
    pb1.place(x=200,y=330)
    pb1.start()
    lhora = Label(ventana, text='Music and Playing Time : ',bg=colorFondo, \
                       fg=colorLetra,font=('Helvetica',13)).place(x=230,y=330)
    mpt = listaH[i]
    lmpt = Label(ventana, text=mpt,bg=colorFondo, \
                       fg=colorLetra,font=('Helvetica',10)).place(x=430,y=330)
    pygame.event.wait

def pause():
    pygame.mixer.music.stop()
    

V = 0
ventana = Tk()
nombre = StringVar()
conteliminar = StringVar()
colorFondo = "#006"
colorLetra = "#FFF"
iniciarArchivo()
cargar()
consultar()
ventana.title("Media Player ✅ advR002 ")
ventana.geometry("700x500")
ventana.configure(bg=colorFondo)
#------------------------------
relStatus = StringVar()
#------------------------------

etiquetaTitulo = Label(ventana, text='Media Player Playlist Files',bg=colorFondo, \
                       fg=colorLetra,font=('Helvetica',16)).place(x=230,y=10)
etiquetaN      = Label(ventana, text='Playlist-Catalog: ',bg=colorFondo, \
                       fg=colorLetra).place(x=50,y=50)
cajaN          = Entry(ventana, textvariable=nombre).place(x=150,y=50)

r0 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='M0', bg='powder blue',value='Clicou! M0',variable = relStatus)
r0['command'] = partial(bt_click,r0)
r0.place(x=150,y=80)

r1 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='powder blue', text='M1',value='Clicou! M1', variable = relStatus) 
r1['command'] = partial(bt_click,r1)
r1.place(x=150,y=110)

r2 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='GOLDENROD', text='M2',value='Clicou! M2', variable = relStatus)
r2['command'] = partial(bt_click,r2)
r2.place(x=150,y=140)

r3 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='GOLDENROD', text='M3',value='Clicou! M3', variable = relStatus)
r3['command'] = partial(bt_click,r3)
r3.place(x=150,y=170)

r4 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M4',value='Clicou! M4', variable = relStatus)
r4['command'] = partial(bt_click,r4)
r4.place(x=200,y=80)

r5 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M5',value='Clicou! M5', variable = relStatus)
r5['command'] = partial(bt_click,r5)
r5.place(x=200,y=110)

r6 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='powder blue', text='M6',value='Clicou! M6', variable = relStatus)
r6['command'] = partial(bt_click,r6)
r6.place(x=200,y=140)

r7 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='powder blue', text='M7',value='Clicou! M7', variable = relStatus)
r7['command'] = partial(bt_click,r7)
r7.place(x=200,y=170)

r8 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='GOLDENROD', text='M08',value='Clicou! M08', variable = relStatus)
r8['command'] = partial(bt_click,r8)
r8.place(x=250,y=80)

r9 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='GOLDENROD', text='M09',value='Clicou! M9', variable = relStatus)
r9['command'] = partial(bt_click,r9)
r9.place(x=250,y=110)

r10 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M10',value='Clicou! M10', variable = relStatus)
r10['command'] = partial(bt_click,r10)
r10.place(x=250,y=140)

r11 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M11',value='Clicou! M11', variable = relStatus)
r11['command'] = partial(bt_click,r11)
r11.place(x=250,y=170)

r12 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M12',value='Clicou! M12', variable = relStatus)
r12['command'] = partial(bt_click,r12)
r12.place(x=315,y=80)

r13 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='gray', text='M13',value='Clicou! M13', variable = relStatus)
r13['command'] = partial(bt_click,r13)
r13.place(x=315,y=110)

botonGuardar     = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='Save',bg='red',command=guardar)
botonGuardar.place(x=315,y=140)

btnpause = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='Pause',bg='green',command=pause)
btnpause.place(x=315,y=180)

etiquetaEliminar = Label(ventana, text='Seek: ',bg=colorFondo, \
                       fg=colorLetra).place(x=370,y=50)

spinTelefono     = Spinbox(ventana, textvariable=conteliminar).place(x=450,y=50)


botonEliminar    = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='Delete', command=eliminar,bg='yellow')
botonEliminar.place(x=470,y=80)

bot1             = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='Select', command=ver,bg='yellow')
bot1.place(x=470,y=115)

bot2             = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),text='Shutdown', command=fim,bg='yellow')
bot2.place(x=470,y=145)

r14 = Radiobutton(ventana,bd=4,font=('arial',10,'bold'),bg='red', text='MIX',command=mix)
r14.place(x=470,y=180)

for widget in (r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,botonGuardar,botonEliminar,bot1,bot2,r14):
    widget.configure(relief="groove", border=8)

mainloop()


