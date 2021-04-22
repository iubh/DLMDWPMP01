# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# diese Funktion ist zur Verwendung in einem anderen \
# Python-Skript gedacht
def what_a_function(x, y):
    """
    This function sums up its two inputs and
    returns the quadratic of this sum

    input arguments:
    - x: numeric
    - y: numeric 

    dependencies:
    - none

    output arguments:
    The quadratic of the sum of inputs
    """
    
    # add the two input arguments
    z = x + y

    # square this sum
    out = z**2

    # return the results from the function
    return(out)