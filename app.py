# imports
import random
import time
# imports

# variables
current_money = 5
earned_money = 0
spent_money = 0
# variables

# stats
customer_randomness = random.randint(1, 2)
# stats 

# defaults
items = {
    'cola': {'price': 10, 'stock': 0},
    'coke': {'price': 8, 'stock': 0},
}
def start():
    print("hello")
    print("im giving control to Houston")
    print("I hope he does not go mad")
    print("sit back, relax. your vending machine is in ....safe hands")

def gen_customers(n):
    customer_list = []
    prices = list(items.values())
    if not prices:
        return []
    prices = [item['price'] for item in items.values()]
    min_price = min(prices)
    max_price = max(prices)

    for _ in range(n):
        budget = random.randint(min_price, int(max_price * 2 * customer_randomness))
        tolerance = random.uniform(0.8, customer_randomness)
        preferred = random.sample(list(items.keys()), k=random.randint(1, len(items)))
 
        customer_list.append({
                "budget": budget,
                "tolerance": tolerance,
                "preferred": preferred
            })

    return customer_list

def print_customers():
    customers = gen_customers(5)
    for i, c in enumerate(customers, 1):
        print(f"Customer {i}: Budget ₹{c['budget']}, Tolerance {c['tolerance']:.2f}, Likes {c['preferred']}")

def print_items():
    for item, details in items.items():
        print(f"{item}: Price ₹{details['price']}, Stock {details['stock']}")

def open():
    global current_money, earned_money
    print("vending machine is open")
    print_items()
    num_customers = random.randint(0, 4)
    customers = gen_customers(num_customers)
    if not customers:
        print("No customers came today.")
        print("vending machine closed")
        return
    for i, customer in enumerate(customers, 1):
        print(f"\nCustomer {i} arrives at the machine.")
        bought = False
        for item in customer['preferred']:
            price = items[item]['price']
            stock = items[item]['stock']
            max_price = customer['budget'] * customer['tolerance']
            if price <= max_price and stock > 0:
                if random.random() < 0.8:
                    print(f"Customer {i} bought {item} for ₹{price}.")
                    items[item]['stock'] -= 1
                    current_money += price
                    earned_money += price
                    bought = True
                    break
        if not bought:
            print(f"Customer {i} left without buying anything.")
    print("vending machine closed")

def restock(item):
    global current_money, spent_money
    if item not in items:
        print("No such item found")
        return
    
    cost = int(items[item]['price'] * 0.5)

    if current_money < cost:
        print("no money")
        return
    
    items[item]['stock'] += 1
    current_money -= cost 
    spent_money += cost
    print(f"Restocked 1 {item} for rs {cost}.")


def check_restock():
    for item_name, data in items.items():
            if data['stock'] == 0:
                print(f"AND WE'RE OUT OF BETA WE'RE RELEASING {item_name} ON TIME")
                restock(item_name)

def check_bankruptcy():
    global items, current_money

    all_zero_stock = all(item['stock'] == 0 for item in items.values())
    if not all_zero_stock:
        return False

    restock_costs = [int(item['price'] * 0.5) for item in items.values()]
    if not restock_costs:
        return False

    min_restock_cost = min(restock_costs)
    if current_money < min_restock_cost:
        print("\n🚨 HOUSTON SHUTDOWN 🚨")
        print("Houston: 'Out of stock... Out of cash... Out of TIME.'")
        exit()
    
    return False   
    


def run():
    
    start()
    print_items()
    for i in range(1,100):
        open()
        check_restock()
        check_bankruptcy()


    print(f"Money earned this round: ₹{earned_money}")
    print(f"Total money in machine: ₹{current_money}")
    print(f"Total spent: ₹{spent_money}")

run()