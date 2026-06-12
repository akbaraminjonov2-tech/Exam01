age = int(input("Yosh: "))

price = 100000
discount = 0

if 0 <= age <= 6:
    discount = 0.5
elif 7 <= age <= 17:
    discount = 0.2
elif age > 60:
    discount = 0.3

final_price = int(price * (1 - discount))

print(f"Yakuniy narx: {final_price} so'm ({int(discount*100)}% chegirma qo'llanildi)")