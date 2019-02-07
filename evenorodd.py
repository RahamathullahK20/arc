#evenorodd
def main():
    x=int(raw_input())
    if(x>0):
        if(x%2==0):
            print("The number is Even")
        else:
            print("The number is odd")
    else:
        print("The number is invalid")
