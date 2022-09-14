bitcoin_price = int(input("What is Bitcoin price today?\n"))
dollars = int(input("How much $ do you have?\n"))
print(f"You can buy {dollars / bitcoin_price:.8f} BTC")