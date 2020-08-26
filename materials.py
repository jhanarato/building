# A script to calculate building material requirements for the stables project

import csv

# Insulation products
sound_screen_70 = {"name" : "Bradford SoundScreen Wall Batts 70mm",
               "thickness" : 70,
               "length" : 1160,
               "width" : 580,
               "r-value" : 2,
               "pack-pieces" : 9,
               "pack-meters-sqr" : 6.1,
               "pack-coverage" : 6.8,
               "code" : "182313" }

sound_screen_88 = {"name" : "Bradford SoundScreen Wall Batts 88mm",
               "thickness" : 88,
               "length" : 1160,
               "width" : 580,
               "r-value" : 2.5,
               "pack-pieces" : 7,
               "pack-meters-sqr" : 4.7,
               "pack-coverage" : 5.3,
               "code" : "182286" }

gold_hp_ceiling_240 = {"name" : "Bradford Gold High-Performance Ceiling Batts 240mm",
               "thickness" : 240,
               "length" : 1160,
               "width" : 580,
               "r-value" : 5,
               "pack-pieces" : 8,
               "pack-meters-sqr" : 5.4,
               "pack-coverage" : 6.1,
               "code" : "105419" }

gold_hp_wall_90 = {"name" : "Bradford Gold High-Performance Wall Batts 90mm R2.5",
                   "thickness" : 90,
                   "length" : 1160,
                   "width" : 570,
                   "r-value" : 2.5,
                   "pack-pieces" : 9,
                   "pack-meters-sqr" : 6,
                   "pack-coverage" : 6.7,
                   "code" : "181471" }



products = [sound_screen_70, sound_screen_88, gold_hp_ceiling_240, gold_hp_wall_90]
products_by_code = [(product["code"],product) for product in products]


# Sections to insulate
ne_bedroom_n = {"name" : "Northeast Bedroom, North Wall", "area" : 5.8 }
ne_bedroom_e = {"name" : "Northeast Bedroom, East Wall", "area" : 7.9}
ne_bedroom_s = {"name" : "Northeast Bedroom, South Wall", "area" : 7.8}
ne_bedroom_w = {"name" : "Northeast Bedroom, West Wall", "area" : 11.0}

se_bedroom_n = {"name" : "Southeast Bedroom, North Wall", "area" : 7.8 }
se_bedroom_e = {"name" : "Southeast Bedroom, East Wall", "area" : 7.9}
se_bedroom_s = {"name" : "Southeast Bedroom, South Wall", "area" : 5.8}
se_bedroom_w = {"name" : "Southeast Bedroom, West Wall", "area" : 11.0}

sw_bedroom_n = {"name" : "Southwest Bedroom, North Wall", "area" : 7.8 }
sw_bedroom_e = {"name" : "Southwest Bedroom, East Wall", "area" : 11.0}
sw_bedroom_s = {"name" : "Southwest Bedroom, South Wall", "area" : 4.1}
sw_bedroom_w = {"name" : "Southwest Bedroom, West Wall", "area" : 11.0}

nw_bedroom_n = {"name" : "Northwest Bedroom, North Wall", "area" :  2.8}
nw_bedroom_e = {"name" : "Northwest Bedroom, East Wall", "area" : 11.0}
nw_bedroom_s = {"name" : "Northwest Bedroom, South Wall", "area" : 4.1};
nw_bedroom_w = {"name" : "Northwest Bedroom, West Wall", "area" : 8.2}

ne_bedroom_ceiling = {"name" : "Northeast Bedroom, Ceiling",  "area" : 14.0 }
se_bedroom_ceiling = {"name" : "Southeast Bedroom, Ceiling",  "area" : 14.0 }
sw_bedroom_ceiling = {"name" : "Southwest Bedroom, Ceiling",  "area" : 14.0 }
nw_bedroom_ceiling = {"name" : "Northwest Bedroom, Ceiling",  "area" : 14.0 }

living_e = {"name" : "Living Area, East Wall, Adjacent to Bedroom", "area" : 17.6}
living_s = {"name" : "Living Area, South Wall", "area" : 20.6}
living_w = {"name" : "Living Area, West Wall, Main Entrance", "area" : 9.2}
living_ceiling = {"name" : "Living Area, Raked Ceiling", "area" : 60.5}

laundry_partition = {"name" : "Toilets and Laundry Partition Walls", "area" : 11.5}
laundry_ceiliing = {"name" : "Toilets and Laundry Ceiling", "area" : 7.0}

showers_partition = {"name" : "Showers Partition Walls", "area" : 7.5}
showers_ceiliing = {"name" : "Showers Ceiling", "area" : 8.1}

disabled_wall = {"name" : "Disabled bathroom wall", "area" : 6.9}
disabled_ceiling = {"name" : "Disabled bathroom ceiling", "area" : 9.6}

# A list of tuples matching insulation product to section to insulate.
product_section_match = [(ne_bedroom_n, sound_screen_88),
                         (ne_bedroom_e, sound_screen_88),
                         (ne_bedroom_s, sound_screen_70),
                         (ne_bedroom_w, sound_screen_70),
                         (se_bedroom_n, sound_screen_70),
                         (se_bedroom_e, sound_screen_88),
                         (se_bedroom_s, sound_screen_88),
                         (se_bedroom_w, sound_screen_70),
                         (sw_bedroom_n, sound_screen_70),
                         (sw_bedroom_e, sound_screen_70),
                         (sw_bedroom_s, sound_screen_88),
                         (sw_bedroom_w, sound_screen_70),
                         (nw_bedroom_n, sound_screen_88),
                         (nw_bedroom_e, sound_screen_70),
                         (nw_bedroom_s, sound_screen_70),
                         (nw_bedroom_w, sound_screen_70),
                         (ne_bedroom_ceiling, sound_screen_88),
                         (se_bedroom_ceiling, sound_screen_88),
                         (se_bedroom_ceiling, sound_screen_88),
                         (se_bedroom_ceiling, sound_screen_88),
                         (living_e, sound_screen_88),
                         (living_s, gold_hp_wall_90),
                         (living_w, gold_hp_wall_90),
                         (living_ceiling, gold_hp_ceiling_240),
                         (laundry_partition, sound_screen_88),
                         (laundry_ceiliing, gold_hp_ceiling_240),
                         (showers_partition, sound_screen_88),
                         (showers_ceiliing, gold_hp_ceiling_240),
                         (disabled_wall, gold_hp_wall_90),
                         (disabled_ceiling, gold_hp_ceiling_240)]


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