brand_exp = int(input("Enter the total expenses for the brand: "))
travel_exp = int(input("Enter the total expenses for travel: "))
food_exp = int(input("Enter the total expenses for food: "))
logistics_exp = int(input("Enter the total expenses for logistics: "))

total_exp = brand_exp + travel_exp + food_exp + logistics_exp

print(f"The total expenses for the four seasoners is: {total_exp}")
print(f"Brand expenses percentage: {round((brand_exp/total_exp)*100, 2)*100}%")
print(f"Travel expenses percentage: {round((travel_exp/total_exp)*100, 2)*100}%")
print(f"Food expenses percentage: {round((food_exp/total_exp)*100, 2)*100}%")
print(f"Logistics expenses percentage: {round((logistics_exp/total_exp)*100, 2)*100}%")

