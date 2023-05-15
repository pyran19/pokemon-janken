import random

reward=0.01
p=0.5  #相手視点で見た時にサイコショックを持っている確率

class Pokemon():
    moves={"技名":"確率"}
    def __init__(self,name,moves):
        self.name=name
        self.moves=moves
    #勝った時はその時選択した技をより選びやすくするように確率を更新
    def probUpdate(self,move,result):
        #result  win:1 lose:-1
        self.moves[move] = min(1,self.moves[move]+reward*result)
        total=sum(self.moves.values())
        for m in self.moves:
            self.moves[m] /= total
    #乱数で技を選択
    def selectMove(self):
        rp=random.random()
        for m in self.moves:
            if self.moves[m]>rp:
                return m
            else:
                rp -= self.moves[m]
#勝敗を計算
def battle(you,enemy):
    if you == "サイコショック" and enemy =="交代":
        return -1
    elif you == "ムーンフォース" and enemy =="交代":
        return 1
    elif you == "サイコショック" and enemy =="居座り":
        return 1
    elif you == "ムーンフォース" and enemy =="居座り":
        return -1
    else:
        print("error. 想定していないパターンです。どっかバグってる")

#ポケモン毎に持ってる技＆確率の初期値の設定
clodsire=Pokemon("ドオー",{"交代":0.5,"居座り":0.5})
fluttermane=Pokemon("ショック無ハバカミ",{"ムーンフォース":1.})
fluttershock=Pokemon("ショック有ハバカミ",{"サイコショック":0.7,"ムーンフォース":0.3})


def match():
    #使用するポケモンを選択
    rp=random.random()
    if(rp < p):
        you=fluttershock
    else:
        you=fluttermane
    enemy=clodsire
    
    #出す技を乱数で決める
    youMove=you.selectMove()
    enemyMove=enemy.selectMove()
    
    #勝敗を計算
    result=battle(youMove,enemyMove)

    #勝敗に応じて確率を更新
    you.probUpdate(youMove,result)
    enemy.probUpdate(enemyMove,-result)

for i in range(1000):
    match()

print("カミ:   ",fluttershock.moves)
print("ドオー: ",clodsire.moves)
