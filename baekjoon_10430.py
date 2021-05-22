"""
백준 10430 - 나머지

간단한 출력문제. 곱하기 연산기호는 코드에서는 *로 사용된다는 점에 주의하며 출력문을 작성하도록 하자.
안그러면 컴파일 에러를 만나게 될지도...?
"""

import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) *(B%C))%C)