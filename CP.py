import pandas as pd
from collections import defaultdict

class pokemon():
    def __init__(self,poke_name,Aiv,Div,Hiv,PL):
        #各値はファイルから引っ張ってくる
        self.A = df.loc[poke_name,"ATK"]
        self.D = df.loc[poke_name,"DEF"]
        self.H = df.loc[poke_name,"HP"]
        #!!ポケモンレベルと各個体値は入力から持ってくる
        self.PL = PL
        self.Aiv = Aiv
        self.Div = Div
        self.Hiv = Hiv
    def CP(self):
        #!!self.cprはCP補正値
        self.cpr = cprs[self.PL]
        return int((self.A+self.Aiv)*(self.D+self.Div)**0.5*(self.H+self.Hiv)**0.5*self.cpr/10)

df = pd.read_pickle(r"C:\Users\ktmks\programming\GUI_app\Data\race_values.pkl")
with open(r"C:\Users\ktmks\programming\GUI_app\Data\cpr.txt") as f:
    cprs_data = f.read().split("\n")
cprs = defaultdict(lambda:-1)
for i in range(len(cprs_data)):
    pl, r = map(float,cprs_data[i].split("\t"))
    cprs[pl] = r




if __name__ == "__main__":
    kairyu = pokemon("カイリュー",15,15,15,35.5)
    print(kairyu.CP())
