import random

kok="çağ"
ekler=["la","ra","tı","lı","ıl","rı","şı","lat","laş"]
eklen=""
toplam=10

for isim in range(toplam):
    for i in range(random.randrange(1,4)):
        ek=ekler[random.randrange(len(ekler))]
        if len(ek)==1:
            arabul=[e for e in ekler if len(e)>1]
            ek+=arabul[random.randrange(len(arabul))]
        eklen+=ek
    print(kok+eklen)
    eklen=""    

