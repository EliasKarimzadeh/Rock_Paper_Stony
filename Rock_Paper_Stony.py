""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    | $  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @                      ELIAS KARIMZADEH                            @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @              GitHub: github.com/EliasKarimzadeh                  @ \ $ |
    | $ \ @             Linkdin: in/elias-karimzadeh-a7a9b8283               @ / $ |
    | $ / @            Instagram : instagram.com/elyaskarymzade              @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |        
    | $ \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ $ |
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|"""

                                                                                                                                                
import random

time = 0
time_user = 0
time_AI = 0
tio = 0

chooses = ['R' , 'S' , 'P']
print('Hello\nWelcom to Applecation Game_IRANY')

while True:
    user_choise = input("""Please choose of the following
                        \nRock with a name R _ Paper with the name P _ Scissor with the name S :""")
    AI_choose = random.choice(chooses)
    if user_choise in chooses:
        if user_choise == AI_choose :
            print("Tie")
            tio += 1    
        elif (user_choise == 'P' and AI_choose == 'R') or (user_choise == 'S' and AI_choose == 'P') or (user_choise == 'R' and AI_choose == 'S') :
            print('you Won :))) ')
            time_user += 1      
        else :
            print('you Lost :((( ')
            time_AI += 1       
        time += 1       
        choose_mining = {
                        'R' : 'Rock',
                        'S' : 'Scissos',
                        'P' : 'Paper'
                        }   
        print(f'you Choose {choose_mining[user_choise]} and PC choose {choose_mining[AI_choose]}')       
    else :
        print("please choose of the following") 
    if time > 4:
        break
    
if time_user > time_AI :
    result = 'You Won :))'
    
elif time_user < time_AI :
    result = 'PC Won :(('
    
else :
    result = 'Tio' 
    
print(f'''Overall result of the Game : {result}
       Your win Count : {time_user}
       PC win Count : {time_AI}
       Tio : {tio}''')
