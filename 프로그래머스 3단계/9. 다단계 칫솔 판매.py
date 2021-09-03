def solution(enroll, referral, seller, amount):
    answer = []
    # 가격
    price = {}
    price['-'] = 0
    for i in enroll:
        price[i] = 0
    for i in range(len(amount)):
        amount[i] *= 100

    # db
    db = {}
    for i in range(len(referral)):
        if enroll[i] in db.keys():
            db[enroll[i]].append(referral[i])
        else:
            db[enroll[i]] = referral[i]

    # print(db)

    def dfs(seller, amount):  # 1200
        try:
            givePrice = (amount // 10)
            getPrice = amount - givePrice
            price[seller] += getPrice
            # print(seller, getPrice, givePrice)
            if seller == '-' or amount <= 1:
                return
            dfs(db[seller], givePrice)
        except:
            print()

    for i in range(len(seller)):
        dfs(seller[i], amount[i])

    result = list(price.values())
    return result[1:]


"""
["-", "-",       "mary", "edward", "mary", "mary", "jaimie", "edward"]
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
["young", "john", "tod", "emily", "mary"]
[12, 4, 2, 5, 10]
"""