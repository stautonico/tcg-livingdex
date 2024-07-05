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

for file in os.listdir("pokemon_data"):
    with open(f"pokemon_data/{file}", 'r') as f:
        data = loads(f.read())

    row_index = int(file.split(".")[0])
    livingdex.write(row_index, 0, data["id"], id_text)
    livingdex.write(row_index, 1, data["name"].title(), pokemon_text)
    livingdex.write(row_index, 2,
                    f"=IMAGE(\"https://raw.githubusercontent.com/stautonico/tcg-livingdex/main/images/{data['id']}/1.jpg\", 2)")

    livingdex.set_column_pixels(2, 2, 63*4)
    livingdex.set_row_pixels(row_index, 88*4)

workbook.close()
