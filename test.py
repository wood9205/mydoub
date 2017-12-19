import base64
x=['MjE2LjE4OS4xNTguMTQ3OjU3ODQ6YXV0aF9hZXMxMjhfc2hhMTpjaGFjaGEyMDp0bHMxLjJfdGlja2V0X2F1dGg6Wkc5MVlpNXBieTl6YzNwb1puZ3ZLbVJ2ZFdJdVltbGtMM056ZW1obWVDOHFOVGM0TkEvP3JlbWFya3M9NXB5czZMU201WS0zNXAybDZJZXFPbVJ2ZFdJdWFXOHZjM042YUdaNEwtbVZuT1dEai1XZm4tV1FqVHBrYjNWaUxtSnBaQzl6YzNwb1puZ3Y']
x[0] += "=" * ((4 - len(x[0]) % 4) % 4)
y=str(base64.b64decode(x[0].encode('utf-8')),encoding='utf-8')
y=y.split(':')
print(y)
pwd=y[5].split('/?remarks=')
pwd[0] += "=" * ((4 - len(pwd[0]) % 4) % 4)
print(pwd[0])
password=base64.b64decode(pwd[0].encode('utf-8'))
print(password)