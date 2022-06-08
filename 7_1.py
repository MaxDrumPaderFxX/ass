def main(input):
    a = (input & 0x00000000000000000000001111111111)
    b = (input & 0x00000000000001111111110000000000) << 13
    c = (input & 0x00011111111110000000000000000000) >> 6
    d = (input & 0x11100000000000000000000000000000) >> 19

    return (a | b | c | d)

print(main(0x02dcb40b))