from core.banner import get_banner
from core.help import Help
from core.menu import Menu
from core.output_manager import Output_Manager_Menu


def main():
    while True:

        print(get_banner())

        print("""
        version : 1.5
        number of tools:12

        Enter help/h to get help
        Enter Menu/m to go to the menu
        Enter Output/o to open Output Manager
        Enter E/Exit to exit the program
        """)

        W = input("Enter your option: ")

        if W.lower() in ("m", "menu"):

            result = Menu()

            if result == "exit":
                break

        elif W.lower() == "o" or W.lower() == "output":
            result = Output_Manager_Menu()

            if result == "exit":
                break

        elif W.lower() in ("e", "exit"):

            break

        elif W.lower() == "h" or W.lower() == "help":

            result = Help()

            if result == "exit":
                break

if __name__ == "__main__":
    main()
