import sections, insulation

description = "Earthwool + Bradford 70mm Bedroom Internal"

# A list of tuples matching insulation product to section to insulate.
config = [(sections.ne_bedroom_n, insulation.earth_wall_25),
          (sections.ne_bedroom_e, insulation.earth_wall_25),
          (sections.ne_bedroom_s, insulation.sound_screen_70),
          (sections.ne_bedroom_w, insulation.sound_screen_70),

          (sections.se_bedroom_n, insulation.sound_screen_70),
          (sections.se_bedroom_e, insulation.earth_wall_25),
          (sections.se_bedroom_s, insulation.earth_wall_25),
          (sections.se_bedroom_w, insulation.sound_screen_70),

          (sections.sw_bedroom_n, insulation.sound_screen_70),
          (sections.sw_bedroom_e, insulation.sound_screen_70),
          (sections.sw_bedroom_s, insulation.earth_wall_25),
          (sections.sw_bedroom_w, insulation.sound_screen_70),

          (sections.nw_bedroom_n, insulation.earth_wall_25),
          (sections.nw_bedroom_e, insulation.sound_screen_70),
          (sections.nw_bedroom_s, insulation.sound_screen_70),
          (sections.nw_bedroom_w, insulation.sound_screen_70),

          (sections.nw_bedroom_above_ceiling, insulation.earth_ceiling_50),
          (sections.ne_bedroom_above_ceiling, insulation.earth_ceiling_50),
          (sections.se_bedroom_above_ceiling, insulation.earth_ceiling_50),
          (sections.sw_bedroom_above_ceiling, insulation.earth_ceiling_50),

          (sections.nw_bedroom_ceiling, insulation.earth_ceiling_50),
          (sections.ne_bedroom_ceiling, insulation.earth_ceiling_50),
          (sections.se_bedroom_ceiling, insulation.earth_ceiling_50),
          (sections.sw_bedroom_ceiling, insulation.earth_ceiling_50),

          (sections.living_e, insulation.earth_wall_25),
          (sections.living_s, insulation.earth_ceiling_50),
          (sections.living_w, insulation.earth_ceiling_50),
          (sections.living_ceiling, insulation.earth_ceiling_50),

          (sections.laundry_partition, insulation.earth_wall_25),
          (sections.laundry_ceiliing, insulation.earth_ceiling_50),

          (sections.showers_partition, insulation.earth_wall_25),
          (sections.showers_ceiliing, insulation.earth_ceiling_50),

          (sections.disabled_wall, insulation.earth_ceiling_50),
          (sections.disabled_ceiling, insulation.earth_ceiling_50)]
