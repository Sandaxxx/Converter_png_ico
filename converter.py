import os
from PIL import Image
from colorama import Fore
from pystyle import Colors, Colorate, Write

banner = """
                       ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
                      ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                      ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
                      ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
                      ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
                       ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

                                 ─══════════════════════════☆☆══════════════════════════─
                                            Developper : https://github.com/Sandaxxx
                                 ─══════════════════════════☆☆══════════════════════════─



                                                                                                     """

def converter_png_ico(filename_png):

    try:
        file = Image.open(filename_png)
        ico_image = file.resize((400, 400))

        ico_image.save('image_file.ico')
        print(Fore.BLUE+"[!]"+Fore.WHITE+" >"+Fore.GREEN+" Successfully Converted!")
        
    except FileNotFoundError:
        print(Fore.BLUE+"[X]"+Fore.WHITE+" >"+Fore.RED+" Error File Path")


if __name__ == "__main__":
    print(Colorate.Horizontal(Colors.purple_to_blue, banner))
    path_png = Write.Input("[+] File path > ", Colors.red_to_purple, interval=0.0025)
    
    converter_png_ico(path_png)
