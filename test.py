import requests
from time import sleep
from json import dumps

for x in range(1, 1200):
    try:
        print(x)
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")

        json = r.json()

        with open(f"pokemon_data/{x}.json", "w") as f:
            f.write(dumps(json))

        sleep(0.25)

    except Exception as e:
        print(f"[WARN] {x} FAILED! ({e})")
