is_connected: bool = False

def connect_to_internet():
    if not is_connected:
        raise Exception("You are not connected to the internet!") #raise an error
    else:
        print("You are connected to the internet!")
try:
    connect_to_internet()
except Exception as e:
    print(e)