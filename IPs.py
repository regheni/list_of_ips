f = open("list_of_ips.txt", "w")
for ip1 in range(0, 256):
    for ip2 in range(0, 256):
        for ip3 in range(0, 256):
            for ip4 in range(0, 256):
                f.write("%s.%s.%s.%s" % (ip1, ip2, ip3, ip4))
                f.write("\n")
f.close()
