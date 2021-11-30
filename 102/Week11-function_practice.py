# Carter Strate
# CSCI 102 - Section D
# Week 11 Lab
# References: None
# Time: 20 minutes
import math
def print_output(user_input):
    print(f'OUTPUT {user_input}')
def triangle_hypotenuse(side1,side2):
    hypo = (((float(side1))**2)+((float(side2))**2))**0.5
    hypo = '{:.2f}'.format(round(hypo,2))
    print_output(hypo)
def feet_to_meters(num_feet):
    num_meters = float(num_feet) * 0.3048
    num_meters = '{:.4f}'.format(round(num_meters,4))
    print_output(num_meters)
def polar_coords(x,y):
    r = (((float(x))**2)+((float(y))**2))**0.5
    r = '{:.2f}'.format(round(r,2))
    sr = f'r: {r}'
    theta = math.atan((float(y)/float(x)))
    theta = theta * 57.2958
    theta = '{:.2f}'.format(round(theta,2))
    stheta = f'theta: {theta}'
    print_output(sr)
    print_output(stheta)
def dollars_to_euros(dollars):
    euros = float(dollars) * 0.86
    euros = '{:.2f}'.format(euros)
    print_output(euros)
triangle_hypotenuse(3,4)
polar_coords(12,5)
