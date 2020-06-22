
SECURE = (('s', '$'), ('and','&'), ('a', '@'), ('o', '0'), ('i', '1'), ('@', 'a'), ('h', '#'), ('1', '!'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password: ")
    password = securePassword(password)
    print(f"Your secure password is {password}")