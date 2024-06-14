
from lector import Lector
from articulo import Articulo
from valuador import Valuador_Pricely
#from valuador_asincrono import Valuador_Pricely
from threading import Thread

class Operador:
    def __init__(self) -> None:
        self.articulos = {}
        self.sesiones = {}
        

    def definir_hilo_buscador(self):
        self.hilo_buscador = Thread(target=self.valuador.buscar_precios, daemon=True)
        #self.hilo_buscador = Thread(target=self.valuador.correr_valuador, daemon=True)

    def crear_lector(self, nombre, ruta):
        self.lector = Lector(nombre, ruta)
    
    def crear_valuador(self):
        self.valuador = Valuador_Pricely()

    def crear_articulos(self):
        articulos = self.lector.obtener_datos()
        articulos.pop(0)
        for articulo_dict in articulos:
            articulo = Articulo()
            articulo.nombre = articulo_dict['nombre']
            articulo.sku = articulo_dict['SKU']
            articulo.costo = articulo_dict['costo']
            articulo.codigo = int(articulo_dict['codigo'])
            self.articulos[articulo.codigo] = articulo

    def inicializar(self):
        self.crear_valuador()
        self.valuador.cargar_articulos(self.articulos)
        self.lector.intercode(self.articulos)
        self.definir_hilo_buscador()
        self.hilo_buscador.start()
        return self.articulos