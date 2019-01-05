
def ficheroCorreoContraseña():
    with open("properties.txt") as f:
        lines = f.readlines()
        email = (lines[0].split(" = "))[1]
        passw = (lines[1].split(" = "))[1]

    f.close()
    print(email,passw)
    return (email, passw);


if __name__ == '__main__':
    ficheroCorreoContraseña()
