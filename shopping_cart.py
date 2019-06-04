class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None, total=0, items=[]):
        self.employee_discount = emp_discount
        self.total = total
        self.items = items
       
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
       
    def mean_item_price(self):
        mean = self.total/len(self.items)
        return mean

    def median_item_price(self):    
        prices = [item["price"] for item in self.items]       
        length = len(prices)
        if (length%2 == 0):
            a = int(length/2)
            b = mid_one - 1
            median = (prices[a] + prices[b])/2
            return median
        else:
            c = int(length/2)
            return prices[c]

    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount/100
            disc_total = self.total * discount
            real_total = self.total - disc_total
            return real_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
    

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']