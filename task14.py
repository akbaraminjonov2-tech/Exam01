fayl = input("Fayl nomini kiriting: ")

if fayl.endswith(".pdf"):
    print("Fayl turi: pdf")

elif fayl.endswith(".docx"):
    print("Fayl turi: docx")

elif fayl.endswith(".txt"):
    print("Fayl turi: txt")

else:
    print("Noma'lum fayl turi")