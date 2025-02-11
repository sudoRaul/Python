import time #Representa los segundos desde el 1970
from datetime import datetime, date, timedelta #Mejora del módulo anterior
import calendar
time.time() #Devuelve los segundos
tiempo = time.time()
tiempo = time.localtime(tiempo) #Devuelve una estructura más legible, año, dia, 
#mes, hora, minuto, segundo, dia de la semana
tiempo.tm_year #Año actual

time.asctime() #Devuelve la fecha en una cadena
time.strftime("%d/%m/%Y %H:%M:%S") #Devuelve esa información con ese formato
time.strftime("%d-%b-%Y") #Solo dia mes año, y mes en cadena

datetime.now() #Fecha y hora actual
datetime.now().day, datetime.now().month, datetime.now().year #Tupla de esos datos



fecha1 = date.today()
#Se suma a la fecha 1 dos días
fecha2 = fecha1+timedelta(days=2)


anio = date.today().year
mes = date.today().month
#Imprime un calendario
calendario= calendar.month(anio, mes)
#Imprime el calendario de ese año
print(calendar.TextCalendar(calendar.MONDAY).formatyear(2023,2,1,1,2))


