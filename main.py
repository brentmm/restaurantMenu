menuItems = ["Bresaola and tuna pasta","Mangosteen and ezekiel salad","Egg and bacon soup","Italian sausage and sweet dessert wine salad","Lamb and plantain vindaloo","Chickpea and celery soup","Mandarine and cauliflower salad","Bresaola and opossum salad","Mangetout and jalape stir fry","Raspberry and haroset salad"]
menuDescriptions = ["Fresh egg pasta in a sauce made from bresaola and tuna","A crisp salad featuring fresh mangosteen and ezekiel","Free range eggs and streaky bacon combined into creamy soup","A crisp salad featuring italian sausage and sweet dessert wine","Spicy vindaloo made with succulent lamb and fresh plantain","Fresh chickpea and celery combined into creamy soup","A crisp salad featuring fresh mandarine and cauliflower","A crisp salad featuring bresaola and opossum","Crunchy stir fry featuring fresh mangetout and jalape","Salad with raspberries and herosets"]
glutenFriendly = [False,True,False,False,False,False,True,True,False,True]
menuPrices = ["10.99","12.99","6.99","8.25","5.99","13.50","4.30","5.20","14.60","100.29"]

for i in range(0, 10):
  print("Item: '" + menuItems[i] + "'")
  print("Description: '" + menuDescriptions[i] + "'")
  print("Gluten Friendly: " + str(glutenFriendly[i]))
  print("Price: $" + str(menuPrices[i]))
  print(" ")

