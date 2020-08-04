from bs4 import BeautifulSoup
import codecs
import pandas as pd

soup = BeautifulSoup(codecs.open(r"C:\Users\ktmks\programming\GUI_app\Data\pokemapi.html","r","utf-8"),"html.parser")

td_tags = soup.find_all("td")

def last_specify():
    i = 0
    while 1:
        i += 1
        try:
            cp_rank = int(td_tags[7*(i-1)].string)
        except ValueError:
            break
        if cp_rank != i:
            break
    return i-1

poke_num = last_specify()

poke_names = [0]*poke_num
Race_Vals = [[0]*3 for _ in range(poke_num)]

for i in range(poke_num):
    poke_names[i] = str(td_tags[7*i+1].string)
    Race_Vals[i] = [int(race_val.string) for race_val in td_tags[7*i+2:7*i+5]]

columns = ["HP","ATK","DEF"]
index = poke_names

df = pd.DataFrame(Race_Vals,columns=columns,index=index)

df.to_pickle(r"C:\Users\ktmks\programming\GUI_app\Data\race_values.pkl")






