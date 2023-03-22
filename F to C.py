fahrenheit = float(input('화씨 입력: '))
celsius = (fahrenheit - 32.0) * (5.0/9.0)
print("화씨 %lf도는 섭씨 %lf도 입니다" % (fahrenheit, celsius))
print(f"화씨 {fahrenheit:.2f}는 섭씨 {celsius:.2f}도 입니다")
 