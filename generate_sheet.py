import xlsxwriter
import os
from json import loads

workbook = xlsxwriter.Workbook("livingdex.xlsx")

livingdex = workbook.add_worksheet("Living Dex")

center_text = workbook.add_format()
center_text.set_align("center")
center_text.set_align("vcenter")

id_text = workbook.add_format({
    # "border": 1,
    "align": "center",
    "valign": "vcenter",
    # Make the text big
    "font_size": 16
})

pokemon_text = workbook.add_format({
    # "border": 1,
    "align": "center",
    "valign": "vcenter",
    # Make the text big
    "font_size": 16
})


livingdex.write(0, 0, "#", center_text)
livingdex.write(0, 1, "Pokémon", center_text)
livingdex.write(0, 2, "Top Pick", center_text)
livingdex.write(0, 3, "Second Pick", center_text)
livingdex.write(0, 4, "Third Pick", center_text)
livingdex.write(0, 5, "Fourth Pick", center_text)

row_itr = 1
for file in os.listdir("pokemon_data"):
    with open(f"pokemon_data/{file}", 'r') as f:
        data = loads(f.read())

    livingdex.write(row_itr, 0, data["id"], id_text)
    livingdex.write(row_itr, 1, data["name"].title(), pokemon_text)
    livingdex.write(row_itr, 2,
                    f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/1.png\", 2)")

    if os.path.exists(f"images/{data['id']}/2.png"):
        livingdex.write(row_itr, 3,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/2.png\", 2)")

    if os.path.exists(f"images/{data['id']}/3.png"):
        livingdex.write(row_itr, 4,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/3.png\", 2)")

    if os.path.exists(f"images/{data['id']}/4.png"):
        livingdex.write(row_itr, 5,
                        f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/4.png\", 2)")




    livingdex.set_column_pixels(2, 2, 63*4)
    livingdex.set_row_pixels(row_itr, 88*4)

workbook.close()
