print( "Enjoy Custom Game World" )
while True:
    tmp = input("게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다. => ").strip()
    if not tmp: 
        print("정확하게 입력하세요!")
        pass
    elif len(tmp)>20:
        print("20자가 초과되었습니다")
        pass
    else:
         gameTitle = tmp
         break
         pass
    pass
print ( 'gameTitle', gameTitle )