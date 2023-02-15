# Karl Paju IS22

# Avame faili sammud.txt ja loeme andmed
with open("sammud.txt", "r") as file:
    sammud = [int(line.strip()) for line in file]

# Liidame kokku kogu nädala sammude andmed ja väljastame tulemuse
kokku = sum(sammud)
print(f"Kokku: {kokku}")

# Arvutame päeva keskmise sammude arvu ja väljastame tulemuse
keskmine = kokku / len(sammud)
print(f"Keskmine: {keskmine:.2f}")

# Leiame, millisel päeval oli sammude arv kõige suurem ja millisel päeval kõige väiksem ning väljastame tulemuse
max_sammud = max(sammud)
max_index = sammud.index(max_sammud)
min_sammud = min(sammud)
min_index = sammud.index(min_sammud)

print(f"Kõige rohkem samme kõnnitud oli {max_sammud} ning see oli {max_index+1} päeval.")
print(f"Kõige vähem samme kõnnitud oli {min_sammud} ning see oli {min_index+1} päeval.")
