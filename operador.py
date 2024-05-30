
from lector import Lector
from articulo import Articulo

class Operador:
    def __init__(self) -> None:
        self.articulos = {}
        self.sesiones = {}

    def crear_lector(self, nombre, ruta):
        self.lector = Lector(nombre, ruta)

    def crear_articulos(self):
        articulos = self.lector.obtener_datos()
        articulos.pop(0)
        for articulo_dict in articulos:
            articulo = Articulo()
            articulo.nombre = articulo_dict['nombre']
            articulo.sku = articulo_dict['SKU']
            articulo.costo = articulo_dict['costo']
            articulo.codigo = articulo_dict['codigo']
            self.articulos[articulo.codigo] = articulo

    def inicializar(self):
        pass