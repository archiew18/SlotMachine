import random

symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

winner = False
while winner != True:
  results = random.choices(symbols, k=3)
  print(f"{results[0]}|{results[1]}|{results[2]}")
  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
      print("Jackpot! 💰")
      winner = True
  else:
   print("Thanks for playing!")
