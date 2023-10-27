
import os
import random

def read():
    names=[]
    word_number=random.randint(1,171)
    with open("data.txt", "r", encoding="utf-8") as f:
        for line  in f:
            names.append(line)
    game_word=names[word_number]
    game_word = game_word.strip('\n')
    rep = {
        ord('á'): 'a',
        ord('é'): 'e',
        ord('í'): 'i',
        ord('ó'): 'o',
        ord('ú'): 'u',
    }
    game_word = game_word.translate(rep)
    return game_word
       
def empty_line(game_word):
    word_len = len(game_word)
    
    space_line=""
    
    for i in range(0,word_len):
        space_line=space_line  + "_"
    
    return space_line,game_word,word_len

def run():
    
    exit = 's'


    while exit == 's':
        os.system("clear")
        space_line, game_word, word_len = empty_line(read())
        usr_word_list = [i for i in space_line]
        usr_word = ""
        count = 0
        dead_count = 0
        
        


        while usr_word != game_word:
            print("""
                 _    _                                         
                | |  | |                                        
                | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
                |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                | |  | | (_| | | | | (_| | | | | | | (_| | | | |
                |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                     __/ |                      
                                    |___/                       
            
            
            
            
            
            """)
            if dead_count ==1:
                print("""
                ||
                ||                        
                ||                        
                ||                        
                ||                               
                ||                             
                ||                                 
                ||                              
                ||                                       
                ||                                       
                ||                                     
                ||                                        
                ||                            
                ||                                          
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==2:
                print("""
                __________________________________________
                __________________________________________
                ||                        
                ||                        
                ||                        
                ||                               
                ||                             
                ||                                 
                ||                              
                ||                                       
                ||                                       
                ||                                     
                ||                                        
                ||                            
                ||                                          
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==3:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                               
                ||                             
                ||                                 
                ||                              
                ||                                       
                ||                                       
                ||                                     
                ||                                        
                ||                            
                ||                                          
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==4:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                                       
                ||                                       
                ||                                     
                ||                                        
                ||                            
                ||                                          
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==5:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                         |              
                ||                         |               
                ||                         |            
                ||                         |               
                ||                         |   
                ||                         |                 
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==6:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                         |              
                ||                        /|               
                ||                       / |            
                ||                      /  |               
                ||                         |   
                ||                         |                 
                ||                                        
                ||                         
                ||                                      
                """)
            if dead_count ==7:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                         |              
                ||                        /|\               
                ||                       / | \           
                ||                      /  |  \             
                ||                         |   
                ||                         |                 
                ||                                        
                ||                               
                ||                     
                """)
            if dead_count ==8:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                         |              
                ||                        /|\               
                ||                       / | \           
                ||                      /  |  \             
                ||                         |   
                ||                         |                 
                ||                        /                 
                ||                       /           
                ||                      /                      
                """)
            if dead_count == 9:
                print("""
                __________________________________________
                __________________________________________
                ||                        |
                ||                        |
                ||                        |
                ||                      /─────\           
                ||                     /  × ×  \        
                ||                     \   _   /            
                ||                      \_____/        
                ||                         |              
                ||                        /|\               
                ||                       / | \           
                ||                      /  |  \             
                ||                         |   
                ||                         |                 
                ||                        / \                
                ||                       /   \        
                ||                      /     \                 
                """) 
                print("La palabra era: " + game_word)
                break
            if count > 0:
                print("".join(usr_word_list))
            else:
                print(space_line)

            if "".join(usr_word_list) == game_word:
                break

            letter = input("Escriba una letra: ")
            
            
            if letter in game_word:
                for i in range(0,word_len):
                    if letter == game_word[i]:

                        usr_word_list[i] = letter
            else:
                dead_count +=1
            
            os.system("clear")
            count += 1
        exit= input("Desea continuar? s/n: ")
        os.system("clear")
       








if __name__=='__main__':
    run()
