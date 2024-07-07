import os.path

from flask import Flask, render_template, request
from json import loads, dumps
from PIL import Image
import requests
import shutil

app = Flask(__name__, template_folder="web_templates")


def download_file(url, saveto):
    r = requests.get(url, stream=True)

    with open(saveto, "wb") as of:
        shutil.copyfileobj(r.raw, of)


def get_file_extension(path):
    splt = path.split(".")
    return splt[-1]


def convert_image(img):
    if not img.endswith(".png"):
        im = Image.open(img)
        filename = img.split(".")[:-1]
        filename = "".join(filename)
        filename += ".png"
        im.save(filename)
        os.remove(img)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/name_by_number/<string:number>")
def name_by_number(number):
    try:
        with open(f"pokemon_data/{number}.json", "r") as f:
            data = loads(f.read())

        return data["name"]
    except Exception:
        return "invalid"


@app.route("/images_exist/<string:number>")
def images_exist(number):
    if os.path.exists(f"images/{number}"):
        return "yes"
    else:
        return "no"


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json

        if not os.path.exists(f"images/{data['pokedexNum']}"):
            os.mkdir(f"images/{data['pokedexNum']}")

        payload = {}

        filename = "1." + get_file_extension(data["card1"]["img"])
        file_path = os.path.join("images", str(data["pokedexNum"]), filename)
        download_file(data["card1"]["img"], file_path)
        convert_image(file_path)
        payload[1] = {
            "img": file_path,
            "set_name": data["card1"]["set"],
            "set_num": data["card1"]["num"]
        }

        if data["card2"]["img"] != "":
            filename = "2." + get_file_extension(data["card2"]["img"])
            file_path = os.path.join("images", str(data["pokedexNum"]), filename)
            download_file(data["card2"]["img"], file_path)
            convert_image(file_path)
            payload[2] = {
                "img": file_path,
                "set_name": data["card2"]["set"],
                "set_num": data["card2"]["num"]
            }

        if data["card3"]["img"] != "":
            filename = "3." + get_file_extension(data["card3"]["img"])
            file_path = os.path.join("images", str(data["pokedexNum"]), filename)
            download_file(data["card3"]["img"], file_path)
            convert_image(file_path)
            payload[3] = {
                "img": file_path,
                "set_name": data["card3"]["set"],
                "set_num": data["card3"]["num"]
            }

        if data["card4"]["img"] != "":
            filename = "4." + get_file_extension(data["card4"]["img"])
            file_path = os.path.join("images", str(data["pokedexNum"]), filename)
            download_file(data["card4"]["img"], file_path)
            convert_image(file_path)
            payload[4] = {
                "img": file_path,
                "set_name": data["card4"]["set"],
                "set_num": data["card4"]["num"]
            }

        with open(os.path.join("images", str(data["pokedexNum"]), "meta.json"), "w") as f:
            f.write(dumps(payload))

        return "done"
    except Exception as e:
        print(e)
        return f"fail"


app.run(debug=True)
