# Project3 : 개복치 키우기


# Dead function
def dead(reason):
  # Dead
  print("-" * 70)
  print(f"Game Over!! {reason}")
  print("""           ,-.           ,.---'''^\                  
            {   \       ,__\,---'''''`-.,          
             I   \    K`,'^           _  `'.     
             \  ,.J..-'`          // (X)   ,,X,    
             /  (_               ((   ~  ,;:''`  
            /   ,.X'.,            \\      ':;;;:
           (_../      -._                  ,'`
                       K.=,;.__ /^~/___..'`
                               /  /`
                               ~~~  Zeus""")
  print("-" * 70)


## 인삿말
print("-" * 70)
print("안녕하세요! 개복치 키우기에 게임에 오신 것을 환영합니다!")
print("-" * 70)

print("""           ,-.           ,.---'''^\                  O
          {   \       ,__\,---'''''`-.,      O    O
           I   \    K`,'^           _  `'.     o
           \  ,.J..-'`          // (O)   ,,X,    o
           /  (_               ((   ~  ,;:''`  o
          /   ,.X'.,            \\      ':;;;:
         (_../      -._                  ,'`
                     K.=,;.__ /^~/___..'`
                             /  /`
                             ~~~  Zeus""")
print("-" * 70)

while True:
  # 이름 만들기
  name = input("개복치의 이름을 지어주세요. > ")

  # 첫 인사
  print(f"[{name}]: 주인님 안녕하세요! 좋은 아침이에요 >ㅁ<")
  chat1 = input("[User]: ")
  if chat1 == "":
    dead("인사를 받아주지 않아 상처받아 죽었습니다")
  else:
    print(f"[{name}]: 오늘은 뭘 할까요? (여행갈까?: Walk, 일광욕할까?: Sunbath)")
    chat2 = input("[User]: ").lower()
    if chat2 == "walk":
      dead("지난 여행의 트라우마가 생각나 심장마비로 죽었습니다")
    else:
      print(f"[{name}]: 일광욕 중 zZZ..... ")
      print(f"[{name}]: 주인님 배고파요 (해파리: jellyfish, 오징어: squid)")
      chat3 = input("[User]: ").lower()
      if chat3 == "jellyfish":
        dead("알 수 없는 독에 중독되었습니다.")
      else:
        print(f"[{name}]: 쩝쩝쩝.. 너무 맛있어요!")
        print(f"[{name}]: 아 졸린다. 이제 다시 일광욕하러 가도 되요? (응: Yes, 아니: No)")
        chat4 = input("[User]: ").lower()
        if chat4 == "yes":
          dead("커다란 새에게 공격받아 죽었습니다.")
        else:
          print("-" * 70)
          print("Success!! Congratulations! 오늘도 너무 재미있었어요!!")
          print("""           ,-.           ,.---'''^\                  O
          {   \       ,__\,---'''''`-.,      O    O
           I   \    K`,'^           _  `'.     o
           \  ,.J..-'`          // (♡)   ,,X,    o
           /  (_               ((   ~  ,;:''`  o
          /   ,.X'.,            \\      ':;;;:
         (_../      -._                  ,'`
                     K.=,;.__ /^~/___..'`
                             /  /`
                             ~~~  Zeus""")
          print("-" * 70)

  more = input("다시 하시겠어요? ('Yes' or 'No') > ").lower()
  if more == 'no':
    print("게임을 종료합니다. 다음에 또 만나요~")
    break
