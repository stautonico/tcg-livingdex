from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from json import loads

nums = [x for x in range(1, 1025 + 1)]

replacements = {
    "nidoran-f": "nidoran f",
    "nidoran-m": "nidoran m",
    "mr-mime": "mr. mime",
    "ho-oh": "ho-oh",
    "deoxys-normal": "deoxys",
    "wormadam-plant": "wormadam",
    "mime-jr": "mime jr",
    "porygon-z": "porygon-z",
    "giratina-altered": "giratina",
    "shaymin-land": "shaymin",
    "basculin-red-striped": "basculin",
    "darmanitan-standard": "darmanitan",
    "tornadus-incarnate": "tornadus",
    "thundurus-incarnate": "thundurus",
    "landorus-incarnate": "landorus",
    "keldeo-ordinary": "keldeo",
    "meloetta-aria": "meloetta",
    "meowstic-male": "meowstic",
    "aegislash-shield": "aegislash",
    "pumpkaboo-average": "pumpkaboo",
    "gourgeist-average": "gourgeist",
    "zygarde-50": "zygarde",
    "oricorio-baile": "oricorio",
    "lycanroc-midday": "lycanroc",
    "wishiwashi-solo": "wishiwashi",
    "type-null": "type: null",
    "minior-red-meteor": "minior",
    "mimikyu-disguised": "mimikyu",
    "jangmo-o": "jangmo-o",
    "hakamo-o": "hakamo-o",
    "kommo-o": "kommo-o",
    "tapu-koko": "tapu koko",
    "tapu-lele": "tapu lele",
    "tapu-bulu": "tapu bulu",
    "tapu-fini": "tapu fini",
    "toxtricity-amped": "toxtricity",
    "mr-rime": "mr. rime",
    "eiscue-ice": "eiscue",
    "indeedee-male": "indeedee",
    "morpeko-full-belly": "morpeko",
    "urshifu-single-strike": "urshifu",
    "basculegion-male": "basculegion",
    "enamorus-incarnate": "enamorus",
    "great-tusk": "great tusk",
    "scream-tail": "scream tail",
    "brute-bonnet": "brute bonnet",
    "flutter-mane": "flutter mane",
    "slither-wing": "slither wing",
    "sandy-shocks": "sandy shocks",
    "iron-treads": "iron treads",
    "iron-bundle": "iron bundle",
    "iron-hands": "iron hands",
    "iron-jugulis": "iron jugulis",
    "iron-moth": "iron moth",
    "iron-thorns": "iron thorns",
    "wo-chien": "wo-chien",
    "chien-pao": "chien-pao",
    "ting-lu": "ting-lu",
    "chi-yu": "chi-yu",
    "roaring-moon": "roaring moon",
    "iron-valiant": "iron valiant",
    "walking-wake": "walking wake",
    "iron-leaves": "iron leaves",
    "gouging-fire": "gouging fire",
    "raging-bolt": "raging bolt",
    "iron-boulder": "iron boulder",
    "iron-crown": "iron crown",
}


def num_to_name(number):
    with open(f"pokemon_data/{number}.json", "r") as f:
        data = loads(f.read())

    if "-" in data["name"]:
        return replacements[data["name"]]

    return data["name"]


# Function to create PDF with name tags
def create_name_tags(output_file='pokemon_name_tags.pdf'):
    # PDF settings
    page_width, page_height = letter
    c = canvas.Canvas(output_file, pagesize=letter)

    # Tag settings
    tags_per_page = 156  # Increase the number of tags per page
    tag_width = 100
    tag_height = 30
    margin = 0  # Smaller margin to fit more tags
    horizontal_spacing = 0  # No horizontal spacing
    vertical_spacing = 0  # No vertical spacing

    for i, pkmn_num in enumerate(nums):
        if i > 0 and i % tags_per_page == 0:
            c.showPage()  # Start a new page

        page_number = i // tags_per_page
        local_index = i % tags_per_page

        # Calculate tag position
        row = local_index // 6
        col = local_index % 6
        x = margin + col * (tag_width + horizontal_spacing)
        y = page_height - margin - (row + 1) * (tag_height + vertical_spacing)

        # Draw the tag
        c.rect(x, y, tag_width, tag_height)
        c.drawString(x + 5, y + 10, f"#{pkmn_num} {num_to_name(pkmn_num).title()}")

    c.save()


create_name_tags()
