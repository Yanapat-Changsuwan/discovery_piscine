import sys
import re
if len(sys.argv) < 3:
    print("none")
else:
    keyword = sys.argv[1]
    txt = sys.argv[2]
    count = 0
    ans = re.findall(keyword, txt)
    if ans:
        count = len(ans)
        print(count)