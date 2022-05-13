# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:


def rgb(r, g, b):
    r = roundToValid(r)
    g = roundToValid(g)
    b = roundToValid(b)
    rgb = (r, g, b)
    return '%02X%02X%02X' % rgb

def roundToValid(val):
    if val < 0: val = 0
    if val > 255: val = 255
    return val


rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
rgb(-20,275,125) # "00FF7D"