import sys
def calculate_Simple_interest(principal,rate,time):
    """Calculate Simple interest given principal,rate,time."""
    return(principal*rate*time)/100

if __name__  == "__main__":
    print("=== Simple Interest Calculator ===")
    try:
        if len(sys.argv) == 4:
            p = float(sys.argv[1])
            r = float(sys.argv[2])
            t = float(sys.argv[3])
            
        else:
            p = float(input("Enter the principal amount: "))
            r = float(input("Enter the rate of interest: "))
            t = float(input("Enter the time in years: "))
            
        print("\n====Program Parameters====")
        print("Principal Amount :",p)
        print("Rate of interest :",r) 
        print("Time in years :",t) 
         
        interest = calculate_Simple_interest(p,r,t)
        print(f"\nSimple interest={interest:.2f}")
         
    except ValueError:   
        print("Invalid input! Please enter numeric values.")  

                