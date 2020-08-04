import pandas as pd

class pokemon():
    def __init__(self,poke_name):
        #!!各値はデータベースから引っ張ってくる
        self.A = 263
        self.D = 198
        self.H = 209
        #!!ポケモンレベルと各個体値は入力から持ってくる
        self.PL = 36
        self.Aiv = 15
        self.Div = 15
        self.Hiv = 15
    def CP(self):
        #!!self.cprはCP補正値
        self.cpr = 0.5888984165
        return int((self.A+self.Aiv)*(self.D+self.Div)**0.5*(self.H+self.Hiv)**0.5*self.cpr/10)


df = pd.read_pickle(r"C:\Users\ktmks\programming\GUI_app\Data\race_values.pkl")




if __name__ == "__main__":
    kairyu = pokemon("kairyu")
    print(kairyu.CP())
