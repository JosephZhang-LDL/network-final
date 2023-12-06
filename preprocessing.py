def preprocess(_fin, _fout, ip):
    '''
    Pre process the FIBs into flash format

    Input format:
    Destination, gateway, flags, netif, expire

    Output format:
    fw, ipv4, prefix, outport
    fw: type
    ipv4: device ip
    prefix: the ip prefix
    outport: the port to be sending to
    '''
    f = open(_fin, 'r')

    res = []
    for line in f.readlines():
        curr = ""
        destination, gateway, flags, netif, expire = line.split()

        curr += "fw,"
        curr += "".join(destination.split("/")[0].split(".")) + ","
        curr += destination.split("/")[-1] + ","
        curr += gateway
        curr += "\n"

        res.append(curr)

    f.close()

    f = open(_fout, 'w')

    for line in res:
        f.write(line)

    f.close()

if __name__ == "__main__":
    preprocess("fib.txt", "out.txt", "192.168.1.2")