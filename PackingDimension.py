import sys
import statistics
import math
from statistics import variance
 load and show an image with Pillow
from PIL import Image
# Open the image form working directory
image = Image.open('kolala.jpeg')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image
load_image.show()

from PIL import Image
from numpy import asarray
# load the image
image = Image.open('kolala.jpeg')
# convert image to numpy array
data = asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
print(data)
def dis2(X, Y)
    dist = math.dist([X], [Y])
    return dist
dis2(random.choice(Sn), random.choice(Sn))
def calculator_dimension(r1, r2, Sn, e, distance):
    Sn = [1, 2, 3, 4, 5]
    for l in range(1, 200):
        perm = permutations(Sn)
        for k in range(1, 2):
            c = set()
            Csize=sys.getsizeof(c)
            for i in range(1, len(Sn)):
                for j in range(1, Csize):
                    if distance < r1 or r2:
                        j = len(Sn) + 1
                    if j < len(Sn) + 1:
                        C = c.union(random.choice(Sn))
                L1 = math.log(Csize)
                L2 = math.log(Csize)
            Dpack = statistics.mean(L2) - statistics.mean(L1) / math.log(r2) - math.log(r1)
            if l > 10 and 1.65 * math.sqrt(variance(L1) + variance(L2)) / math.sqrt(l) * (math.log(r2) - math.log(r1)) < Dpack * (1 - e) / 2:
            return Dpack
calculator_dimension(4, 8, Sn, 6, distance)

