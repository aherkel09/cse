def checkval(password):
    has_length = False
    has_lc = False
    has_uc = False
    has_num = False
    has_special = False
    if len(password) >= 6 and len(password) <= 16:
        has_length = True
    for p in password:
        if p.isdigit():
            has_num = True
        elif p.islower():
            has_lc = True
        elif p.isupper():
            has_uc = True
        else:
            if p in ['$', '#', "@"]:
                has_special = True
    if has_length and has_lc and has_uc and has_num and has_special:
        return(print("Password is valid."))
    return(print("Your password sucks. Please try a different password."))

checkval("75gfgGdh#")
                
                
