from application.controller.usuario_controller import UsuarioController

class indexController:
    def __init__(self):
        self.usuario_controller = UsuarioController()
    
    def inicializar_biblioteca(self):
        self.usuario_controller.inicializa()

def main():
    index = indexController()
    index.inicializar_biblioteca()

if __name__ == "main":
    main()