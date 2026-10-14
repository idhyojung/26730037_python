#9391 문자열 - 자가진단 7
hour, minute = map(int, input().split())

if hour >= 12:
    ampm = "PM"
    if hour > 12:
        hour -= 12
else:
    ampm = "AM"

print(f"{hour:02d} : {minute:02d} {ampm}")
