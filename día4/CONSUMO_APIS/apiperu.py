import requests

TOKEN = 'b83033aa95235c7c8e7036b0df7c52a0858ce2ba4df547aa231959196457962c'
API_URL = 'https://apiperu.dev/api/ruc'

ruc = input('INGRESE NRO DE RUC : ')
data_request = {
    "ruc":ruc
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL,
                         json=data_request,
                         headers=headers)

if response.status_code == 200:
    data = response.json()['data']
    print(f"RUC : {ruc}")
    print(f"Razón social : {data['nombre_o_razon_social']}")
    print(f'Dirección : {data["direccion"]}')
    print(f'Distrito : {data["distrito"]}')
    print(f'Provincia : {data["provincia"]}')
    print(f'Departamento : {data["departamento"]}')
    print(f'ubigeo : {data["ubigeo_sunat"]}')
    