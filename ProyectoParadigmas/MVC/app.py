from vista import *
from controlador import *
class App:
    """docstring for App."""
    def __init__(self):
        self.opciones = [
            ["Buscar Clientes",self.buscar_cliente],
            ["Buscar Articulos",self.buscar_articulo],
            ["Mostrar Pedidos",self.mostrar_pedidos],
        ]
        # IDEA: CREAR GRUPOS DE MENU PARA PODER ACCEDER A DISTINTAS ACCIONES

        self.control=Controlador()
        self.vista=Vista()
        #self.iniciar_sesion()

    def mostrar_menu(self):
        self.vista.mostrar_opciones(self.opciones)

    def iniciar_sesion(self):

        usu = input("Introduzca su nombre de usuario")
        if(not self.control.definir_usuario_actual(usu)):
            print("Usuario inexistente")
            self.iniciar_sesion()
        else :
            print("Bienvenido")
            self.cargar_opciones(type(self.control.usuario.rol).__name__)

    def cerrar_sesion(self):

        pass

    def cargar_opciones(self,usu):
        if usu== "EmpleadoFacturador":
            self.opciones.append(["Elegir Pedido",self.elegir_pedido_usuario])
            self.opciones.append(["Preparar Pedido",self.preparar_pedido_usuario])
            self.opciones.append(["Facturar Pedido",self.facturar_pedido_usuario])
            self.opciones.append(["Cancelar Pedido",self.cerrar_pedido_usuario])
            self.opciones.append(["Cerrar Pedido",self.cerrar_pedido_usuario])


            pass
        elif usu == "EmpleadoRepartidor":
            self.opciones.append(["Elegir Pedido",self.elegir_pedido_usuario])
            self.opciones.append(["Preparar Pedido",self.preparar_pedido_usuario])
            self.opciones.append(["Facturar Pedido",self.facturar_pedido_usuario])
            self.opciones.append(["Cancelar Pedido",self.cerrar_pedido_usuario])
            self.opciones.append(["Cerrar Pedido",self.cerrar_pedido_usuario])


            pass
        elif usu == "EmpleadoReceptor" :
            self.opciones.append(["Obtener Pedidos a Entregar",self.obtener_pedidos_entregables])
            self.opciones.append(["Ver pedidos a entregar ",self.obtener_pedidos_a_entregar])
            self.opciones.append(["Entregar Pedido",self.entregar_pedido_usuario])


        else :
            #crear excepcion de error
            pass

    def entrada(self,usu):
        self.control.definir_usuario_actual(usu)

    def buscar_cliente(self):
        self.vista.desplegar_mensaje("Introduzca el nombre del cliente a buscar (enter para listar todo)")
        cliente = input(" > ")
        self.control.buscar_cliente(cliente)

    def buscar_articulo(self):
        self.vista.desplegar_mensaje("Introduzca el nombre del articulo a buscar (enter para listar todo)")
        cliente = input(">")
        self.control.buscar_cliente(cliente)

    def mostrar_pedidos(self):
        self.vista.desplegar_lista(self.control.mostrar_pedidos())

    def crear_pedido(self):
        cliente_temp={}
        self.vista.desplegar_mensaje("Introduzca el nombre del cliente")
        cliente_temp["nombre"]=input(">")
        self.vista.desplegar_mensaje("Introduzca el R.U.C. del cliente")
        cliente_temp["ruc"]=input(">")
        self.vista.desplegar_mensaje("Introduzca la direccion del cliente")
        cliente_temp["direccion"]=input(">")
        self.vista.desplegar_mensaje("Introduzca el numero de celular del cliente")
        cliente_temp["direccion"]=input(">")

    def crear_cliente(self):
        cliente_temp={}
        self.vista.desplegar_mensaje("Introduzca el nombre del cliente")
        cliente_temp["nombre"]=input(">")
        self.vista.desplegar_mensaje("Introduzca el R.U.C. del cliente")
        cliente_temp["ruc"]=input(">")
        self.vista.desplegar_mensaje("Introduzca la direccion del cliente")
        cliente_temp["direccion"]=input(">")
        self.vista.desplegar_mensaje("Introduzca el numero de celular del cliente")
        cliente_temp["direccion"]=input(">")

    def agregar_articulo_pedido(self):
        pass

    def cancelar_pedido_usuario(self):
        pass

    def cerrar_pedido_usuario(self):
        pass

    def elegir_pedido_usuario(self):
        pass

    def preparar_pedido_usuario(self):
        pass

    def facturar_pedido_usuario(self):
        pass

    def entregar_pedido_usuario(self):
        pass

    def obtener_pedidos_entregables(self):
        pass
    def obtener_pedidos_a_entregar(self):
        pass
