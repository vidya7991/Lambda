import time

def count_to_ten():
    print("Counting from 1 to 10...\n")
    for i in range(1, 11):
        print(i)
        time.sleep(1)  # wait 1 second between numbers
    print("\nDone!")

if __name__ == "__main__":
    count_to_ten()
