
from systemsmanager import SystemsManager

class Menu:

    def greet_user(self):
        print("Hello, which System of Linear Equations are you looking to solve today?")

    def menu(self):
        manager.get_size()
        manager.solve_linear_system()



MainMenu = Menu()
manager=SystemsManager()
MainMenu.greet_user()
MainMenu.menu()

