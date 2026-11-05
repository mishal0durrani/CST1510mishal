"""
RECORD CHECK  -  my version
===========================

Name  :  Mishal Durrani
Lane  :  AI
Date  :  5/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("D:\\CST1510\\CST1510mishal\\Week 06 - Pandas\\LAB\\lab_data.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
df["percent"] = ((df["rows_loaded"] / df["rows_expected"])*100).round(2)
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x>= 100 else "WARNING" if x >= 90 else "OK")

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
print("======NORMAL DATAFRAME======")
print(df)
print("======FILTERED DATAFRAME======")#filtered only for only ok status
print(df[df["status"] == "OK"])
print("======GROUPED DATAFRAME======")#grouped by status and printing
grouped = df.groupby("status")
print(grouped.size())
df.to_csv("new_lab_data.csv",index=False)#saving to new csv
#making bar chart
grouped.size().plot(kind="bar")
plt.savefig("lab_status_counts.png")
plt.show()

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
