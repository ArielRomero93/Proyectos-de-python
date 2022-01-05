#IMPORTO WIN32COM.CLIENT PARA PODER TRABAJAR CON LOS ESCRIPPTS DE WINDOWS.
#OS PARA TRABAJAR CON LAS UTILIDADES DE SISTEMA OPERATIVO.
#TIME PARA TRABAJAR CON LA FUNCION DEL TIEMPO.
#EASYGUI PARA GENERAR CARTELES.
import win32com.client
import os
import time
import easygui as eg

#COMIENZO CREARNDO UN ACCESO DIRECTO EN EL ESCRITORIO CON Dispatch.
comienzo = win32com.client.Dispatch("WScript.Shell")
escritorio = comienzo.SpecialFolders("Desktop")

#USO UNA VARIABLE BOOLEANA COMO  BANDERA PARA PODER DAR UNA CONDICIÓN PARA CREAR O NO LA CARPETA.
existe = False
#sI EXISTE LA CARPETA NO LA CREA, DE LO CONTRARIO, SI.
if existe == False:
    try:
        #CREO LA CARPETA CON OS LLAMANDO AL METODO MKDIR.
        carpeta = os.mkdir(escritorio + "\\Ejercicio3")
        existe = True
    except:
        pass


#EJECUTO EL BLOCK DE NOTAS.
comienzo.Run("notepad.exe")
#ACTIVO SU USO.
comienzo.AppActivate("notepad.exe")
#GENERO UNA VARIABLE CON EL TEXTO A INGRESAR EN EL BLOCK.
texto = "Todo lo puedo en Cristo que me fortalece."
#dOY UNA ESPERA DE MEDIO SEGUNDO ANTES DE COMENZAR.
time.sleep(0.5)
#ANTES DE INGRESAR TEXTO. sI ESTE BLOCK YA FUÉ USADO. sELECCINA TODO Y LO BORRA.
comienzo.SendKeys("^e")
comienzo.SendKeys("{DEL}")
#ESPERA MEDIO SEGUNDO
time.sleep(0.5)
#RECORRE EL TEXTO Y LO VA INGRESANDO LETRA POR LETRA CON UNA ESPERA DE 0,1 SEGUNDO.
for i in texto:
    comienzo.SendKeys(i)
    time.sleep(0.1)

#ESPERA UN SEGUNDO.
time.sleep(1)


#CIERRA EL PROGRAMA DANDO LUGAR AL CUADRO DE DIALOGO DE CONFIRMACIÓN QUE DA LA OPCIÓN DE GUARDAR.
comienzo.SendKeys("%{f4}")

#GENERO UN CARTEL QUE ME DÁ UNA INSTRUCCIÓN FINAL Y COLMINA LA ACTIVIDAD.
cartel = eg.msgbox(msg='Fin de la presentación del Ejercicio3. Por favor cierre este cuadro de dialogo y precione guardar para almacenar el archivo en la carpeta "Ejercicio 3" ya creada en el escritorio.', title='Finalización')