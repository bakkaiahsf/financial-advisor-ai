import yfinance as yf

def get_stock_data(stock_code):
    stock = yf.Ticker(stock_code)
    data = stock.history(period="1mo")  # Fetch last 1 month of stock data
    return data

if __name__ == "__main__":
    stock_code = "TCS.NS"  # Replace with any Indian stock code
    print(get_stock_data(stock_code))