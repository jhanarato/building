# A script to calculate building material requirements for the stables project

# Insulation products
sound_shield_70 = {"name" : "Bradford SoundShield Wall Batts 70mm",
               "thickness" : 70,
               "length" : 1160,
               "width" : 580,
               "r-value" : 2,
               "pack-pieces" : 9,
               "pack-meters-sqr" : 6.1,
               "pack-coverage" : 6.8,
               "product-code" : 182313 }

sound_shield_88 = {"name" : "Bradford SoundShield Wall Batts 88mm",
               "thickness" : 88,
               "length" : 1160,
               "width" : 580,
               "r-value" : 2.5,
               "pack-pieces" : 7,
               "pack-meters-sqr" : 4.7,
               "pack-coverage" : 5.3,
               "product-code" : 182286 }

gold_hp_240 = {"name" : "Bradford Gold High-Performance Ceiling Batts 240mm",
               "thickness" : 240,
               "length" : 1160,
               "width" : 580,
               "r-value" : 5,
               "pack-pieces" : 8,
               "pack-meters-sqr" : 5.4,
               "pack-coverage" : 6.1,
               "product-code" : 105419 }

# Sections to insulate
ne_bedroom_n = {"name" : "Northeast Bedroom, North Wall",
                "area" : 5.8 }
ne_bedroom_e = {"name" : "Northeast Bedroom, East Wall",
                "area" : 7.9}
ne_bedroom_s = {"name" : "Northeast Bedroom, South Wall",
                "area" : 7.8}
ne_bedroom_w = {"name" : "Northeast Bedroom, West Wall",
                "area" : 11.0}

se_bedroom_n = {"name" : "Southeast Bedroom, North Wall",
                "area" : 7.8 }
se_bedroom_e = {"name" : "Southeast Bedroom, East Wall",
                "area" : 7.9}
se_bedroom_s = {"name" : "Southeast Bedroom, South Wall",
                "area" : 5.8}
se_bedroom_w = {"name" : "Southeast Bedroom, West Wall",
                "area" : 11.0}

sw_bedroom_n = {"name" : "Southwest Bedroom, North Wall",
                "area" : 7.8 }
sw_bedroom_e = {"name" : "Southwest Bedroom, East Wall",
                "area" : 11.0}
sw_bedroom_s = {"name" : "Southwest Bedroom, South Wall",
                "area" : 4.1}
sw_bedroom_w = {"name" : "Southwest Bedroom, West Wall",
                "area" : 11.0}

nw_bedroom_n = {"name" : "Northwest Bedroom, North Wall",
                "area" :  2.8}
nw_bedroom_e = {"name" : "Northwest Bedroom, East Wall",
                "area" : 11.0}
nw_bedroom_s = {"name" : "Northwest Bedroom, South Wall",
                "area" : 4.1}
nw_bedroom_w = {"name" : "Northwest Bedroom, West Wall",
                "area" : 8.2}

