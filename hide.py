from colorama import init, Fore, Back, Style

def banner():
    init()

    banner = """
    """ + Fore.RED +   """██╗  ██╗███████╗██╗  ██╗██╗  ██╗██╗██████╗ ███████╗██████╗ """ + """    
    """ + Fore.RED +   """██║  ██║██╔════╝╚██╗██╔╝██║  ██║██║██╔══██╗██╔════╝██╔══██╗""" + """ 
    """ + Fore.WHITE + """███████║█████╗   ╚███╔╝ ███████║██║██║  ██║█████╗  ██████╔╝""" + """  
    """ + Fore.WHITE + """██╔══██║██╔══╝   ██╔██╗ ██╔══██║██║██║  ██║██╔══╝  ██╔══██╗""" + """
    """ + Fore.BLUE + """██║  ██║███████╗██╔╝ ██╗██║  ██║██║██████╔╝███████╗██║  ██║""" + """
    """ + Fore.BLUE + """╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝""" + """
    """ + Fore.RESET
                                                
    print(banner)


banner()

#this is the function to hide text inside the image
def hide():
    img = input("what image would you like to use : ") 
    txt = input("what do you want to hide : ")
    with open(img, 'ab') as f:
        f.write(bytes(txt + " ", encoding= 'utf-8'))
    print("added : " + txt + " inside the image, returning to menu..")

#this is the function to extract the text from an image
def extract():
    img = input("what image would you like to use : ") 
    with open(img, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)
        print(f.read())

action = input("[1] Hide text\n[2] Extract text \n[99] Exit\nYou want to : ")

while True:

    if action == "1":
        hide()

    elif action == "2":
        extract()

    elif action == "99":
        break

    else:
        print("Please pick a valid number. returning to menu...")

    action = input("[1] Hide text\n[2] Extract text \n[99] Exit\nYou want to : ")

