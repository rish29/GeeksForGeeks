#code
no_of_testcases = int(input())

while no_of_testcases:
    transactions = 0
    no_of_person = int(input())
    money_each_person_have = input().split()
    money_each_person_have = [int(i) for i in money_each_person_have]
    can_money_divided_equally = sum(money_each_person_have) % no_of_person
    if can_money_divided_equally != 0:
        print(-1)
    else:
        average_money_one_can_have = sum(money_each_person_have) / no_of_person
        for money in money_each_person_have:
            if abs(average_money_one_can_have - money) % 3 == 0:
                transactions += abs(average_money_one_can_have - money) / 3
            else:
                print(-1)
                break
        else:
            print(int(transactions/2))
    no_of_testcases -= 1