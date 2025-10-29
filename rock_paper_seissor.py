import random


def WhoPlay(func):
    def wrapper(*args, **kwargs):
        name = input('Enter your name: ')
        psk = input('Enter your passcode: ')
        if psk != "12345687":
            print('wrong passcode!')
            quit()
        func(*args, **kwargs)
    return wrapper


def rps(name: str):
  u: int = 0
  b: int = 0
  user: str = input("[R]ock, [P]aper, [S]cissor: ").lower()
  bot: str = random.choice(["R", "P", "S"]).lower()
  print(f"{user} vs {bot}")
  
  if user in ['r', 'p', 's']:
    if (user == "r" and bot == "s") or (user == "s" and bot == "p") or (user == "p" and bot == "r"):
       print(f"{name} win!")
       u += 5
    elif user == bot: 
       print("draw")
    else:
       print("bot win!")
       b += 5 
  else: 
    print("invalid input!")
   
  return u, b

@WhoPlay
def main():
  user_point: int = 0
  bot_point: int = 0
  
  user_name: str = input("User name: ")
  user_wish: int = int(input("Repeat: "))
  
  for _ in range(user_wish):
    user_pt, bot_pt = rps(user_name)
    user_point += user_pt
    bot_point += bot_pt
  print(f"{user_name} got {user_point} points")
  print(f"bot got {bot_point} points")
    


if __name__ == "__ main__":
   main()
main()
