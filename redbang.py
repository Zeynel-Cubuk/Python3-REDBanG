from socket import *
import colorama
import time
import sys
from colorama import Fore

class BannerGrab(object):
    colorama.init()
    def banner():
        time.sleep(2)
        print(Fore.GREEN+'\n\n#-------------------------------------------------------#')
        print('#                    | REDBanG V1.0 |                   #')
        print('#-------------------------------------------------------#')
        print('#-------------------------------------------------------#')
        print('#                                                       #')
        print('#                Coded by RedSoftware                   #')
        print('#                                                       #')
        print('#               IG :@redsoftwareofficial                #')
        print('#                                                       #')
        print('#-------------------------------------------------------#')
        time.sleep(2)

    banner()
    def __init__(self,host=''):
        self.host = host
        self.ports = [20, 21, 22, 23, 25, 53, 80, 111, 139, 389, 443, 445, 514]
        colorama.init()

    def portScanner(self):

        setdefaulttimeout(2)
        time.sleep(2)

        print(Fore.GREEN+'\n[*] Scanning {} '.format(self.host))
        print('\n'+'-'*28)
        for port in self.ports:
            try:
                sock = socket(AF_INET,SOCK_STREAM)
                sock.connect((self.host,port))
                time.sleep(2)
                print(Fore.GREEN+'\n[+] {}:{} Open!'.format(self.host,port))

            except:
                time.sleep(2)
                print(Fore.RED+'\n[-] {}:{} Closed!'.format(self.host,port))
        print('\n'+'-' *28)
    def grabber(self,host,grabfile):
        time.sleep(3)
        print(Fore.GREEN + '\n[*] Scanning {} '.format(self.host))
        print('\n' + '-' * 28+'\n')
        port_list = [20, 21, 22, 23, 25, 53, 80, 111, 139, 445]
        for port in port_list:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(1)

            try:
                sock.connect((host, port))
                banner = sock.recv(1024)
                #banner = str(banner).encode('utf-8').decode('utf-8')
                banner = bytes(banner).decode('utf-8').strip('\n')

                with open(grabfile, 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        line = line.strip('\n').encode('utf-8').decode('utf-8')

                        if line in banner:
                            time.sleep(2)
                            print(Fore.GREEN+'[+] '+str(host)+':'+str(port),line+'\n')

            except:
                time.sleep(2)
                print(Fore.RED+'[!] '+str(host)+':'+str(port)+' Not detected!\n')
        print(Fore.GREEN+'-' * 28)
if __name__ == '__main__':

    print("""\n
    ----------------------
    # 1- Port Scanner    #
    # 2- Banner Grabbing #
    # 3- Exit            #
    ----------------------
    """)

    userValue = input('REDBanG >>> ')
    host = input('\n[*] Host/IP: ')  # '192.168.180.128'
    banner_grab = BannerGrab(host)
    if userValue == '1':
        banner_grab.portScanner()

    elif userValue == '2':
        grabfile = input('\n[*] Banner File: ')  # 'vulns.txt'
        banner_grab.grabber(host=host, grabfile=grabfile)

    elif userValue == '3':
        sys.exit(0)

    else:
        print('\n[!] Please check values...')

