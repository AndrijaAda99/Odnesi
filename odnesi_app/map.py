from matplotlib import pyplot as plt
from io import BytesIO
from PIL import Image
import requests
import pandas as pd
import math

URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"

TILE_SIZE = 256

df = pd.read_csv('data.csv')

def point_to_pixels(lat, lon, zoom):
    """convert gps coordinates to web mercator"""
    r = math.pow(2, zoom) * TILE_SIZE
    lat = math.radians(lat)

    x = int((lon + 180.0) / 360.0 * r)
    y = int((1.0 - math.log(math.tan(lat) + (1.0 / math.cos(lat))) / math.pi) / 2.0 * r)

    return x, y

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

top, bot = df.lat.max(), df.lat.min()
lef, rgt = df.lon.min(), df.lon.max()

zoom = 12
x0, y0 = point_to_pixels(lef, top, zoom)
x1, y1 = point_to_pixels(rgt, bot, zoom)

lat = cal_average(df['lat'])
lon = cal_average(df['lon'])

print(lat)
print(lon)

x, y = point_to_pixels(lat, lon, zoom)

x_tiles, y_tiles = int(x / TILE_SIZE), int(y / TILE_SIZE)

# format the url
url = URL.format(x=x_tiles, y=y_tiles, z=zoom)

# make the request
with requests.get(url) as resp:
    img = Image.open(BytesIO(resp.content))

x = df['lat']
y = df['lon']

fig, ax = plt.subplots()

ax.imshow(img, extent=(lef, rgt, bot, top))
ax.scatter(x,y)
ax.set_ylim(bot, top)
ax.set_xlim(lef, rgt)



fig.show()



