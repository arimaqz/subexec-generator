from string import ascii_lowercase
import random
import sys

target = sys.argv[1]
target_len = len(target)

needed_chars = ""

for c in ascii_lowercase:
    if c in target and c not in needed_chars:
        needed_chars += c

for i in range(0,3):
    needed_chars += ascii_lowercase[random.randint(0, len(ascii_lowercase)-1)]

if " " in target:
    needed_chars += " "
if "/" in target:
    needed_chars += "/"
if "-" in target:
    needed_chars += "-"

needed_chars = list(needed_chars)
random.shuffle(needed_chars)
needed_chars = "".join(needed_chars)
needed_index = ""
for c in target:
    needed_index += str(needed_chars.index(c)) + " "

final_command = f'cmd /V /C "set unique={needed_chars}&&FOR; %A IN ({needed_index}) DO set final=!final!!unique:~%A,1!&& CALL %final:~-{target_len}%"'
print(final_command)
