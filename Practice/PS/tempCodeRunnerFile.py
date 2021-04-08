answer = []

if not (8 <= len(inp_str) <= 15):
    answer.append(1)

second_ck = True
for c in inp_str:
    if not (('A' <= c <= 'Z') or ('a' <= c <= 'z') or (0 <= int(c) <= 9) or (c in '~!@#$%^&*')):
        answer.append(2)
        break
