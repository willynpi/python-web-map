import random
fs = open('example.txt', 'w')
fs.seek(0)
fs.write('LATITUDE,LONGITUDE,ALTITUDE\n')
for t in range(0,50):
    lat = random.uniform(25.088079, 24.961660)
    longt = random.uniform(121.418127, 121.666716)
    alt = random.uniform(100, 1100)
    fs.write('%f,%f,%0.1f \n' %(lat, longt ,alt))
fs.close()
