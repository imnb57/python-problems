# . removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython


bad_chars = [';', ':', '!', "*"]
string = "py;th*o:n ! ;py*t*h:o!n"
for i in bad_chars:
    string = string.replace(i, "")
    continue
print(string)
