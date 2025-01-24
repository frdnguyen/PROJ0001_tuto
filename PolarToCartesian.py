# Importing external libraries or functions
import numpy

# Function definition
def PolarToCartesian(rho,theta):
    """
    Parameters
    ----------
    rho : radius
        
    theta : angle in degrees
        

    Returns
    -------
    Cartesian coordinates of a point defined from its polar coordinates.

    """
    
    theta = theta * numpy.pi/180
    x = rho * numpy.cos(theta)
    y = rho * numpy.sin(theta)
    return x,y