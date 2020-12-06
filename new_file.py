def main():
    f = open('newoutput.txt', 'r')
    d = dict()
    l = 0
    m = 0
    n = 0
    while True:
        line = f.readline()
        if not line: break
        if 'end' in line[0:3]:
            line = f.readline()
            l = int(line[0:len(line)])
            line = f.readline()
            m = int(line[0:len(line)])
            line = f.readline()
            n = int(line[0:len(line)])
            break;
    f.close()
    f = open('output.txt', 'a+')
    f.write("\n\n\nNew Algorithm Output ->\n\nTotal no of Active nodes - " + str(l) + "\nTotal resources at all the nodes = " + str(m))
    f.write("\nTotal resources on active nodes = " + str(n))
    f.write("\nTotal unused resources = " + str(m-n))
    f.close()


if __name__ == "__main__":
    main()