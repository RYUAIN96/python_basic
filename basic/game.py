# 절차적 프로그램 실습
# 간단한 게임을 구현하여
# 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다
# 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어 등을 프로그램을 개발하면서
# 심화학습한다.
#-----------------------------------------------------------------------------------------------------------
# step1 게임이 시작하면 "Enjoy Custom Game World" 라는 문구를 출력한다
# step2
#   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구를 출력한다
#       -> 매번 입력을 대기할 때 마다 해당 프럼프트를 출력하겠다
#   2-2 사용자가 입력할때까지 무제한으로 대기한다
#   2-3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다.
#   2-4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다
#   2-5 20자 이내로 입력하면 gameTitle 라는 변수에 게임 제목을 담고 3 단계로 진입한다
# step3 
#   3-1 "플레이어의 닉네임을 입력하시오, 15자로 제한한다"
#   3-2 입력에 대한 처리는 step2와 동일하다
#   3-3 플레이어의 이름은 player_name이라는 변수에 담는다
# step4
#   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
#   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력한다.
#   4-3 게임 난이도는 game_level 이라는 변수에 담는다

print( "Enjoy Custom Game World" )
#   2-2 사용자가 입력할때까지 무제한으로 대기한다
while True:# 반드시 내부에 break가 있어야 한다
    #2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구를 출력한다
    #       -> 매번 입력을 대기할 때 마다 해당 프럼프트를 출력하겠다
    # 사용자가 엔터키를 칠때까지 코드를 블럭하고 있다 코드가 더 가지 않도록 막는다
    tmp = input("게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다. => ").strip()
    if not tmp: # 2-3 아무것도 입력하지 않고 엔터를 치면
        # 스페이스바를 몇번치고 엔터를 친 것도 같이 처리한다 =
        # 2-3-1 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다.
        print("정확하게 입력하세요!")
    elif len(tmp)>20: # 2-4 20자 이상 입력하면
        print("20자가 초과되었습니다")
        # 2-4-1 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다
    else: # 2-5 20자 이내로 입력하면
         # 2-5-1 gameTitle 라는 변수에 게임 제목을 담고
         gameTitle = tmp
        # 다음 3단계로 진입한다 
         break
# 3단계
# gameTitle이 정의된 곳 -> while 안에 else 안에서 정의
# while 밖에서도 사용이 가능하다
# 함수나 클래스 내부에서 정의된 변수가 아닌 변수들은 모두 전역변수이다.(어느곳에서든지 사용 가능하다) <- variable scope (범위)
print ( 'gameTitle', gameTitle )
while True:
    tmp = input("플레이어의 닉네임을 입력하시오, 15자로 제한한다. => ").strip()
    if not tmp:
        print("정확하게 입력하세요!")
    elif len(tmp)>15:
        print("15자가 초과되었습니다")
    else:
        player_name = tmp
        break
print ( 'player_name', player_name )

# step4
#   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
#   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력한다.
#   4-3 게임 난이도는 game_level 이라는 변수에 담는다

while True:
    tmp = input("게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다. => ").strip()
    if tmp:
        print("정확하게 입력하세요!")
    elif 0<len(tmp)<10:
        print('game_level', game_level)
    else:
        tmp = input(a)
            if type(tmp) = int(a)
                print( "에러" )
        break