"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.


예시
<입력>
print(Triangle(10,20))

<출력>
100

"""
def Triangle(a,b):
    return (a*b/2)

a=int(input('삼각형 가로 입력 :'))
b=int(input('삼각형 높이 입력 :'))
print(f'{Triangle(a,b):.0f}')
