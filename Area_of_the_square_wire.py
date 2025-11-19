#Area_of_the_square_wire

angle_in_deg= 60
r_of_arc = 42
angle_in_rad = angle_in_deg*(3.14159/180)

#as we know that angle = arc/radius
#so we have to find arc length 
#for that formula will be arc = radius*angle_in_rad
arc_len = 42*angle_in_rad
side_of_sq = arc_len/4
area_of_sq = side_of_sq**2
print("Area of the square wire = ",area_of_sq)