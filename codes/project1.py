# Project1 : 이름 생성기 만들기
isquit = 1

print("-" * 70)
print("안녕하세요! 아이디 추천 프로그램에 오신 것을 환영합니다!")
print("-" * 70)
while isquit == 1:
  print("다음 3가지의 질문에 대해 답해주세요 :)")

  food = input("질문1. 가장 좋아하는 음식이 무엇인가요? > ")
  color = input("질문2. 좋아하는 색이 무엇인가요?(00색) > ")
  animal = input("질문3. 좋아하는 동물이 무엇인가요? > ")

  print(f"저는 '{food}먹는{color}{animal}'(을)를 추천드릴게요!")
  isquit = int(input("다시 해볼까요?('Y': 1, 'N': 0) > "))
  while True:
    if isquit == 1:
      print("-" * 70)
      break
    elif isquit == 0:
      print("-" * 70)
      print("이용해주셔서 감사합니다 :)")
      print("-" * 70)
      break
    else:
      isquit = int(input("잘못 입력하셨습니다. 다시 입력해주세요('Y': 1, 'N': 0) > "))
