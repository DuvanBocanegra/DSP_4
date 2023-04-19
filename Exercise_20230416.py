import numpy as num
import matplotlib.pyplot as matlab
#Input Signal

x = []
t=num.arange(-4,6,1)
for i in t:
    if i >= 0:
        x.append(int(1))
    elif i < 0:
        x.append(int(0))

LIT=num.arange(1,20,1)
## LIT

y_1 = []
y_2 = []
amp = 0.5
for i in LIT:
    y_1.append(float(amp ** (i-1)))
# LIT inversa

LIT_3 = [3.814697265625e-06,7.62939453125e-06,1.52587890625e-05,3.0517578125e-05,6.103515625e-05,0.0001220703125,0.000244140625,0.00048828125,0.0009765625,0.001953125,0.00390625,0.0078125,0.015625,0.03125,0.0625,0.125,0.25,0.5,1.0]
stm = num.convolve(x,LIT_3)
matlab.stem(stm)
# Signal h(-k) + x(n)


## Stem h(k)


matlab.stem(LIT,y_1)
matlab.xlabel('x')
matlab.ylabel('t')
matlab.title('h(k)')


## Stem x(n)
matlab.stem(t,x)
matlab.xlabel('x')
matlab.ylabel('t')
matlab.title('x(n)')
matlab.show()

## Stem h(-k)
matlab.stem(LIT_2,y_1)
matlab.xlabel('x')
matlab.ylabel('t')
matlab.title('LIT Inversa')
matlab.show()