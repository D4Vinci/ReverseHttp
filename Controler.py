import requests ,time ,socket ,binascii ,os
port = 8080 #<Port To Connect On>
connections = []

while 1:
    try:
        a = open("Connections.txt","r")
        c = a.readlines()
        for conn in c:
            connections.append(conn.replace("/n",""))
        a.close()
        break
    except :
        print " There is no connections yet !"
        print " Waiting for 5 seconds.."
        time.sleep(5)
        continue

while True:
    prompt = raw_input(" #Control#> ").lower()
    if prompt == "help":
        print "\n Available Commands"
        print "  help    - print this message"
        print "  list    - list the connections"
        print "  connect - connect device by its id from list commnad"
        print "  exit    - Exit the script"
        print "\n"
        continue
    elif prompt == "list":
        print "\nConnections :"
        for i,conn in enumerate(connections):
            print " ["+str(i)+"] "+str(conn)
        print "\n"
        continue
    elif prompt == "exit":
        exit(0)
    elif prompt.split(" ")[0] == "connect":
        n = int(prompt.split(" ")[1])
        ip = connections[n].replace("\n","")
        print "\n"
        while 1:
            p = raw_input("  [%s]> "%ip)
            if p.lower() == "quit":
                break
            else:
                c = requests.post("http://{0}:{1}/control".format(ip,port),{"cmd":"{0}".format(str(binascii.hexlify(p)))})
                print " "+str(binascii.unhexlify(c.content))
                continue
    else:
        print " Command Not Found"
