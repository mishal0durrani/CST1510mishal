"""
RECORD CHECK  -  my version
===========================

Name  : Mishal Durrani
Lane  :  AI      (delete two)
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def get_input():
    """Gets the input (dataset name, value, and limit)"""
    label = input("Enter your dataset name or 'quit' to stop: ")
    if label == "quit":
        return None      
    value = float(input("Enter the number of rows loaded: "))     
    limit = float(input("Enter the number of rows expected: "))    
    return label, value, limit

def status_of(percent):
    """Calculates the status using the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value,limit):
    """Returns the unused rows (difference) and percentage of rows used (percent)"""
    difference = limit - value
    percent = (value/limit)*100
    return difference, percent

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.
      


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

def print_report(label, value, limit, difference, percent, status_of):
    """Prints the report"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Rows loaded      : {value:>2.2f}")
    print(f"Rows expected    : {limit:>2.2f}")
    print(f"Rows not loaded  : {difference:>2.2f}")
    print(f"Used             : {percent:>2.2f} %")
    print(f"Status           : {status_of(percent):>2}")
    print("=" * 34)

over_limit = 0

while True:
    record = get_input()
    if record is None:
        break
    label, value, limit = record
    difference, percent = check(value,limit)   
    status = status_of(percent)  
    if status == "OVER LIMIT":
        over_limit += 1
    print_report(label, value, limit, difference, percent, status_of)

print(f"It went over the limit {over_limit} times.")
        



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
