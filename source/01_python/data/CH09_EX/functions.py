# functions.py => fn1~()부터 fn9()
from customer import Customer
def fn1_insert_customer_info():
    '''
    사용자로부터 name, phone, email, age, grade, etc를 입력받아 Customer형 객체 반환
    '''
    import re
    name = input('이름 :')
    name_pattern = r'[가-힣]{2,}'
    while not re.search(name_pattern, name):
        print('이름을 제대로 입력하세요(한글 2글자 이상)')
        name = input('이름 :')
    phone = input('전화 :')
    email = input('메일 :')
    while True:
        try:
            age = int(input('나이 :'))
            if (age<0) or (age>130) :
                raise Exception('나이 범위 이상')
            break 
        except:
            print('올바른 나이를 입력하세요')
    try:
        grade = int(input('등급(1~5) : '))
        # grade = 1 if grade < 1 else 5 if grade>5 else grade
        if grade < 1:
            grade = 1
        if grade > 5:
            grade = 5
    except:
        print('유효하지 않은 등급 입력시 1등급으로 초기화')
        grade = 1
    etc = input('기타 정보 :')
    return Customer(name, phone, email, age, grade, etc)