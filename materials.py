# A script to calculate building material requirements for the stables project

import csv

import insulation, config_1, config_2, config_3

configurations = [config_1, config_2, config_3]

products = insulation.products
products_by_code = [(product["code"],product) for product in products]

# Get a dictionary with the key being the product code
# and the value being the total area of that product.
def get_area_by_code(configuration):
    code_to_area = {}

    for product_by_code in products_by_code:
        code_to_area[product_by_code[0]] = 0

    for match in configuration:
        section = match[0]
        material = match[1]
        area = section["area"]
        code = material["code"]
        code_to_area[code] += area

    return code_to_area

def write_area_by_product():
    with open("product_area.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Code", "Product Description", "Area to Cover"])

        for config in configurations:
            writer.writerow(["", config.description])
            for product in products:
                code = product["code"]
                name = product["name"]
                area = get_area_by_code(config.config)[code]
                if area > 0:
                    writer.writerow([code, name, area])
            writer.writerow([""])

write_area_by_product()