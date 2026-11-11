"""
RECORD CHECK  -  my version
===========================

Name  :  Mishal Durrani
Lane  :  AI
Date  :  11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    surveyPart, rest = line.split(",", 1)
    surveyName = surveyPart.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
    return {"survey": surveyName, "rating": fields["rating"], "age": fields["age"]}

def status_of(rating, good_at=90):
    """Returns GREAT, OK, OR POOR for a rating"""
    if rating >= good_at:
        return "GREAT"
    elif rating >= 50:
        return "OK"
    else:
        return "BAD"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
total_count = 0
bad_count = 0
with open("D:\\CST1510\\CST1510mishal\\Week 07 - Strings and Text Manipulation\\LAB\\lab_messy_lines.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        status = status_of(record["rating"])
        total_count += 1
        if status == "BAD":
            bad_count += 1
        print(f"Survey:{record['survey']}||Age:{record['age']}||Rating: {record['rating']}||Status: {status_of(record['rating'])}")
 
print(f"Total records: {total_count}, Low rated (BAD): {bad_count}")           
        



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
