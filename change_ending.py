fruits = {
    'apple': 1000,
    'banana': 2000,
    'plum': 500,
    'peach': 4000
}

fruit = input("어서옵쇼~ 어떤 과일을 찾으세요? ")

if fruit in fruits:
    print(f"아! {fruit}는 {fruits[fruit]}원입죠~")
else:
    print(f"아이고~ {fruit}는 매장에 없네요.")


print(f'가격판 종료')