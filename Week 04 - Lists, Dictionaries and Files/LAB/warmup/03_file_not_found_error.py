# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt","w") as f:
    f.write("lala, 90, 100")
with open("records.txt") as f:
    print(f.read())
