import math

최대공약수: math.gcd(a, b)
분수 약분할 때 씀

```python
import math

# 4/8 약분
a = 4
b = 8
gcd = math.gcd(a, b)

print(a // gcd, b // gcd)  # 1 2
```
