def get_recipe_price(prices, optionals=None, **ingredients):

    if optionals is None:
        optionals = []
    sum = 0
    if len (prices) == 0:
        return sum

    for ingredient, amount in ingredients.items():
        if ingredient in optionals:
            continue
        sum += prices[ingredient]*(amount//100)
    return sum

if __name__ == "__main__":
    print (get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print (get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print (get_recipe_price({}))