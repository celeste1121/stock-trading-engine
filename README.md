# Stock Trading Engine

## Overview
This program implements a real-time stock trading engine that matches buy and sell orders based on given constraints. It supports up to 1,024 stock tickers and handles multi-threaded order execution efficiently without using dictionaries, maps, or equivalent data structures.

## Features
- **Add orders** (`add_order` function): Supports both buy and sell orders.
- **Order Matching** (`match_order` function): Executes trades when a buy order meets or exceeds the lowest sell price.
- **Lock-free multi-threading**: Ensures safe concurrent execution.
- **Random order simulation**: Generates and processes random trades.

## Requirements
- Python 3.x

## How to Run
1. Clone the repository or download the script.
2. Run the following command in the terminal:
   ```bash
   python stock_trading_engine.py
   ```
3. The system will simulate real-time stock trading and print executed trades.

## Example Output
```
EXECUTED TRADE: Ticker: MSFT | Quantity: 50 | Price: $132
EXECUTED TRADE: Ticker: AAPL | Quantity: 30 | Price: $250
```

## Notes
- The program is optimized for O(n) order matching.
- Uses **priority queues** for fast order processing.
- Fully adheres to problem constraints (no dictionary/map usage).

## Author
Celeste Chen

