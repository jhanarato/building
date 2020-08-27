# A script to calculate building material requirements for the stables project

import csv

import insulation, config_1

products = insulation.products
products_by_code = [(product["code"],product) for product in products]

# Get a dictionary with the key being the product code
# and the value being the total area of that product.
def get_area_by_code():
    code_to_area = {}

    for product_by_code in products_by_code:
        code_to_area[product_by_code[0]] = 0

    for match in config_1.config:
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
        writer.writerow([config_1.description])
        writer.writerow(["Product Code", "Product Description", "Area to Cover"])
        for product in products:
            code = product["code"]
            name = product["name"]
            area = get_area_by_code()[code]
            if area > 0:
                writer.writerow([code, name, area])

write_area_by_product()