while True:
    try:
        a= float(input("a: "))
        b= float(input("b: "))
        op= input("op: (+ - * /) ")
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            if b == 0:
                print("MUMKIN EMAS")
            else:
                print(a/b)
    except ValueError:
        print("Invalid input")





