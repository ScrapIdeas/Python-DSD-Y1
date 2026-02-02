weeklypoints = 0
steps = 0
water_ml = 0
tiers = ("Bronze", "Silver", "Gold")
def weeklytier():
    steps = int(input("What are your steps?"))
    water_ml = int(input("What is your water intake?"))
    weeklypoints = (steps // 1000) *2 + (water_ml // 500)
    if(0 <= weeklypoints <= 19):
        print(f"You belong in the {tiers[0]} Tier!")
    elif(20 <= weeklypoints <= 39):
        print(f"You belong in the {tiers[1]} Tier!")
    elif(weeklypoints >= 40):
        print(f"You belong in the {tiers[2]} Tier")

weeklytier()
