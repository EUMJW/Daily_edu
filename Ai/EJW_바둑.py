# -*- coding: utf-8 -*-
"""바둑.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sPCrCTz211ENOoKBYaQy0MTSbXbueQxe
"""

dataset = [0,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,
1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,
0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,
0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,
0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,
0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,
0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,
1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,
0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,
0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,
0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,
0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0]

# 돈 단위는 만원
start_fund = 5000
betting_money = [100,200,400,800,1600,3200,6400,12800,25600,51200] # 등비배팅
# repeat = 1~10
# pettern = [] # repeat 갯수만큼 랜덤하게 생성

import random

# 랜덤 패턴생성
def make_pettern(repeat):
  pettern = []
  for i in range(1,repeat+1):
    pettern.append(random.randint(0,1))
  return pettern




# 데이터셋을 통해 배팅시작
# 일정한 패턴으로 배팅 ex) 흑흑백흑백 흑흑백흑백 흑흑백흑백 ....
# 돈을 잃는다면 다음 배팅머니로 배팅 ex)등차배팅일 경우 100만원에서 잃는다면 200만원, 또 잃으면 400만원
# 돈을 따게된다면 처음 배팅머니로 다시 배팅 
# 최종적으로 갖고있는 돈을 리턴
def betting(pettern, repeat):
  now_fund = start_fund
  betting_num = 0
  index = 0
  while now_fund >betting_money[betting_num]:
    if len(dataset) == index:
      break

    if dataset[index] == pettern[index%repeat]:
      now_fund += betting_money[betting_num]
      betting_num = 0
      index +=1
    
    else:
      now_fund -= betting_money[betting_num]
      betting_num += 1
      index += 1

  return now_fund




# 배팅패턴의 횟수와 배팅패턴을 랜덤하게 만들어 실제 dataset으로 배팅 시뮬레이션
# 가장 크게 수익이 난 수익과 패턴을 리턴
def randomsearch(times):
  max_fund = 0
  for i in range(times):
    repeat = random.randint(1,10)
    pettern = make_pettern(repeat)
    now_fund = betting(pettern, repeat)
    if now_fund > max_fund:
      max_fund = now_fund
      print('얻게되는 돈:',max_fund,'패턴반복횟수:', repeat,'배팅패턴:', pettern)



# 등비배팅
start_fund = 5000
betting_money = [100*2**i for i in range(20)]
print('배팅머니:',betting_money)
randomsearch(100000)

"""
배팅머니: [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400, 3276800, 6553600, 13107200, 26214400, 52428800]
얻게되는 돈: 2200 패턴반복횟수: 9 배팅패턴: [0, 1, 0, 1, 0, 0, 1, 0, 0]
얻게되는 돈: 2500 패턴반복횟수: 2 배팅패턴: [0, 1]
얻게되는 돈: 3700 패턴반복횟수: 9 배팅패턴: [0, 0, 0, 1, 1, 1, 1, 1, 1]
얻게되는 돈: 6600 패턴반복횟수: 4 배팅패턴: [1, 0, 0, 1]
얻게되는 돈: 28800 패턴반복횟수: 5 배팅패턴: [0, 0, 1, 1, 1]
얻게되는 돈: 29500 패턴반복횟수: 4 배팅패턴: [1, 1, 0, 1]
얻게되는 돈: 29900 패턴반복횟수: 10 배팅패턴: [0, 1, 1, 0, 1, 1, 0, 0, 0, 0]
얻게되는 돈: 31000 패턴반복횟수: 6 배팅패턴: [0, 0, 1, 1, 1, 1]
얻게되는 돈: 31100 패턴반복횟수: 10 배팅패턴: [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
"""

# 피보나치 배팅
start_fund = 5000
betting_money = [100, 200, 300, 500, 800, 1300, 2100, 3400, 5500, 8900, 14400, 23300]
print('배팅머니:',betting_money)
randomsearch(100000)

"""
배팅머니: [100, 200, 300, 500, 800, 1300, 2100, 3400, 5500, 8900, 14400, 23300]
얻게되는 돈: 100 패턴반복횟수: 2 배팅패턴: [0, 0]
얻게되는 돈: 15900 패턴반복횟수: 4 배팅패턴: [1, 1, 0, 1]
얻게되는 돈: 17600 패턴반복횟수: 7 배팅패턴: [0, 0, 0, 0, 0, 0, 1]
얻게되는 돈: 20200 패턴반복횟수: 6 배팅패턴: [0, 0, 0, 0, 1, 0]
"""


# 랜덤생성을 통한 배팅패턴
def betting(betting_money, pettern, repeat):
  now_fund = start_fund
  betting_num = 0
  index = 0
  while now_fund >betting_money[betting_num]:
    if len(dataset) == index:
      break

    if dataset[index] == pettern[index%repeat]:
      now_fund += betting_money[betting_num]
      betting_num = 0
      index +=1
    
    else:
      now_fund -= betting_money[betting_num]
      betting_num += 1
      index += 1

  return now_fund

def randomsearch(times):
  max_fund = 0
  for i in range(times):
    # 매번 시도마다 배팅머니의 패턴을 랜덤하게 변경
    betting_money = [random.randint(1,10)*100 for i in range(30)]
    repeat = random.randint(1,10)
    pettern = make_pettern(repeat)
    now_fund = betting(betting_money,pettern, repeat)
    if now_fund > max_fund:
      max_fund = now_fund
      print('얻게되는 돈:',max_fund,'패턴반복횟수:', repeat,'배팅패턴:', pettern, '배팅머니:',betting_money)

start_fund = 5000
randomsearch(100000)


# 랜덤 배팅머니 패턴을 통한 배팅의 경우 처음에 큰 돈으로 시작하는것이 매우 주요하게 작용하였다는걸 추론
"""
얻게되는 돈: 500 패턴반복횟수: 2 배팅패턴: [1, 0] 배팅머니: [800, 600, 500, 100, 300, 800, 100, 800, 1000, 900, 400, 1000, 500, 600, 700, 400, 700, 400, 400, 900, 400, 800, 300, 600, 100, 900, 700, 600, 200, 700]
얻게되는 돈: 15800 패턴반복횟수: 8 배팅패턴: [1, 0, 0, 1, 1, 1, 0, 1] 배팅머니: [700, 400, 700, 900, 1000, 800, 600, 500, 100, 400, 900, 600, 100, 800, 600, 600, 200, 400, 500, 800, 100, 200, 200, 800, 1000, 100, 100, 600, 500, 100]
얻게되는 돈: 23600 패턴반복횟수: 7 배팅패턴: [0, 1, 0, 1, 0, 1, 1] 배팅머니: [600, 600, 900, 800, 700, 500, 200, 1000, 900, 500, 600, 600, 300, 600, 700, 600, 400, 400, 600, 1000, 400, 400, 200, 100, 400, 1000, 200, 300, 100, 1000]
얻게되는 돈: 30000 패턴반복횟수: 8 배팅패턴: [0, 0, 0, 1, 0, 0, 0, 1] 배팅머니: [900, 300, 400, 1000, 700, 100, 700, 900, 200, 100, 300, 900, 200, 600, 1000, 400, 400, 900, 200, 500, 800, 700, 800, 900, 900, 500, 700, 100, 500, 600]
얻게되는 돈: 43200 패턴반복횟수: 6 배팅패턴: [0, 0, 0, 1, 1, 1] 배팅머니: [700, 500, 800, 900, 600, 1000, 700, 200, 400, 700, 1000, 1000, 600, 1000, 1000, 500, 1000, 600, 900, 800, 500, 200, 400, 100, 700, 900, 200, 1000, 300, 100]
얻게되는 돈: 51000 패턴반복횟수: 6 배팅패턴: [0, 0, 0, 1, 1, 1] 배팅머니: [800, 300, 200, 900, 1000, 1000, 200, 700, 700, 400, 200, 500, 800, 500, 400, 400, 1000, 500, 600, 200, 300, 300, 400, 100, 500, 700, 300, 100, 900, 900]
얻게되는 돈: 51900 패턴반복횟수: 6 배팅패턴: [0, 0, 0, 0, 1, 1] 배팅머니: [900, 600, 1000, 300, 1000, 100, 700, 900, 100, 100, 800, 600, 300, 500, 700, 1000, 300, 200, 100, 600, 200, 900, 200, 300, 900, 100, 400, 900, 300, 300]
얻게되는 돈: 53600 패턴반복횟수: 9 배팅패턴: [0, 0, 1, 0, 1, 1, 0, 0, 0] 배팅머니: [1000, 700, 500, 1000, 1000, 700, 500, 200, 700, 400, 700, 900, 700, 500, 200, 300, 200, 700, 100, 1000, 700, 700, 1000, 300, 900, 900, 200, 200, 200, 400]
얻게되는 돈: 55300 패턴반복횟수: 9 배팅패턴: [0, 0, 1, 0, 1, 1, 0, 1, 1] 배팅머니: [1000, 300, 300, 800, 400, 100, 400, 100, 600, 900, 900, 900, 400, 300, 300, 400, 800, 600, 1000, 1000, 200, 700, 300, 100, 100, 600, 1000, 500, 400, 800]
얻게되는 돈: 60900 패턴반복횟수: 9 배팅패턴: [0, 0, 1, 0, 1, 1, 0, 1, 1] 배팅머니: [1000, 200, 200, 900, 600, 500, 200, 900, 400, 200, 1000, 900, 500, 700, 800, 600, 400, 1000, 1000, 900, 400, 300, 700, 800, 300, 1000, 1000, 300, 300, 700]
"""
