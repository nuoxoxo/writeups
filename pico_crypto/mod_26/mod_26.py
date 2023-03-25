s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
r = ""
for c in s:
    code = ord(c)
    if ord(c) <= ord('Z') and ord(c) >= ord('A'):
        code -= 13
        if code < ord('A'):
            code = ord('Z') - ord('A') + code + 1
    elif ord(c) <= ord('z') and ord(c) >= ord('a'):
        code += 13
        if code > ord('z'):
            code = code - ord('z') + ord('a') - 1
    print(chr(code), end='')
    r += chr(code)
assert r == "picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}"
