# module

# ------------------------------------------------------------------------------------
## 모듈 만들기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

form mod1 import add
add(3, 4)

# ------------------------------------------------------------------------------------
## 클래스나 변수 등을 포함한 모듈

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

# ------------------------------------------------------------------------------------
## 다른 파일에서 모듈 불러오기





