# Project2 : 더치페이 계산기

## 인삿말
print("-" * 70)
print("안녕하세요! 더치페이 계산기 입니다.")
print("-" * 70)

## 입력받기 
people = input("더치페이 대상자를 입력하세요(구분: 띄어쓰기, ex. A, B)\n> ").split(' ')
isdrink = int(input("주류는 따로 계산하시나요? ('Y': 1, 'N': 0) > "))
money = list(map(int, input("비용을 차례대로 입력해주세요(구분: 띄어쓰기)\n> ").split(' ')))

## 조건문 
### 1) 모두 같은 금액
if isdrink == 0:
  ## 계산
  result = sum(money) / len(people)

  ## 결과
  print('>>> 더치페이 계산 결과입니다.')
  print('-' * 50)
  for p in people:
    print(f'{p}: {result}원')
  print('-' * 50)
  
### 2) 인원별 다른 금액
elif isdrink == 1:
  ## 입력받기
  drink = list(map(int, input("주류 비용을 차례대로 입력해주세요(구분: 띄어쓰기) \n> ").split(' ')))
  subject = list(map(int, input("주류 비용 대상자는 1 비대상자는 0으로 표현해주세요(구분: 띄어쓰기 ex. 1, 0)\n> ").split(' ')))

  # 계산
  result = (sum(money) - sum(drink))  / len(people)
  plus = sum(drink) / len(subject)

  # 결과
  print('>>> 더치페이 계산 결과입니다.')
  print('=' * 50)
  print('총 금 액'.ljust(10) + f': {sum(money):.0f}({"+".join(list(map(str,money)))})')
  print('안 주 류'.ljust(10) + f': {result * len(people):.0f}')
  print('주    류'.ljust(11) + f': {sum(drink):.0f}({"+".join(list(map(str,drink)))})')
  print('-' * 50)
  for s, p in zip(subject, people):
    if s == 1:
      print(f'{p}'.ljust(10) + f'{result + plus:.0f}원')
    else:
      print(f'{p}'.ljust(10) + f'{result:.0f}원')
  print('=' * 50)
