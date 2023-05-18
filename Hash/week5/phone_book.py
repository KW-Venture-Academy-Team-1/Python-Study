def solution(phone_book):
    # 전화번호부를 해시테이블에 저장
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 전화번호 중에 다른 전화번호의 접두사인 경우가 있는지 검사
    for phone_number in phone_book:
        for i in range(len(phone_number)):
            prefix = phone_number[:i]
            if prefix in hash_map and prefix != phone_number:
                return False
    return True
