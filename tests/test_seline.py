import pymorph
import numpy as np

def test_seline_len():
    for angle in (0, 45, -45, 90, -90, 180):
        for w in range(1,7):
            assert pymorph.seline(w, angle).sum() == w
