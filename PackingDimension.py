import sys
import statistics
import math
from statistics import variance
from PIL import Image
im = Image.open("lena.ppm")
from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
           from __future__ import print_function
import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
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

