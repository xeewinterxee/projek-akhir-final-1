import time
import sys

def loading_efek():
    for i in range(3):  
        sys.stdout.write("Loading" + "." * (i + 1))  
        sys.stdout.flush()  
        time.sleep(0.5) 
        sys.stdout.write("\r")  
    
    print("Kembali ke menu utama!")

if __name__ == "__main__":
    loading_efek()
