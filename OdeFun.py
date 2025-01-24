def odefunction(t, y, const):
    # Ordinary differential equation system defined by:
    #   t: the time
    #   y: system variables
    # The function returns dy, an array containing the derivatives
    
    # Necessary import
    import numpy as np
    
    # Main part
    # Constant definitions
    epsilon = const[0]
    omega = const[1]

    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = epsilon * omega * (1 - y[0]**2) * y[1] - (omega**2) * y[0]
    
    return dy