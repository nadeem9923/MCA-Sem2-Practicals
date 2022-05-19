import re

if __name__ == '__main__':
    string = "abc123"
    pattern = re.compile("[A-Za-z0-9]+")

    # if found match (entire string matches pattern)
    if pattern.fullmatch(string) is not None:
        print("Found match: " + string)
    else:
        # if not found match
        print("No match")