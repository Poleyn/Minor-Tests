import os
import shutil
import time


with open("path.txt","r") as f:
    path = f.read()
    f.close

def find_file():
    global file_name
    os.system("cls")

    directories = os.scandir(str(path))

    for file in directories:
        if file.is_file():
            print(file.name)
    file_name = input("\n\nLütfen dosya adını ve uzantısını giriniz: ")
    wait_time = input("Kaç dakika bekleyeyim?: ")
    wait_time = int(wait_time) * 60

    copy_file()

def copy_file():
    os.system("cls")
    src_path = path + "\\" + file_name
    dst_path = os.path.expanduser('~/Documents') + "/Biyolojicopy/" + file_name
    try: 
        os.mkdir(os.path.expanduser('~/Documents') + "/Biyolojicopy/") 
        print("hry")
    except OSError as error: 
        pass
    
    
    shutil.copy(src_path, dst_path)
    print('Copied') 


if __name__ == '__main__':
    print("""

██████╗ ██╗██╗   ██╗ ██████╗ ██╗      ██████╗      ██╗██╗                               
██╔══██╗██║╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗     ██║██║                               
██████╔╝██║ ╚████╔╝ ██║   ██║██║     ██║   ██║     ██║██║                               
██╔══██╗██║  ╚██╔╝  ██║   ██║██║     ██║   ██║██   ██║██║                               
██████╔╝██║   ██║   ╚██████╔╝███████╗╚██████╔╝╚█████╔╝██║                               
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚════╝ ╚═╝                               
                                                                                        
 █████╗ ██████╗ ████████╗██╗██╗  ██╗    ███████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗    
██╔══██╗██╔══██╗╚══██╔══╝██║██║ ██╔╝    ██╔════╝██╔═══██╗██╔══██╗██║   ██║████╗  ██║    
███████║██████╔╝   ██║   ██║█████╔╝     ███████╗██║   ██║██████╔╝██║   ██║██╔██╗ ██║    
██╔══██║██╔══██╗   ██║   ██║██╔═██╗     ╚════██║██║   ██║██╔══██╗██║   ██║██║╚██╗██║    
██║  ██║██║  ██║   ██║   ██║██║  ██╗    ███████║╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    
                                                                                        
██████╗ ███████╗ ██████╗ ██╗██╗               ▄▄▄       ███▄    █  ▒█████   ███▄    █  ██▓ ███▄ ▄███▓                                      
██╔══██╗██╔════╝██╔════╝ ██║██║              ▒████▄     ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▓██▒▓██▒▀█▀ ██▒                                      
██║  ██║█████╗  ██║  ███╗██║██║              ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒██▒▓██    ▓██░                                      
██║  ██║██╔══╝  ██║   ██║██║██║              ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒░██░▒██    ▒██                                       
██████╔╝███████╗╚██████╔╝██║███████╗          ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░██░▒██▒   ░██▒                                      
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚══════╝          ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ░  ░
                                               ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░░  ░      ░
                                               ░   ▒      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░  ▒ ░░      ░   
                                                   ░  ░         ░     ░ ░           ░  ░         ░  
    \n\n\n\n\n\n\n 
    """)
    print("Sorumluluk kabul etmiyom.")
    wait_time = input("İşlemi kaç dakika sonra başlatayım?: ")
    wait_time = int(wait_time) * 60

    time.sleep(wait_time)

    find_file()