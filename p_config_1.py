import sections, plasterboard

description = "Fire & Standard 13mm x 2400 x 1200"

# A list of tuples matching insulation product to section to insulate.
config = [(sections.ne_bedroom_n, plasterboard.gtek_fire_2400_by_1200),
          (sections.ne_bedroom_e, plasterboard.gtek_fire_2400_by_1200),
          (sections.ne_bedroom_s, plasterboard.gtek_fire_2400_by_1200),
          (sections.ne_bedroom_w, plasterboard.gtek_fire_2400_by_1200),

          (sections.se_bedroom_n, plasterboard.gtek_fire_2400_by_1200),
          (sections.se_bedroom_e, plasterboard.gtek_fire_2400_by_1200),
          (sections.se_bedroom_s, plasterboard.gtek_fire_2400_by_1200),
          (sections.se_bedroom_w, plasterboard.gtek_fire_2400_by_1200),

          (sections.sw_bedroom_n, plasterboard.gtek_fire_2400_by_1200),
          (sections.sw_bedroom_e, plasterboard.gtek_fire_2400_by_1200),
          (sections.sw_bedroom_s, plasterboard.gtek_fire_2400_by_1200),
          (sections.sw_bedroom_w, plasterboard.gtek_fire_2400_by_1200),

          (sections.nw_bedroom_n, plasterboard.gtek_fire_2400_by_1200),
          (sections.nw_bedroom_e, plasterboard.gtek_fire_2400_by_1200),
          (sections.nw_bedroom_s, plasterboard.gtek_fire_2400_by_1200),
          (sections.nw_bedroom_w, plasterboard.gtek_fire_2400_by_1200),

          (sections.plasterboard_layer_two, plasterboard.gtek_fire_2400_by_1200),

          (sections.nw_bedroom_ceiling, plasterboard.gtek_fire_2400_by_1200),
          (sections.ne_bedroom_ceiling, plasterboard.gtek_fire_2400_by_1200),
          (sections.se_bedroom_ceiling, plasterboard.gtek_fire_2400_by_1200),
          (sections.sw_bedroom_ceiling, plasterboard.gtek_fire_2400_by_1200),

          (sections.living_e, plasterboard.gtek_fire_2400_by_1200),
          (sections.living_s, plasterboard.gtek_standard_2400_by_1200),
          (sections.living_w, plasterboard.gtek_standard_2400_by_1200),
          (sections.living_ceiling, plasterboard.gtek_standard_2400_by_1200),

          #(sections.laundry_partition, plasterboard.gtek_fire_2400_by_1200),
          (sections.laundry_ceiliing, plasterboard.gtek_standard_2400_by_1200),

          #(sections.showers_partition, plasterboard.gtek_fire_2400_by_1200),
          (sections.showers_ceiliing, plasterboard.gtek_standard_2400_by_1200),

          (sections.disabled_wall, plasterboard.gtek_fire_2400_by_1200),
          (sections.disabled_ceiling, plasterboard.gtek_standard_2400_by_1200)]
