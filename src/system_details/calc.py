def byteToGB(bytes: int):
    gb = 1073741824
    gigs = round(bytes/gb, 2)
    return gigs