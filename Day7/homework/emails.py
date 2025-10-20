

def emails():
    with open("emails.txt", 'w+') as f:
        f.write("name, mailbox\n")
        for i in range(0, 100):
            name = "student" + str(i + 1)
            email = name + "@gmail.com"
            line = name + ", " + email + "\n"
            f.write(line)


if __name__ == '__main__':
    emails()