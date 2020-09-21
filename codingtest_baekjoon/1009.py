t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a % 10 == 0:
        print(10)

    elif a % 10 == 1 or a % 10 == 5 or a % 10 ==6:
        print(a % 10)

    elif b % 4 ==1:
        print(a%10)

    elif b % 4 == 2:
        if a % 10 == 9 :
            print(1)
        elif a % 10 == 2 or a % 10 == 8 :
            print(4)
        elif a % 10 == 3 or a % 10 == 7 :
            print(9)
        elif a % 10 == 4 or a % 10 == 6 :
            print(6)

    elif b % 4 == 3 :

        if a% 10 == 2:
            print(8)
        elif a% 10 == 3:
            print(7)
        elif a% 10 == 4:
            print(4)
        elif a% 10 == 7:
            print(3)
        elif a% 10 == 8:
            print(2)
        elif a% 10 == 9:
            print(9)

    elif b % 4 == 0:

        if a%2==0:
            print(6)
        else:
            print(1)

            """
                r = a ** b
                if(r%10==0):
                    print(10)
                else:
                    print(r%10)
            """
            """

                if a%10==1:
                    print(1)
                elif a % 10 ==2:
                    if b%4==1:
                        print(2)
                    elif b%4==2:
                        print(4)
                    elif b%4==3:
                        print(8)
                    elif b%4==0:
                        print(6)
                elif a % 10 ==3:
                    if b % 4 == 1:
                        print(3)
                    elif b % 4 == 2:
                        print(9)
                    elif b % 4 == 3:
                        print(7)
                    elif b % 4 == 0:
                        print(1)
                elif a % 10 ==4:
                elif a % 10 ==5:
                elif a % 10 ==6:
                elif a % 10 ==7:
                elif a % 10 ==8:
                elif a % 10 ==9:
                elif a % 10 ==0:
            1 1

            2 4 8 6 2 4 8

            3 9 7 1 3 9

            4 6 4 6 4 6 4

            5 5 5 5 5

            6 6 6 6 6

            7 9 3 1 7

            8 4 2 6 8

            9 1 9 1 9

            10 10

            11 1 1 1 1

            2 144
            """