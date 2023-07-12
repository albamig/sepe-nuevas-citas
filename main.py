from time import sleep
import requests
import os

data = {
    'idCliente': '39',
    'idGrupoServicio': '41',
    'idTipoAtencion': '1',
    'codigoPostal': '28028',
    'latOrigen': '40.431732',
    'lngOrigen': '-3.66524',
    'hasDependientes': '0',
}

while True:
    response = requests.post(
        'https://citaprevia-sede.sepe.gob.es/citapreviasepe/cita/cargaOficinasMapa',
        data=data
    )
    print("Petición enviada")

    for ofi in response.json()['listaOficina']:
        if ofi['primerHuecoDisponible']:
            lugar = ofi['oficina']
            fecha = ofi['primerHuecoDisponible']

            print(f"Nueva cita en {lugar} {fecha}")
            os.system(f'notify-send "¡Nueva cita!" "En {lugar} el {fecha}"')

    sleep(10)
