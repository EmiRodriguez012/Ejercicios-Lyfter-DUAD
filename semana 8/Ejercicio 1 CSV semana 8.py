import csv 

def get_games_number():
  games_number= int(input("Please enter de amount of games you would like to include: "))
  return games_number



def get_games(games_number):
  game_list= [ ]

  for i in range(games_number):
      print(f"Entering game number: {i+1} ")
      game = {}
      game['name']= input("Please enter the name of game:")
      game['genre']=input("Please enter the genre of game:")
      game['developer']=input("Please enter the developer:")
      game['esrb_class']=input("Please enter the ESRB classification:")

      game_list.append(game)
  return game_list

  
def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline= '') as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter= ',')
    writer.writeheader()
    writer.writerows(data)
  print ()


def main(): 
 
  game_headers = (
    'name',
    'genre',
    'developer',
    'esrb_class',
  )

  games_number= get_games_number()
  games_list= get_games(games_number)

  print(games_list)

  write_csv_file('game_list.csv', games_list, game_headers)

main()