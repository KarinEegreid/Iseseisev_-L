import turtle

# Funktsioon, mis loeb failist andmed ja teisendab need kilpkonna liikumiseks sobivaks formaadiks
def loe_juhendid(kilpkonn):
    juhendid = []
    with open(kilpkonn, 'r') as f:
        for rida in f:
            käsk = rida.strip().split(' ')
            juhendid.append(käsk)
    return juhendid

# Funktsioon, mis joonistab kilpkonna järgi geomeetrilise kujundi
def joonista_kujund(kujund, kilpkonn):
    for käsk in kujund:
        if käsk[0] == 'edasi':
            kilpkonn.forward(int(käsk[1]))
        elif käsk[0] == 'tagasi':
            kilpkonn.backward(int(käsk[1]))
        elif käsk[0] == 'paremale':
            kilpkonn.right(int(käsk[1]))
        elif käsk[0] == 'vasakule':
            kilpkonn.left(int(käsk[1]))

# Küsime kasutajalt, mitu korda kujund joonistada
kordade_arv = int(input("Mitu korda kujund joonistada? "))

# Loeme failist juhendid
juhendid = loe_juhendid('kilpkonn.txt')

# Loome akna ja kilpkonna
a = input("Sisestage soovitud värv inglise keeles: ")
aken = turtle.Screen()
aken.bgcolor(a)
k = turtle.Turtle()
k.speed(0)

# Joonistame kujundid vastavalt kasutaja sisestatud kordade arvule
for i in range(kordade_arv):
    joonista_kujund(juhendid, k)

# Lõpetame programmi, kui kasutaja vajutab hiireklahvi või vajutab klahvikombinatsiooni Ctrl+C
turtle.exitonclick()
