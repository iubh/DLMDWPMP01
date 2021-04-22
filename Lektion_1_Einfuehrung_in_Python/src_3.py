# IU - Internationale Hochschule
# Programmierung mit Python
# Course Code: DLMDWPMP01

# in diesem Skript sehen wir, wie wir, je nach
# Art der Ausführung, das verhalten eines
# Skriptes in der jeweiligen Umgebung
# steuern können

def main():
    """ This part of the script will only by executed
    if the script is called directly (not by import in
    another script)
    """

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

# is this script called directly...
if __name__ == "__main__":
    
    # ...then execute the code above
    main()
