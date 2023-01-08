print("i am starting")

def main():
    a = int(input("Enter a number: "))
    a *= a
    print(a)

    doStuff(a, a)

def doStuff(a, b):
    if a >= 10:
        c = a * b
        print(c)
        print("this is way better")
    else:
        print(b)
        print("omg omg omg")

if __name__ == "__main__":
    main()
