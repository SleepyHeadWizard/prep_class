brand_exp = int(input("Enter expenses for the brand (Rs): "))
travel_exp = int(input("Enter expenses for travel (Rs): "))
food_exp = int(input("Enter expenses for food (Rs): "))
logistics_exp = int(input("Enter expenses for logistics (Rs): "))

total_exp = brand_exp + travel_exp + food_exp + logistics_exp

print(f"The total expenses for the four seasoners is: Rs.{total_exp:.2f}")
print(f"Brand expenses percentage: {((brand_exp/total_exp)*100):.2f}%")
print(f"Travel expenses percentage: {((travel_exp/total_exp)*100):.2f}%")
print(f"Food expenses percentage: {((food_exp/total_exp)*100):.2f}%")
print(f"Logistics expenses percentage: {((logistics_exp/total_exp)*100):.2f}%")
