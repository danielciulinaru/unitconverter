FACTOR: float = 1024
B = "b"
K = "k"
KB = "kb"
M = "m"
MB = "mb"
G = "g"
GB = "gb"
T = "t"
TB = "tb"
P = "p"
PB = "pb"
UNITS_B = [B]
UNITS_KB = [K, KB]
UNITS_MB = [M, MB]
UNITS_GB = [G, GB]
UNITS_TB = [T, TB]
UNITS_PB = [P, PB]
UNITS_LIST = UNITS_B + UNITS_KB + UNITS_MB + UNITS_GB + UNITS_TB + UNITS_PB
STANDARD_UNIT_B = B.upper()
STANDARD_UNIT_KB = K.upper()
STANDARD_UNIT_MB = M.upper()
STANDARD_UNIT_GB = G.upper()
STANDARD_UNIT_TB = T.upper()
STANDARD_UNIT_PB = P.upper()


class Byte(object):
    def __repr__(self):
        return B


class KiloByte(object):
    def __repr__(self):
        return KB
