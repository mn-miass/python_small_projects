import time

if __name__ == "__main__":
    my_time = int(input("Enter time in seconds: "))

    for x in range(0, my_time):
        seconds = x % 60
        minutes = int(x / 60)
        houres = int(x / 3600)
        print(f"{houres:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    
    print("Times up!")