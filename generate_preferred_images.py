import os
import re
import requests
import shutil
from PIL import Image
from json import dumps

# TODO: Write a web interface that makes this easier to do :)


def validate_link(link):
    if link == "":
        return True  # For < 4 preferred cards

    regex = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, link) is not None


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


while True:
    pkmn_id = input("Enter the Pokemon's pokedex number> ")

    try:
        pkmn_id = int(pkmn_id)
    except Exception as e:
        print(f"Invalid pokedex number")
        exit(1)

    # Check if the id exists, then confirm overwrite
    if os.path.exists(f"images/{pkmn_id}"):
        overwrite = input(f"Preferred images already exist, overwrite? [y/N] ")

        if overwrite != "y":
            print("Bye!")
            exit()

    if not os.path.exists(f"images/{pkmn_id}"):
        os.mkdir(f"images/{pkmn_id}")

    while True:
        link_1 = input("Enter the image url if your first choice> ")

        if not validate_link(link_1):
            print(f"Provided link is invalid")
        else:
            set_name_1 = input("Enter the set name the card belongs to: ")
            set_num_1 = input("Enter the card num in the set: ")

            break

    while True:
        link_2 = input("Enter the image url if your second choice (leave blank for no preference)> ")

        if not validate_link(link_2):
            print(f"Provided link is invalid")
        else:
            if link_2 != "":
                set_name_2 = input("Enter the set name the card belongs to: ")
                set_num_2 = input("Enter the card num in the set: ")
            break

    while True:
        link_3 = input("Enter the image url if your third choice (leave blank for no preference)> ")

        if not validate_link(link_3):
            print(f"Provided link is invalid")
        else:
            if link_3 != "":
                set_name_3 = input("Enter the set name the card belongs to: ")
                set_num_3 = input("Enter the card num in the set: ")
            break

    while True:
        link_4 = input("Enter the image url if your fourth choice (leave blank for no preference)> ")

        if not validate_link(link_4):
            print(f"Provided link is invalid")
        else:
            if link_4 != "":
                set_name_4 = input("Enter the set name the card belongs to: ")
                set_num_4 = input("Enter the card num in the set: ")
            break

    # Now dump the json information
    payload = {}

    filename = "1." + get_file_extension(link_1)
    file_path = os.path.join("images", str(pkmn_id), filename)
    download_file(link_1, file_path)
    convert_image(file_path)
    payload[1] = {
        "img": file_path,
        "set_name": set_name_1,
        "set_num": set_num_1
    }

    if link_2 != "":
        filename = "2." + get_file_extension(link_1)
        file_path = os.path.join("images", str(pkmn_id), filename)
        download_file(link_2, file_path)
        convert_image(file_path)
        payload[2] = {
            "img": file_path,
            "set_name": set_name_2,
            "set_num": set_num_2
        }

    if link_3 != "":
        filename = "3." + get_file_extension(link_1)
        file_path = os.path.join("images", str(pkmn_id), filename)
        download_file(link_3, file_path)
        convert_image(file_path)
        payload[3] = {
            "img": file_path,
            "set_name": set_name_3,
            "set_num": set_num_3
        }

    if link_4 != "":
        filename = "4." + get_file_extension(link_1)
        file_path = os.path.join("images", str(pkmn_id), filename)
        download_file(link_4, file_path)
        convert_image(file_path)
        payload[4] = {
            "img": file_path,
            "set_name": set_name_4,
            "set_num": set_num_4
        }

    with open(os.path.join("images", str(pkmn_id), "meta.json"), "w") as f:
        f.write(dumps(payload))

    print("All done")
    again = input("Would you like to add another? [Y/n] ")

    if again != "y":
        print("Bye!")
        exit()
