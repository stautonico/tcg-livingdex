import xlsxwriter
import os
from json import loads

workbook = xlsxwriter.Workbook("livingdex.xlsx")

livingdex = workbook.add_worksheet("Living Dex")

center_text = workbook.add_format()
center_text.set_align("center")
center_text.set_align("vcenter")

title_text = workbook.add_format({
    "align": "center",
    "valign": "vcenter",
    "border": 1,
    "font_size": 24,
    "bg_color": "#adadad"
})

id_text = workbook.add_format({
    "align": "center",
    "valign": "vcenter",
    # Make the text big
    "font_size": 26
})

pokemon_text = workbook.add_format({
    # "border": 1,
    "align": "center",
    "valign": "vcenter",
    # Make the text big
    "font_size": 30
})


set_name_num_format = workbook.add_format({
    "align": "center",
    "valign": "vcenter",
    "font_size": 14,
    "bg_color": "#adadad"
})
set_name_num_format.set_bottom(1)
set_name_num_format.set_left(1)
set_name_num_format.set_right(1)

livingdex.write(0, 0, "#", title_text)
livingdex.write(0, 1, "Pokémon", title_text)
livingdex.write(0, 2, "Top Pick", title_text)
livingdex.write(0, 3, "Second Pick", title_text)
livingdex.write(0, 4, "Third Pick", title_text)
livingdex.write(0, 5, "Fourth Pick", title_text)
livingdex.write(0, 6, "Owned", title_text)

row_itr = 1
for file in os.listdir("pokemon_data"):
    with open(f"pokemon_data/{file}", 'r') as f:
        data = loads(f.read())

    if not os.path.exists(f"images/{data['id']}/meta.json"):
        json_payload = {
            "1": {
                "img": "",
                "set_name": "",
                "set_num": ""
            },
            "2": {
                "img": "",
                "set_name": "",
                "set_num": ""
            },
            "3": {
                "img": "",
                "set_name": "",
                "set_num": ""
            },
            "4": {
                "img": "",
                "set_name": "",
                "set_num": ""
            }
        }
    else:
        with open(f"images/{data['id']}/meta.json", "r") as f:
            json_payload = loads(f.read())

    livingdex.write(row_itr, 0, data["id"], id_text)
    livingdex.write(row_itr, 1, data["name"].title(), pokemon_text)
    livingdex.write(row_itr, 2,
                    f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/1.png\", 2)")
    row_itr += 1
    livingdex.write(row_itr, 2, json_payload["1"]["set_name"] + "\n" + "#" + json_payload["1"]["set_num"],
                    set_name_num_format)
    row_itr -= 1

    if os.path.exists(f"images/{data['id']}/2.png"):
        livingdex.write(row_itr, 3,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/2.png\", 2)")
        row_itr += 1
        livingdex.write(row_itr, 3, json_payload["2"]["set_name"] + "\n" + "#" + json_payload["2"]["set_num"],
                        set_name_num_format)
        row_itr -= 1

    if os.path.exists(f"images/{data['id']}/3.png"):
        livingdex.write(row_itr, 4,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/3.png\", 2)")
        row_itr += 1
        livingdex.write(row_itr, 4, json_payload["3"]["set_name"] + "\n" + "#" + json_payload["3"]["set_num"],
                        set_name_num_format)
        row_itr -= 1

    if os.path.exists(f"images/{data['id']}/4.png"):
        livingdex.write(row_itr, 5,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/4.png\", 2)")
        row_itr += 1
        livingdex.write(row_itr, 5, json_payload["4"]["set_name"] + "\n" + "#" + json_payload["4"]["set_num"],
                        set_name_num_format)
        row_itr -= 1

    livingdex.write(row_itr, 6, "FALSE")

    # If the 7th column in the row is "TRUE", make the background green
    # otherwise, make the background red

    livingdex.conditional_format(row_itr, 0, row_itr, 6, {
        "type": "formula",
        "criteria": f'=COUNTIF($G{row_itr+1}, "TRUE") = 1',
        "format": workbook.add_format({"bg_color": "#00FF00"})
    })

    livingdex.conditional_format(row_itr, 0, row_itr, 6, {
        "type": "formula",
        "criteria": f'=COUNTIF($G{row_itr+1}, "FALSE") = 1',
        "format": workbook.add_format(
            {"bg_color": "#FF0000", "font_color": "#FFFFFF"})
    })

    livingdex.set_column_pixels(2, 5, 63 * 4)
    livingdex.set_row_pixels(row_itr, 88 * 4)
    row_itr += 3

workbook.close()
