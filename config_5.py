import sections, insulation

description = "Bradford 70mm + Glasswool 90 + Earthwool 240"

# A list of tuples matching insulation product to section to insulate.
config = [(sections.ne_bedroom_n, insulation.pink_wall_90),
          (sections.ne_bedroom_e, insulation.pink_wall_90),
          (sections.ne_bedroom_s, insulation.sound_screen_70),
          (sections.ne_bedroom_w, insulation.sound_screen_70),

          (sections.se_bedroom_n, insulation.sound_screen_70),
          (sections.se_bedroom_e, insulation.pink_wall_90),
          (sections.se_bedroom_s, insulation.pink_wall_90),
          (sections.se_bedroom_w, insulation.sound_screen_70),

          (sections.sw_bedroom_n, insulation.sound_screen_70),
          (sections.sw_bedroom_e, insulation.sound_screen_70),
          (sections.sw_bedroom_s, insulation.pink_wall_90),
          (sections.sw_bedroom_w, insulation.sound_screen_70),

          (sections.nw_bedroom_n, insulation.pink_wall_90),
          (sections.nw_bedroom_e, insulation.sound_screen_70),
          (sections.nw_bedroom_s, insulation.sound_screen_70),
          (sections.nw_bedroom_w, insulation.sound_screen_70),

          (sections.nw_bedroom_above_ceiling, insulation.pink_wall_90),
          (sections.ne_bedroom_above_ceiling, insulation.pink_wall_90),
          (sections.se_bedroom_above_ceiling, insulation.pink_wall_90),
          (sections.sw_bedroom_above_ceiling, insulation.pink_wall_90),

          (sections.nw_bedroom_ceiling, insulation.pink_wall_90),
          (sections.ne_bedroom_ceiling, insulation.pink_wall_90),
          (sections.se_bedroom_ceiling, insulation.pink_wall_90),
          (sections.sw_bedroom_ceiling, insulation.pink_wall_90),

          (sections.living_e, insulation.pink_wall_90),
          (sections.living_s, insulation.pink_wall_90),
          (sections.living_w, insulation.pink_wall_90),
          (sections.living_ceiling, insulation.earth_ceiling_50),

          (sections.laundry_partition, insulation.pink_wall_90),
          (sections.laundry_ceiliing, insulation.earth_ceiling_50),

          (sections.showers_partition, insulation.pink_wall_90),
          (sections.showers_ceiliing, insulation.earth_ceiling_50),

          (sections.disabled_wall, insulation.pink_wall_90),
          (sections.disabled_ceiling, insulation.earth_ceiling_50)]
