import cherrypy ,os ,binascii
global added
port = 8080 #<Port To Listen On>
class Main(object):
    global added
    added=[]
    @cherrypy.expose
    def index(self):
        try:
            a="<h1> Connections :\n</h1><h2>"
            f=open("Connections.txt","r")
            ips = f.readlines()
            for i in ips:
                a += "["+str(ips.index(i))+"] "+str(i) +"<br />"
            f.close()
            a +="</h2>"
            return a
        except :
            return "<h1> No Connections Yet ! !</h1>"

    @cherrypy.expose
    def NewConnection(self, ip):
        ip = binascii.unhexlify(ip)
        try:
            if ip not in added:
                a = open("Connections.txt","a")
                added.append(ip)
                a.write(str(ip)+"\n")
                a.close()
                return "Ok"
        except:
            if ip not in added:
                a = open("Connections.txt","w")
                added.append(ip)
                a.write(str(ip)+"\n")
                a.close()
                return "Ok"


if __name__ == '__main__':
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = port
    cherrypy.quickstart(Main())
