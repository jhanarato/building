import plasterboard, perth_building_materials, p_config_1
import csv, math

prices = [perth_building_materials.prices]
configurations = [p_config_1]
vendor_names = [perth_building_materials.company]
products = plasterboard.products
products_by_code = [(product["code"],product) for product in products]

# Get the area of coverage needed per product
def get_area_by_code(configuration):
    code_to_area = {}

    for product_by_code in products_by_code:
        code_to_area[product_by_code[0]] = 0

    for match in configuration:
        section = match[0]
        product = match[1]
        code = product["code"]
        area = section["area"]
        code_to_area[code] += area

    return code_to_area

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

def write_plasterboard():
    with open("plasterboard.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product", "Area to Cover", "Sheets Needed"] + vendor_names)
        for config in configurations:
            writer.writerow(["", config.description])
            for product in products:
                code = product["code"]
                name = product["name"]
                area_to_cover = get_area_by_code(config.config)[code]
                sheets = math.ceil(area_to_cover / (product["length"] * product["width"]))
                writer.writerow([name, area_to_cover, sheets])

write_plasterboard()