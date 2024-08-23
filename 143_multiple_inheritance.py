class Transmitter: 
    def __init__(self): 
        print("In Transmitter.__init__()") 
        print("Returning from Transmitter.__init__()")
    
    def transmit(self): 
        print("In Transmitter.transmit")
        print("Returning from Transmitter.transmit()")

class Receiver: 
    def __init__(self): 
        print("In Receiver.__init__()")
        print("Returning from Receiver.__init__()")

    def receive(self): 
        print("In Receiver.receive()")
        print("Returning from Receiver.receive()")

class Radio(Transmitter, Receiver): 
    def __init__(self): 
        print("In Radio.__init__()")
        Transmitter.__init__(self)
        Receiver.__init__(self)
        print("Returning from Radio.__init__()")

def main(): 
    R = Radio() 
    R.transmit() 
    R.receive() 

main()