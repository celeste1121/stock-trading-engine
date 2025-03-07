# Author: Celeste Chen
import threading
import random
import time
import queue

class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

# OrderBook manages buy and sell orders for stocks and handles matching trades
class OrderBook:
    def __init__(self):
        self.buy_orders = queue.PriorityQueue()  # Max-Heap (negative price for highest priority)
        self.sell_orders = queue.PriorityQueue()  # Min-Heap (natural order for lowest priority)
        
    # Adds a new buy or sell order to the order book and attempts to match it with existing orders
    def add_order(self, order_type, ticker, quantity, price):
        new_order = Order(order_type, ticker, quantity, price)
        
        if order_type == "Buy":
            self.buy_orders.put((-price, new_order))  # Use negative price for max heap behavior
        else:
            self.sell_orders.put((price, new_order))  # Min heap keeps lowest price at top
        
        self.match_order()
    
    # Matches buy and sell orders if conditions are met (buy price >= lowest sell price)
    def match_order(self):
        while not self.buy_orders.empty() and not self.sell_orders.empty():
            buy_price, buy_order = self.buy_orders.queue[0]
            sell_price, sell_order = self.sell_orders.queue[0]
            
            if -buy_price >= sell_price:  # Match condition
                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                print(f"EXECUTED TRADE: Ticker: {buy_order.ticker} | Quantity: {trade_quantity} | Price: ${sell_price}")
                
                buy_order.quantity -= trade_quantity
                sell_order.quantity -= trade_quantity
                
                if buy_order.quantity == 0:
                    self.buy_orders.get()  # Remove fully matched Buy order
                if sell_order.quantity == 0:
                    self.sell_orders.get()  # Remove fully matched Sell order
            else:
                break

# Simulating Stock Transactions
def simulate_trading(order_book, num_orders=50):
    tickers = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"]
    order_types = ["Buy", "Sell"]
    
    for _ in range(num_orders):
        order_type = random.choice(order_types)
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = random.randint(100, 500)
        
        threading.Thread(target=order_book.add_order, args=(order_type, ticker, quantity, price)).start()
        time.sleep(random.uniform(0.01, 0.1))

if __name__ == "__main__":
    order_book = OrderBook()
    simulate_trading(order_book)
