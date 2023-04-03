import pandas as pds
import numpy as np

data = pds.read_csv('Base_pictures_blurry.csv', index_col = 0)
queryl= []
column = (list(data.columns))
Chevu = True

for i in [-1,1] :
    queryi = "Male == " + str(i) + " and "
    for j in [-1,1] :
        queryj = queryi + "Bald == " + str(j) + " and "
        if j == 1 :
            Chevu = False
        for k in [-1,1] :
            queryk = queryj + "Young == " + str(k) + " and "
            for l in [-1,1] :
                queryil = queryk + "Eyeglasses == " + str(l) + " and "
                for m in [0,-1,1]:
                    if m == 0 :
                        querym = queryil + "Bushy_Eyebrows == -1" + " and " + "Arched_Eyebrows == -1" + " and "
                    else :
                        querym = queryil + "Bushy_Eyebrows == "+ str(m) + " and " + "Arched_Eyebrows == "+ str(m*-1) + " and "
                    for n in [0,-1,1]:
                        if n == 0 :
                            queryn = querym + "Big_Nose == -1" + " and " + "Pointy_Nose == -1" + " and "
                        else :
                            queryn = querym + "Big_Nose == "+ str(n) + " and " + "Pointy_Nose == "+ str(n*-1) + " and "
                        for o in [0,-1,1]:
                            if o == 0 :
                                queryo = queryn + "No_Beard == 1" + " and " + "Mustache == -1" + " and "
                            if o == 1 :
                                queryo = queryn + "No_Beard == -1" + " and "
                            if o == -1 :
                                queryo = queryn + "Mustache == 1" + " and "
                            if Chevu :
                                for v in [0,-1,1] :
                                    if v == 0 :
                                        queryv = queryo + "(Brown_Hair == -1" + " or " + "Black_Hair == -1" + ") and " + "(Blond_Hair == -1" + " or " + "Grey_Hair == -1" + ") and "
                                    if v == 1 :
                                        queryv = queryo + "(Brown_Hair == " + str(v) + " or " + "Black_Hair == " + str(v) + ") and " + "(Blond_Hair == " + str(v*-1) + " or " + "Grey_Hair == " + str(v*-1) + ") and "
                                    if v == -1 :
                                        queryv = queryo + "(Brown_Hair == " + str(v) + " or " + "Black_Hair == " + str(v) + ") and " + "(Blond_Hair == " + str(v*-1) + " or " + "Grey_Hair == " + str(v*-1) + ") and "

                                    queryv += " Blurry == - 1"
                                    queryl.append(queryv)
                            else :
                                queryo += " Blurry == - 1"
                                queryl.append(queryo)
total_pics = []
empty_queer = []
for queer in queryl :
    pics = data.query(queer)
    if len(pics) == 0:
        empty_queer.append(queer)
    if len(pics) <= 10 :
        for i in range(len(pics)) :
            total_pics.append(pics.iloc[i])
    else :
        choi = np.random.randint(0,len(pics),10)
        for nb in choi :
            total_pics.append(pics.iloc[nb])
pds.DataFrame(empty_queer).to_csv("empty_queer.csv")
tpic = pds.DataFrame(total_pics)
tpic.to_csv("Total_Base_Pics.csv")
