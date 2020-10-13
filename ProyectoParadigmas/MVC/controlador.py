from proyecto import *
from vista import *
class Controlador():
    #usuario=""
    def __init__(self):
        self.usuario=None
        self.empresa=Empresa()

    def definir_usuario_actual(self,usu):
        #buscar el usuario que se ingresa
        temp= [ usuario for usuario in self.empresa.empleados if ( usuario.nombre == usu )]
        if(len(temp)>0):
            self.usuario = temp[0]
            return True
        else:
            return False


    def buscar_articulo(self):
        self.vista.desplegar_mensaje("Ingrese un articulo")
        self.vista.desplegar_lista(self.empresa.buscar_articulo())

    def mostrar_pedidos(self):
        self.vista.desplegar_mensaje("Pedidos Registrados")
        self.vista.desplegar_lista(self.empresa.obtener_pedidos())

    def buscar_cliente(self,nombre):
        self.empresa.buscar_cliente(nombre)

    def registrar_nuevo_nuevo_cliente(self,cliente):
        self.usuario.rol.registrar_cliente(empresa.lista_cliente,cliente)
        #crear vista para mostrar los datos del cliente
        pass
    def crear_pedido(self,cliente,direccion_entrega):
        self.usuario.registrar_pedido(cliente,direccion_entrega)
        self.opciones.append(["Agregar Articulo ",self.registrar_nuevo_nuevo_cliente])
        #crear vista para mostrar pedido
        pass

    def agregar_articulos_a_pedido_actual(self,articulo):
        self.usuario.agregar_articulo(articulo)

    def confirmar_pedido(self):
        self.usuario.cerrar_pedido(self.empresa.lista_pedido)
        self.opciones= [opcion for opcion in self.opciones if(opcion[0]!="Agregar Articulo")]
