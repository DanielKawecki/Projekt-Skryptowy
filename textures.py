import pygame

# Textury
red_overall = pygame.image.load("textures/red_overall.png")
green_overall = pygame.image.load("textures/green_overall.png")

texture_rt = pygame.image.load("textures/road_turn.png")
texture_sr = pygame.image.load("textures/straight_road.png")
texture_tr = pygame.image.load("textures/three_roads.png")
texture_fr = pygame.image.load("textures/four_roads.png")
texture_src = pygame.image.load("textures/straight_road_castle.png")
texture_trc = pygame.image.load("textures/three_roads_castle.png")

texture_cc = pygame.image.load("textures/castle_center.png")
texture_ccf = pygame.image.load("textures/castle_center_field.png")
texture_ccfb = pygame.image.load("textures/castle_center_field_bonus.png")
texture_ccr = pygame.image.load("textures/castle_center_road.png")
texture_ccrb = pygame.image.load("textures/castle_center_road_bonus.png")

texture_ccor = pygame.image.load("textures/castle_corner.png")
texture_ccb = pygame.image.load("textures/castle_corner_bonus.png")
texture_cascr = pygame.image.load("textures/castle_corner_road.png")
texture_cascrb = pygame.image.load("textures/castle_corner_road_bonus.png")

texture_dbc1 = pygame.image.load("textures/double_castle_separate.png")
texture_dbc2 = pygame.image.load("textures/double_castle_separate2.png")

texture_ltc = pygame.image.load("textures/left_turn_castle.png")
texture_rtc = pygame.image.load("textures/right_turn_castle.png")

texture_m = pygame.image.load("textures/monastery.png")
texture_mr = pygame.image.load("textures/monastery_road.png")

texture_sg = pygame.image.load("textures/single_castle.png")
texture_tc = pygame.image.load("textures/tube_castle.png")
texture_tcb = pygame.image.load("textures/tube_castle_bonus.png")

# Skalowanie
texture_rt = pygame.transform.smoothscale(texture_rt, [100, 100])
texture_sr = pygame.transform.smoothscale(texture_sr, [100, 100])
texture_tr = pygame.transform.smoothscale(texture_tr, [100, 100])
texture_fr = pygame.transform.smoothscale(texture_fr, [100, 100])
texture_src = pygame.transform.smoothscale(texture_src, [100, 100])
texture_trc = pygame.transform.smoothscale(texture_trc, [100, 100])

texture_cc = pygame.transform.smoothscale(texture_cc, [100, 100])
texture_ccf = pygame.transform.smoothscale(texture_ccf, [100, 100])
texture_ccfb = pygame.transform.smoothscale(texture_ccfb, [100, 100])
texture_ccr = pygame.transform.smoothscale(texture_ccr, [100, 100])
texture_ccrb = pygame.transform.smoothscale(texture_ccrb, [100, 100])

texture_ccor = pygame.transform.smoothscale(texture_ccor, [100, 100])
texture_ccb = pygame.transform.smoothscale(texture_ccb, [100, 100])
texture_cascr = pygame.transform.smoothscale(texture_cascr, [100, 100])
texture_cascrb = pygame.transform.smoothscale(texture_cascrb, [100, 100])

texture_dbc1 = pygame.transform.smoothscale(texture_dbc1, [100, 100])
texture_dbc2 = pygame.transform.smoothscale(texture_dbc2, [100, 100])

texture_ltc = pygame.transform.smoothscale(texture_ltc, [100, 100])
texture_rtc = pygame.transform.smoothscale(texture_rtc, [100, 100])

texture_m = pygame.transform.smoothscale(texture_m, [100, 100])
texture_mr = pygame.transform.smoothscale(texture_mr, [100, 100])

texture_sg = pygame.transform.smoothscale(texture_sg, [100, 100])
texture_tc = pygame.transform.smoothscale(texture_tc, [100, 100])
texture_tcb = pygame.transform.smoothscale(texture_tcb, [100, 100])