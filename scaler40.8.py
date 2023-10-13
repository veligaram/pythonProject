def verify(s):
    freq_attherate = 0
    freq_dot = 0
    for i in range(len(s)):
        if (s[i] == "@"):
            freq_attherate += 1
        elif (s[i] == "."):
            freq_dot += 1
    if (freq_attherate == 1 and freq_dot >= 1):
        user, domain = s.split("@")

        if (len(user) > 20 or len(user) <= 0):
            return False

        if (len(domain) <= 0):
            return False
        return True
    else:
        return False


def check(emails):
    verified_lex = None
    verified_lex = list(filter(verify, emails))
    verified_lex.sort()
    return verified_lex
print(check(["sara@scaler.com", "brian-23@scaler.com","brute_54@scaler.com"]))