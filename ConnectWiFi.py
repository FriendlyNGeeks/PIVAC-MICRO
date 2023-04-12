from secrets import SECRETS # variables stored in env file

def connect():
    import network
 
    ssid = SECRETS.SSID
    password =  SECRETS.PASS
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
    
    #The following statement ensures that the code doesn’t proceed while the ESP is not connected to your network.
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())