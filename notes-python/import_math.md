# math

[← 전체 목록](README.md)

```python
import math
```

## 함수 목록

| 함수 | 하는 일 | 언제 사용하나 |
| --- | --- | --- |
| `math.gcd(a, b)` | 두 정수의 최대공약수 | 분수 약분하기 |

## math.gcd(a, b) — 최대공약수

두 정수 `a`, `b`를 모두 나누어떨어지게 하는 가장 큰 양의 정수를 반환한다.

### 기본 사용법

```python
import math

print(math.gcd(4, 8))  # 4
print(math.gcd(12, 18))  # 6
print(math.gcd(3, 7))  # 1: 서로소
```

### 활용: 분수 약분하기

분자와 분모를 최대공약수로 각각 나누면 기약분수가 된다.

```python
import math

numerator = 4  # 분자
denominator = 8  # 분모

gcd_val = math.gcd(numerator, denominator)

simplified_num = numerator // gcd_val
simplified_den = denominator // gcd_val

print(simplified_num, simplified_den)  # 1 2
```

### 기억할 점

- 정수를 인자로 넣는다.
- 약분할 때는 정수 나눗셈 `//`를 사용한다. `/`는 실수를 반환한다.
- 음수를 넣어도 최대공약수는 음수가 되지 않는다.
- `math.gcd(0, n)`은 `abs(n)`, `math.gcd(0, 0)`은 `0`이다.
