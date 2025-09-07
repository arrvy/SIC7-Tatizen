def konversi_suhu(nilai, dari, ke):
    hasil = 0
    if dari == "C" and ke == "F":
        try:
            hasil = ((nilai/5)*9)+32
        except:
            "Something Error"
    elif dari == "C" and ke == "K":
        try:
            hasil = nilai+273.15
        except:
            "Something Error"
    elif dari == "F" and ke == "C":
        try:
            hasil = (((nilai-32)/9)*5)
        except:
            "Something Error"
    elif dari == "F" and ke == "K":
        try:
            hasil = (((nilai-32)/9)*5)+273.15
        except:
            "Something Error"
    elif dari == "K" and ke == "C":
        try:
            hasil = nilai-273.15
        except:
            "Something Error"
    elif dari == "K" and ke == "F":
        try:
            hasil = (((nilai-273.15)/9)*5)+32
        except:
            "Something Error"
    else:
        "nilai tidak ada"
    # print(hasil)
    return hasil

def inputValidation(value,str):
    loop = True
    while loop:
            value = input(str).upper()
            # print(value,"H")
            match value:
                case "F":
                    # print("1")
                    loop = False    
                    return value
                case "C":
                    # print("2")
                    loop = False    
                    return value
                case "K":
                    # print("3")
                    loop = False    
                    return value
                case _:
                    print("Ngisi yang bener mas")
                    continue
            