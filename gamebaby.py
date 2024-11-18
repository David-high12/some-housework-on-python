import random
alice_hp=100
monster_hp=150
monster_defence=False

while True:
      
    monster_defence=False
    print("-"*30)
    print("alice当前生命值:",alice_hp)
    print("怪兽当前生命值：",monster_hp)
    print('''            [1]攻击 15血量
           [2]加生命值 40血量
        [3]逃跑 有30%成功率
         ''')
    player_operate=input("请输入你的操作:")
    player_operate=int(player_operate)
    #玩家的回合
    if player_operate==1:
        monster_hp-=15
    elif player_operate==2:
        alice_hp+=40
        if alice_hp>=100:
            alice_hp=100
    elif player_operate==3:
        if random.randint(1,9) <= 3:
            print("逃跑成功")
            break
        else:
            print("逃跑失败") 
    print("玩家回合结束后alice血量:",alice_hp)        
   
    
    #怪物回合
    mons_act = random.randint(1,2)
    print(mons_act)
    if mons_act==1:
        alice_hp-=20
    else: 
        monster_defence = True
        if player_operate==1:
            monster_hp+=7.5
    
    if  alice_hp<=0:
        print("alice 失败了")
        break
    if  monster_hp<=0:
        print("alice 胜利了")
        break   

