import requests


class Cotizacion:

    @staticmethod
    def get_cotizacion_dolar_blue():
        cotizacion = float(0)
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        for coti in r.json():
            if coti['casa']['nombre'] == 'Dolar Blue':
                cotizacion = float(coti['casa']['compra'].replace(".","").replace(",","."))
        return cotizacion