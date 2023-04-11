import random
import pieces
from textures import *

list_of_elements = []

for i in range(9):
    list_of_elements.append(pieces.piece_template(3, 3, 2, 2, False, False, texture_rt))

for i in range(8):
    list_of_elements.append(pieces.piece_template(2, 3, 2, 3, False, False, texture_sr))

for i in range(4):
    list_of_elements.append(pieces.piece_template(2, 2, 2, 3, True, False, texture_tr))

list_of_elements.append(pieces.piece_template(2, 2, 2, 2, True, False, texture_fr))

for i in range(4):
    list_of_elements.append(pieces.piece_template(1, 2, 3, 2, True, False, texture_src))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 2, 2, 2, True, False, texture_trc))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 3, 2, 2, False, False, texture_ltc))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 2, 2, 3, False, False, texture_rtc))

for i in range(5):
    list_of_elements.append(pieces.piece_template(1, 3, 3, 3, False, False, texture_sg))

for i in range(2):
    list_of_elements.append(pieces.piece_template(1, 3, 3, 1, False, True, texture_dbc1))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 3, 1, 3, False, True, texture_dbc2))

for i in range(1):
    list_of_elements.append(pieces.piece_template(3, 1, 3, 1, False, False, texture_tc))

for i in range(2):
    list_of_elements.append(pieces.piece_template(3, 1, 3, 1, False, False, texture_tcb, True))

for i in range(2):
    list_of_elements.append(pieces.piece_template(1, 1, 2, 1, True, False, texture_ccrb, True))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 3, 3, 1, False, False, texture_ccor))

for i in range(2):
    list_of_elements.append(pieces.piece_template(1, 3, 3, 1, False, False, texture_ccb, True))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 2, 2, 1, False, False, texture_cascr))

for i in range(2):
    list_of_elements.append(pieces.piece_template(1, 2, 2, 1, False, False, texture_cascrb))

for i in range(1):
    list_of_elements.append(pieces.piece_template(1, 1, 2, 1, True, False, texture_ccr))

for i in range(1):
    list_of_elements.append(pieces.piece_template(1, 1, 3, 1, True, False, texture_ccfb, True))

for i in range(3):
    list_of_elements.append(pieces.piece_template(1, 1, 3, 1, True, False, texture_ccf))

for i in range(1):
    list_of_elements.append(pieces.piece_template(1, 1, 1, 1, True, False, texture_cc, True))

for i in range(4):
    list_of_elements.append(pieces.piece_template(3, 3, 3, 3, False, False, texture_m, False, True))

for i in range(2):
    list_of_elements.append(pieces.piece_template(3, 3, 2, 3, True, False, texture_mr, False, True))

# Wylosowanie pozyzji startowej

random.shuffle(list_of_elements)
