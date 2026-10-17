"""
RECORD CHECK  -  my version
===========================

Name  :  Mishal Durrani
Lane  :  AI       
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
with open("lab_records.txt","w") as f:
    f.write("SERVER1,90,100\n")
    f.write("SERVER2,150,100\n")
    f.write("SERVER3,29,100\n")

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check(value,limit):
    """Returns the unused rows (difference) and percentage of rows used (percent) and whether the record is over the limit"""
    difference = limit - value
    percent = (value/limit)*100
    status = "OVER LIMIT" if value >= limit else "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status_of):
    """Prints the record check report"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Rows loaded      : {value:>2.2f}")
    print(f"Rows expected    : {limit:>2.2f}")
    print(f"Rows not loaded  : {difference:>2.2f}")
    print(f"Used             : {percent:>2.2f} %")
    print(f"Status           : {status:>2}")
    print("=" * 34)



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_record(path):
    """Reads label, value, and limit from a file and returns it as a list of dicts"""
    try:
        records = []
        with open(path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({"label": label, "value": float(value), "limit": float(limit)})
        return records
    except FileNotFoundError:
         print("File was not found")
         return []


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.
records = load_record("lab_records.txt")
over_count = 0

def result(records,path):
    """Opens a new file and writes the status of each label in it"""
    with open(path,"w") as f:
        for r in records:
            status = "OVER LIMIT" if r["value"] >= r["limit"] else "OK"
            f.write(f"{r["label"]},{status}\n")

# your loop goes here
for r in records:
    difference, percent, status = check(r["value"],r["limit"])
    print_report(r["label"],r["value"],r["limit"],difference, percent, status)
    if status == "OVER LIMIT":
        over_count += 1
print(f"Over the limit {over_count} time.")
with open("lab_results.txt", "w") as f:
    for r in records:
        difference, percent, status = check(r["value"], r["limit"])
        f.write(f"{r['label']},{status}\n")
with open("lab_results.txt") as f:
    for line in f:
        print(line.strip())


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
