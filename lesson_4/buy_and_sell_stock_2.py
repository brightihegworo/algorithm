
def buy_and_sell_stocks(prices):
    maximum = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            maximum = maximum + prices[i + 1] - prices[i]

    return maximum

test_prices = [7, 1, 5, 3, 6, 4]
test_result = buy_and_sell_stocks(test_prices)
print(test_result)