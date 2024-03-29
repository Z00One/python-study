########## 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
# random 호출
import random
# 필요한 변수들 선언
answer           =   []         # 답을 담아줄 변수
Range_List       =   ["0"] * 3    # for 문의 range를 조절할 변수






# ########################################################## 교수님 말씀 의미없는(효율적이지 않은 것은 하지 마라) --> while 문이 효율적이다.
# 리스트에 3가지 값이 중복이 되지 않도록 출력 (for 써보기)
# for 문의 range 의 길이가 계속 길어지도록
for answer_index in Range_List:  # list 자리에 range 함수를 쓸 때 range(value) 의 value 값은 초기 값대로만 적용된다. --> list를 사용한다.
    randomValue = random.randint(1,9)
    # 만약 난수가 리스트에 있을 시에 Range_List 값을 올려주고 한 번 더 하고 컨티뉴
    if randomValue in answer:
        Range_List.append("0")
        continue
    # 없으면 추가
    answer.append(randomValue)









########## 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력

# 필요한 변수 선언
try_count       =   1   # 횟수 카운트 변수
out_count       =   0   # 아웃 카운트 변수

while True:
    # 시도횟수 출력
    print("시도횟수 :",try_count)
    
    # 정수 3개 입력받기
    inputValue      =   input("정수를 3개 입력하세요 \n")
    inputValue      =   [int(inputValue[0]),int(inputValue[1]),int(inputValue[2])]

    # 필요한 변수 선언
    strike_count    =   0   # 스트라이크 카운트
    ball_count      =   0   # 볼 카운트
    index_value     =   0   # 인덱스 카운트



# ##############################교수님이라면 이렇게 짠다고 말씀하셨다
    # 볼, 스트라이크 판별
    for index in range(3):
        if inputValue[index] == answer[index]:
            # 스트라이크
            strike_count += 1
        elif inputValue[index] in answer:
            # 볼
            ball_count += 1

    # 삼진 또는 볼+스트라이크 현황 출력
    if strike_count == 0 and ball_count == 0:
        print("삼진")
        out_count += 1
    else:
        print("Strike : ", strike_count, " Ball : ", ball_count)












    ##### 입력 받은 값이 답과 맞는 지 판별하기
    for value in inputValue:
        # 입력 받은 값이 답 안에 있는 경우
        if value in answer:
        # 인덱스 값이 같다면 스트라이크
            if value == answer[index_value]:
                strike_count    += 1
            # 아니면 볼
            else:
                ball_count      += 1
        index_value  += 1

    ##### 결과 값 출력하기
    print()
    # 스트라이크 부터 출력 하기
    if strike_count:
        print(strike_count, "Strike", end=' ')
    # 볼 출력
    if ball_count:
        print(ball_count,   "Ball",   end=' ')
    # 아웃출력 -- 하나도 안 맞는 경우
    if not(strike_count) and not(ball_count):
        out_count += 1
        print(out_count,    "아웃",   end=' ')
    print()
    print()

    # 한 번 게임이 끝나면 시도횟수 카운트
    try_count += 1


# ############################# 교수님 말씀 --> 다 꺼내서 따로 해라 조건문이 바뀌면 아래의 모든 조건을 바꿔줘야험 종속성의 문제가 생긴다.
    ##### 종료하는 경우
    if  try_count>=7   or   out_count>=2   or   strike_count == 3 :
        # 종료 안내문 출력
        # – 시도 횟수 >= 5
        if try_count   >= :
            print("시도횟수 초과")
            print("아까비 졌네용")
        # – Strike out == 2
        elif out_count >= 2:
            print("아웃횟수 초과")
            print("아까비 졌네용")
        # - 3 Strike
        else:
            print("이겼네요")
        print("정답은",answer[0], answer[1], answer[2], "이에요")
        break
