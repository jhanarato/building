# A script to calculate building material requirements for the stables project

import csv

import insulation, sections

products = insulation.products
products_by_code = [(product["code"],product) for product in products]


# A list of tuples matching insulation product to section to insulate.
product_section_match = [(sections.ne_bedroom_n, insulation.sound_screen_88),
                         (sections.ne_bedroom_e, insulation.sound_screen_88),
                         (sections.ne_bedroom_s, insulation.sound_screen_70),
                         (sections.ne_bedroom_w, insulation.sound_screen_70),

                         (sections.se_bedroom_n, insulation.sound_screen_70),
                         (sections.se_bedroom_e, insulation.sound_screen_88),
                         (sections.se_bedroom_s, insulation.sound_screen_88),
                         (sections.se_bedroom_w, insulation.sound_screen_70),

                         (sections.sw_bedroom_n, insulation.sound_screen_70),
                         (sections.sw_bedroom_e, insulation.sound_screen_70),
                         (sections.sw_bedroom_s, insulation.sound_screen_88),
                         (sections.sw_bedroom_w, insulation.sound_screen_70),

                         (sections.nw_bedroom_n, insulation.sound_screen_88),
                         (sections.nw_bedroom_e, insulation.sound_screen_70),
                         (sections.nw_bedroom_s, insulation.sound_screen_70),
                         (sections.nw_bedroom_w, insulation.sound_screen_70),

                         (sections.nw_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (sections.ne_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (sections.se_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (sections.sw_bedroom_above_ceiling, insulation.gold_hp_wall_90),

                         (sections.nw_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (sections.ne_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (sections.se_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (sections.sw_bedroom_ceiling, insulation.gold_hp_wall_90),

                         (sections.living_e, insulation.sound_screen_88),
                         (sections.living_s, insulation.gold_hp_wall_90),
                         (sections.living_w, insulation.gold_hp_wall_90),
                         (sections.living_ceiling, insulation.gold_hp_ceiling_240),

                         (sections.laundry_partition, insulation.sound_screen_88),
                         (sections.laundry_ceiliing, insulation.gold_hp_ceiling_240),

                         (sections.showers_partition, insulation.sound_screen_88),
                         (sections.showers_ceiliing, insulation.gold_hp_ceiling_240),

                         (sections.disabled_wall, insulation.gold_hp_wall_90),
                         (sections.disabled_ceiling, insulation.gold_hp_ceiling_240)]


# Get a dictionary with the key being the product code
# and the value being the total area of that product.
def get_area_by_code():
    code_to_area = {}

    for product_by_code in products_by_code:
        code_to_area[product_by_code[0]] = 0

    for match in product_section_match:
        section = match[0]
        material = match[1]
        area = section["area"]
        code = material["code"]
        code_to_area[code] += area

    return code_to_area

def display_area_by_product():
    for product in products:
        code = product["code"]
        name = product["name"]
        area = get_area_by_code()[code]
        to_display = "%s - %s - %s" % (code, name, area)
        print(to_display)

def write_area_by_product():
    with open("product_area.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Code", "Product Description", "Area to Cover"])
        for product in products:
            code = product["code"]
            name = product["name"]
            area = get_area_by_code()[code]
            writer.writerow([code, name, area])

write_area_by_product()