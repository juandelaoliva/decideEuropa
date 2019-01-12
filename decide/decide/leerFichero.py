#Los emails se escriben en las líneas pares y el pass en las impares
#Por norma, el primer email y pass es el de decide-europa
def ficheroCorreoContrasena():
    emails = []
    passwords = []
    try:
        with open("decide/emails.txt") as f:
            lines = f.readlines()
            for i in range (len(lines)):
                data = (lines[i].split(" = "))[1]
                if(i%2 == 0):
                    emails.append(data[:-1])
                else:
                    passwords.append(data[:-1])
        f.close()
    except FileNotFoundError:
        with open("decide/emails_dummy.txt") as f:
            lines = f.readlines()
            for i in range (len(lines)):
                data = (lines[i].split(" = "))[1]
                if(i%2 == 0):
                    emails.append(data[:-1])
                else:
                    passwords.append(data[:-1])
        f.close()
    return (emails, passwords)


if __name__ == '__main__':
    ficheroCorreoContrasena()
