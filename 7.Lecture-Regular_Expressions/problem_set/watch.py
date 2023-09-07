import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    if matches := re.search('"https?://(?:www.)?youtube.com/embed/(\S+?)"',s):
        link = "https://youtu.be/" + matches.group(1)
        return link
    else:
        return None

if __name__ == "__main__":
    main()
