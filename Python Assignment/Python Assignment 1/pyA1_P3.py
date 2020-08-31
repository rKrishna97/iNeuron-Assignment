from math import pi

def findVolumeOfSphere(diameter):
    radius = diameter / 2
    volume = (4/3)*pi*(radius**3)
    return round(volume, 3)

volumeOfSphere = findVolumeOfSphere(12)

print("The volumne of the sphere with diameter 12cm is {}cm".format(volumeOfSphere))

