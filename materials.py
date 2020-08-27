# A script to calculate building material requirements for the stables project

import csv, math

import insulation, config_1, config_2, config_3
import insulwest

prices = insulwest.prices

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

def get_price(code):
    for price in prices:
        if price["product"]["code"] == code:
            return price["price"]

# Create a CSV file with each product and the area
# it is to cover for each configuration.
def write_quantities():
    with open("quantities.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Code",
                         "Product Description",
                         "Area to Cover",
                         "Packs Required",
                         "Cost"])

        for config in configurations:
            writer.writerow(["", config.description])
            for product in products:
                code = product["code"]
                name = product["name"]
                area = get_area_by_code(config.config)[code]
                packs_required = math.ceil(area / product["pack-coverage"])
                price = get_price(code)
                if price > 0:
                    cost = round(price * packs_required, 2)
                else:
                    cost = "Price not given"
                if area > 0:
                    writer.writerow([code, name, area, packs_required, cost])
            writer.writerow([""])

# Create a CSV file with each configuration showing what material is used in each section.
def write_config():
    with open("configs.csv", "w") as csvfile:
        for config in configurations:
            writer = csv.writer(csvfile)
            writer.writerow([config.description])
            for section_and_product in config.config:
                writer.writerow([section_and_product[0]["name"], section_and_product[1]["name"]])
            writer.writerow([""])

write_quantities()
write_config()