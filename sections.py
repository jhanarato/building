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

# For insulation only
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

# For plasterboard only
bedroom_walls = [ne_bedroom_n, nw_bedroom_e, nw_bedroom_s, nw_bedroom_w,
                 se_bedroom_n, se_bedroom_e, se_bedroom_s, se_bedroom_w,
                 sw_bedroom_n, sw_bedroom_e, sw_bedroom_s, sw_bedroom_w,
                 sw_bedroom_n, sw_bedroom_e, sw_bedroom_s, sw_bedroom_w]

area = 0
for wall in bedroom_walls:
    area += wall["area"]

plasterboard_layer_two = { "name" : "Second layer of plasterboard", "area" : area * 2}

print("Area %f", plasterboard_layer_two["area"])