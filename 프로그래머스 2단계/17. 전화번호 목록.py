def solution(phone_book):
    # phone_book = sorted(phone_book, key = lambda x : (len(x), int(x)))
    # answer = True
    # for i in range(len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         n = len(phone_book[i])
    #         if phone_book[j][:n] == phone_book[i]:
    #             answer = False
    #             break
    db = {}
    phone_book = sorted(phone_book, key = lambda x : (int(x)))
    min_size = len(phone_book[0])
    answer = True
    for i in phone_book:
        for j in range(min_size, len(i)+1):
            if i[0:j] not in db.keys():
                if j == len(i):
                    db[i[0:j]] = 0
            else:
                return False
    return answer
a =  ["119", "114", "112", "123223123", "1231231234"]
print(solution(a))