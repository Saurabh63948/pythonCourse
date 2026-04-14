tea_prices_inr = {
    "masala chai": 400,
    "green chai": 500,
    "lemon tea": 600
}


new_price = {tea:price / 93 for tea, price in tea_prices_inr.items()}

print(new_price)