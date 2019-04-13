#
# Bisection method for sq. rt.
   
def main():
    input_string = "Enter the number: "
    val = float(input(input_string))

    print("1. Bisection")
    print("2. Newton's Method")
    input_string_choose = "Which algorithm should be used? (enter number): "
    alg = float(input(input_string_choose))
    input_string_tol = "Relative Error Tolerance: "
    tol = float(input(input_string_tol))
    if alg==1:
        if val < 0:
            print("According to my maths its not possible.")
        else:
            low = 0
            high = val
            mid = (low  + high)/2
            relErr = abs((val-mid*mid)/val)
            iter = 1
            while relErr > tol:
                if mid*mid > val:
                    high = mid
                    mid = (low  + high)/2
                else:
                    low = mid
                    mid = (low  + high)/2
                relErr = abs((val-mid*mid)/val)
                iter = iter + 1
            x = mid
    elif alg==2:
        if val < 0:
            print("According to my maths its not possible.")
        else:
            x = val
            relErr = abs((val-x*x)/val)
            iter = 1
            while relErr > tol:
                x = (1/2)*(x+val/x)
                relErr = abs((val-x*x)/val)
                iter = iter + 1

    print("The square root of " + str(val) + " is " + str(x) + " with an accuracy of " + str(relErr*val) + " in " + str(iter) + " iterations.")
  
if __name__ == "__main__":
  main()
