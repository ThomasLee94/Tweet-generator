# Isolating all of stans texts. 
file = open('stan-transcript-s1-s8.txt', 'w')

with open('southpark-transcript-s1-s8.txt', 'r') as original:
    for line in original:
        if line.strip('\n') in ("Stan"):
            file.write((next(original)))

file.close()
