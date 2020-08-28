# A script to calculate building material requirements for the stables project

import csv, math

import insulation, config_1, config_2, config_3, config_4
import insulwest, perth_building_materials

prices = [insulwest.prices, perth_building_materials.prices]
vendor_names = [insulwest.company, perth_building_materials.company]

configurations = [config_1, config_2, config_3, config_4]

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

# Get a list of companies and their price for a given product.
def get_prices_per_product(product_code):
    prices_per_product = []
    for product in products:
        if product["code"] == product_code:
            for vendor_prices in prices:
                for vendor_price in vendor_prices:
                    if vendor_price["product"]["code"] == product_code:
                        prices_per_product.append({ "company" : "Name",
                                                    "price" : vendor_price["price"]})
    return prices_per_product

# Create a CSV file with each product and the area
# it is to cover for each configuration.
def write_quantities():
    with open("quantities.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Code",
                         "Product Description",
                         "Area",
                         "Packs"] + vendor_names)

        for config in configurations:
            writer.writerow(["", config.description])
            for product in products:
                code = product["code"]
                name = product["name"]
                area = get_area_by_code(config.config)[code]
                packs_required = math.ceil(area / product["pack-coverage"])
                prices_per_product = get_prices_per_product(code)
                costs = []
                for price in prices_per_product:
                    if price["price"] > 0:
                        cost = round(price["price"] * packs_required, 2)
                    else:
                        cost = "Price not given"
                    costs.append(cost)
                if area > 0:
                    writer.writerow([code, name, area, packs_required] + costs)
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