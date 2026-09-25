"""
RECORD CHECK  -  my version
===========================

Name  : Mishal Durrani
Lane  :  AI       (delete two)
Date  : 25/9/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

dataset_name = input("Enter the name of the dataset: ")      # : replace with an input() call
rows_used = float(input("Enter the number of rows used: "))     # : replace with an input() call, converted
total_rows = float(input("Enter the total number of rows: "))   # : replace with an input() call, converted

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = total_rows - rows_used  # 
used_percent = (rows_used/total_rows)*100      # 
free_percent = (difference/total_rows)*100      # 

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)

print(f"Rows used            : {rows_used:>10.2f}")
print(f"Total rows           : {total_rows:>10.2f}")
print(f"Free                 : {difference:>+10.2f}")
print(f"Percent of used rows : {used_percent:>10.2f}%")
print(f"Percent of free rows : {free_percent:>10.2f}%")

#Like how % of used rows gives a better idea on how much of the dataset is used,
# % of free rows helps understand how much of the dataset is still available for use.

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
