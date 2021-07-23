import time
import emoji
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print(emoji.emojize('\033[33m :boom:', use_aliases=True))
