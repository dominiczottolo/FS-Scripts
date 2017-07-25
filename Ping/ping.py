# typo error in import
import subprocess
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

def ip_check():

	try:
		ip = raw_input("[+] What IP addresses would you like to ping: ")

		ip.replace(" ", "")
		first = ip.split("-")[0]
		last = ip.split("-")[1]

		start = int(first.split(".")[3])
		end = int(last.split(".")[3]) + 1

		static = ""
		static2 = ""

		for i in range(0,3):
			static += first.split(".")[i] + "."
			static2 += last.split(".")[i] + "."

		# print static, static2

		if(static != static2):
			print "[-] The IP format you entered is not valid"
			again = raw_input("[+] Rerun program (yes/no): ")
			if (again == "yes"):
				ip_check()
			else:
				return

		for ping in range(start,end):
		    address = static + str(ping)
		    print "\n"
		    res = subprocess.call(['ping', '-c', '3', address])
		    if res == 0:
		        print "ping to", address, "OK"
		    elif res == 2:
		        print "no response from", address
		    else:
		        print "ping to", address, "failed!"

		print "\n[+] Tool has finished\n"

	except:
		print "[-] Error has occured"
		again = raw_input("[+] Rerun program (yes/no): ")
		if (again == "yes"):
			ip_check()

print "\n[+] Ping IP tool is running..."
print "[+] Please enter IP addresses in the form of: 120.0.0.0-120.0.0.50"		
ip_check()