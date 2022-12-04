import json
from parametros import GITHUB_BASE_URL, GITHUB_REPO_NAME, GITHUB_REPO_OWNER
from parametros import GITHUB_USERNAME
from parametros import POKEMON_BASE_URL, POKEMON_NUMERO
import requests


def get_pokemon():
        #Completar
        url = POKEMON_BASE_URL.format(f"pokemon/{POKEMON_NUMERO}/")
        response = requests.get(url)
        pokemon = []
        status = int(response.status_code)
        if int(response.status_code) == 200:
                datos = response.json()
                pokemon.append(datos["name"])
                pokemon.append(datos["weight"])
                pokemon.append(datos["height"])
                lista_types = []
                dicc_1 = datos["types"]
                for i in range(0, len(dicc_1)):
                        dicc_2 = dicc_1[i]
                        dicc_3 = dicc_2["type"]
                        dicc_4 = dicc_3["name"]
                        lista_types.append(dicc_4)
                pokemon.append(lista_types)
                return status, pokemon
        return status, pokemon
        pass

def post_issue(token, pokemon):
        #Completar
        header = {
                'Authorization' : 'token ' + token,
                'Accept': 'application/vnd.github.v3+json'
        }
        text = {
                'title' : GITHUB_USERNAME,
                'body' : str(pokemon)
                }
        data1 = json.dumps(text)
        url = GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues")
        print(url)
        resp = requests.post(url, data=data1, headers=header)
        print(resp.status_code)
        if resp.status_code == 201:
                return resp.status_code, resp.json()["number"]
        else:
                return resp.status_code, 0
        


def put_lock_issue(token, numero_issue):
        #Completar
        pass


def delete_lock_issue(token, numero_issue):
        #Completar
        pass
