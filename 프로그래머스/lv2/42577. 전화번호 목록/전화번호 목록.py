def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for i in range(length-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True