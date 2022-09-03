with open('wordlist.txt', 'r') as inf:
    content = inf.readlines()

with open('wordlist.txt', 'a') as outf:
    for line in content:
        outf.write(line.replace('`', "´"))