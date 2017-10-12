import socket
import network
import machine
import time

mi_led=machine.Pin(0,machine.Pin.OUT) #configuramos el pin D3 
mi_led.value(0) #encendemos el led.

#-----configuramos la red

mired=network.WLAN(network.AP_IF)
mired.config(essid="prueba_de_red_local", authmode=network.AUTH_WPA_WPA2_PSK, password="123456789")
mired.active(True)
print('configuracion total: ',mired.ifconfig())

#........................


def abrir_socket():
	s=socket.socket() #creamos el socket
	s.bind(("", 8266))
	s.listen(1) #se deja el socket esperando a clientes
	cliente,a=s.accept()
	print("se ha conectado un cliente", cliente)
	print("Informacion adicional: ",a)

	while True:
		data=cliente.recv(1) #recibimos un byte.
		print(data[0])
		#revisar que imprie data despues de cero?
		 #ascci 1
		if data[0]==49:
			mi_led.value(0)
			print("value del mi_led es igual a", mi_led)
		if data[0]==48:
			mi_led.value(1)
			print("value del mi_led es igual a", mi_led)
	#fin while
#fin fun socket


    
