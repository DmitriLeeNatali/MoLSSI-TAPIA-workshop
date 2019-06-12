import os
import numpy
import sis
file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
coordinates = coordinates.astype(numpy.float)
print(symbols)
print(coordinates)
num_atoms = len(symbols)
for num2 in range(0,num_atoms):
        if num1>num2:
            distance_12 = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_check(distance_12,minimum=0,maximum=1.6) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')
def calculate_distance(coords1,coords2):
    """
    this function has two arguments (2 cartesian vectors in R3) and returns the magnitude of distance between them
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12
    def bond_check(distance,minimum=0,maximum=1.5):
    delta_x = coords1[0] - coords2[0]
    delta_y = coords1[1] - coords2[1]
    delta_z = coords1[2] - coords2[2]
    distance_12 = numpy.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
    if distance_12>minimum and distance<maximum:
        return(True)
    else:
        return(False)
