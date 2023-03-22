while True
    menu = int(input("1) fahrenheit to celsius   2) celsius to fahrenheit   3) exit  : "))

    if menu == 1:
       fahrenheit = float(input('화씨 입력: '))
       celsius = (fahrenheit - 32.0) * (5.0/9.0)
       print(f"화씨 {fahrenheit:.2f}는 섭씨 {celsius:.2f}도 입니다")

    elif menu == 2:

       celsius = float(input('섭씨 입력: '))
       fahrenheit = (celsius * 9.0/5.0) + 32.0
       print(f"섭씨 {celsius:.2f}는 화씨 {fahrenheit:.2f}도 입니다")

    elif menu == 3:
        break
    else:
        print("please choose menu")

print("Program finished")


 #(0°C × 9/5) + 32 = 32°F
