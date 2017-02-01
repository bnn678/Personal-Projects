def Main(a, b):
    return b and Main(b, a % b) or a      # equivalent to if b else a
