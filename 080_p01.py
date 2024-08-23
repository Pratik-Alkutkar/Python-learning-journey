""" 
Screen Resolution: {'resX':1920, 'resY':1080}
"""

class ScreenResolution: 
    def __init__(self, init_resX, init_resY): 
        self.resX = init_resX 
        self.resY = init_resY 

def main(): 
    
    m1_sr = ScreenResolution(1920, 1080)
    m2_sr = ScreenResolution(3840, 2160)
    m3_sr = ScreenResolution(1024, 768)

    print(m1_sr.__dict__)
    print(m2_sr.__dict__)
    print(m3_sr.__dict__)

    print("type(m1_sr):", type(m1_sr))
    print("type(m2_sr):", type(m2_sr))
    print("type(m3_sr):", type(m3_sr))

main()
