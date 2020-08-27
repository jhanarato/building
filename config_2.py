import sections, insulation

description = "Bradford with Pink Batts"

# A list of tuples matching insulation product to section to insulate.
config = [(sections.ne_bedroom_n, insulation.sound_screen_88),
          (sections.ne_bedroom_e, insulation.sound_screen_88),
          (sections.ne_bedroom_s, insulation.sound_screen_70),
          (sections.ne_bedroom_w, insulation.sound_screen_70),

          (sections.se_bedroom_n, insulation.sound_screen_70),
          (sections.se_bedroom_e, insulation.sound_screen_88),
          (sections.se_bedroom_s, insulation.sound_screen_88),
          (sections.se_bedroom_w, insulation.sound_screen_70),

          (sections.sw_bedroom_n, insulation.sound_screen_70),
          (sections.sw_bedroom_e, insulation.sound_screen_70),
          (sections.sw_bedroom_s, insulation.sound_screen_88),
          (sections.sw_bedroom_w, insulation.sound_screen_70),

          (sections.nw_bedroom_n, insulation.sound_screen_88),
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

          (sections.living_e, insulation.sound_screen_88),
          (sections.living_s, insulation.pink_wall_90),
          (sections.living_w, insulation.pink_wall_90),
          (sections.living_ceiling, insulation.gold_hp_ceiling_240),

          (sections.laundry_partition, insulation.sound_screen_88),
          (sections.laundry_ceiliing, insulation.gold_hp_ceiling_240),

          (sections.showers_partition, insulation.sound_screen_88),
          (sections.showers_ceiliing, insulation.gold_hp_ceiling_240),

          (sections.disabled_wall, insulation.pink_wall_90),
          (sections.disabled_ceiling, insulation.gold_hp_ceiling_240)]
