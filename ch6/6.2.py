#!/usr/bin/python3
import sys
start=int(sys.argv[1])
end=int(sys.argv[2])
for line in sys.stdin:
    value=int(line)
    if start<=value<=end:
        print(value)
# ./ch6/6.1.py 60 | ./ch6/6.2.py 20 60