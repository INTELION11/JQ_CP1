# JQ 1st Avarage Numbers Practice
while True:
    class_grd1 = float(input("What is your first period grade?"))
    class_grd2 = float(input("What is your second period grade?"))
    class_grd3 = float(input("What is your third period grade?"))
    class_grd4 = float(input("What is your fourth period grade?"))
    class_grd5 = float(input("What is your fifth period grade?"))
    class_grd6 = float(input("What is your sixth period grade?"))
    class_grd7 = float(input("What is your seventh period grade?"))
    total = class_grd1 + class_grd2 + class_grd3 + class_grd4 + class_grd5 + class_grd6 + class_grd7 
    avarge = (total / 7)
    avarge_rounded = round(avarge,2)
    print(avarge_rounded)
    print("k")