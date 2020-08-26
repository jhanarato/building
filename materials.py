# A script to calculate building material requirements for the stables project

import csv

import insulation

products = insulation.products
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

ne_bedroom_ceiling = {"name" : "Northeast Bedroom, Ceiling Below MLV",  "area" : 14.0 }
se_bedroom_ceiling = {"name" : "Southeast Bedroom, Ceiling Below MLV",  "area" : 14.0 }
sw_bedroom_ceiling = {"name" : "Southwest Bedroom, Ceiling Below MLV",  "area" : 14.0 }
nw_bedroom_ceiling = {"name" : "Northwest Bedroom, Ceiling Below MLV",  "area" : 14.0 }

ne_bedroom_above_ceiling = {"name" : "Northeast Bedroom, Ceiling Above MLV",  "area" : 14.0 }
se_bedroom_above_ceiling = {"name" : "Southeast Bedroom, Ceiling Above MLV",  "area" : 14.0 }
sw_bedroom_above_ceiling = {"name" : "Southwest Bedroom, Ceiling Above MLV",  "area" : 14.0 }
nw_bedroom_above_ceiling = {"name" : "Northwest Bedroom, Ceiling Above MLV",  "area" : 14.0 }

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
product_section_match = [(ne_bedroom_n, insulation.sound_screen_88),
                         (ne_bedroom_e, insulation.sound_screen_88),
                         (ne_bedroom_s, insulation.sound_screen_70),
                         (ne_bedroom_w, insulation.sound_screen_70),

                         (se_bedroom_n, insulation.sound_screen_70),
                         (se_bedroom_e, insulation.sound_screen_88),
                         (se_bedroom_s, insulation.sound_screen_88),
                         (se_bedroom_w, insulation.sound_screen_70),

                         (sw_bedroom_n, insulation.sound_screen_70),
                         (sw_bedroom_e, insulation.sound_screen_70),
                         (sw_bedroom_s, insulation.sound_screen_88),
                         (sw_bedroom_w, insulation.sound_screen_70),

                         (nw_bedroom_n, insulation.sound_screen_88),
                         (nw_bedroom_e, insulation.sound_screen_70),
                         (nw_bedroom_s, insulation.sound_screen_70),
                         (nw_bedroom_w, insulation.sound_screen_70),

                         (nw_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (ne_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (se_bedroom_above_ceiling, insulation.gold_hp_wall_90),
                         (sw_bedroom_above_ceiling, insulation.gold_hp_wall_90),

                         (nw_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (ne_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (se_bedroom_ceiling, insulation.gold_hp_wall_90),
                         (sw_bedroom_ceiling, insulation.gold_hp_wall_90),

                         (living_e, insulation.sound_screen_88),
                         (living_s, insulation.gold_hp_wall_90),
                         (living_w, insulation.gold_hp_wall_90),
                         (living_ceiling, insulation.gold_hp_ceiling_240),

                         (laundry_partition, insulation.sound_screen_88),
                         (laundry_ceiliing, insulation.gold_hp_ceiling_240),

                         (showers_partition, insulation.sound_screen_88),
                         (showers_ceiliing, insulation.gold_hp_ceiling_240),

                         (disabled_wall, insulation.gold_hp_wall_90),
                         (disabled_ceiling, insulation.gold_hp_ceiling_240)]


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