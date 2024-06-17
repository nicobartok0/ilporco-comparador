

class Articulo:
    def __init__(self) -> None:
        self.codigo = 0
        self.cods_pricely = {
            'CAGNOLI': '',
            'NAHUEL': '',
            'DOINA': '',
            'LAS DINAS': '',
            'CABAÑAS ARGENTINAS': '',
            'OTROS': ''
        }
        self.nombre = ''
        self.sku = ''
        self.costo = 0.0
        self.precios = {
            'CAGNOLI': 0,
            'LOS CALVOS': 0,
            'NAHUEL': 0,
            'DOINA': 0,
            'LAS DINAS': 0,
            'CABAÑAS ARGENTINAS': 0,
            'OTROS': 0
        }