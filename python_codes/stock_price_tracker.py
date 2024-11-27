import requests
from tkinter import Tk, Label, Entry, Button, Text, messagebox
from bs4 import BeautifulSoup

# Function to fetch stock price from Google Finance
def get_stock_price():
    stock_symbol = entry_stock_symbol.get().upper()

    if not stock_symbol:
        messagebox.showerror("Input Error", "Please enter a stock symbol.")
        return

    try:
        # URL for the Google Finance stock page
        url = f"https://www.google.com/finance/quote/{stock_symbol}:NSE?sa=X&ved=2ahUKEwiA4d-67dfzAhXg-ysKHREcBYIQ3ecFegQINBAY"

        # Headers to mimic a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "Host": "www.google.com",
            "DNT": "1",
            "TE": "Trailers",
            "Pragma": "no-cache"
        }

        # Send GET request to fetch the page
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            
            price_div = soup.find('div', {'class': 'YMlKec fxKbKc'})  # This class may change, check the page source for the correct one

            if price_div:
                stock_price = price_div.text.strip()
                text_result.config(state="normal")  # Enable text box for editing
                text_result.delete("1.0", "end")  # Clear previous result
                text_result.insert("end", f"Stock Name: {stock_symbol}\nStock Price: ₹{stock_price}")
                text_result.config(state="disabled")  # Disable text box to prevent editing
            else:
                messagebox.showerror("Error", "Could not retrieve stock price.")
        else:
            messagebox.showerror("Error", f"Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch stock data: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#  Tkinter GUI window
root = Tk()
root.title("Stock Price Fetcher")
Label(root, text="Enter Stock Symbol (e.g., RELIANCE):").grid(row=0, column=0, padx=10, pady=5)
entry_stock_symbol = Entry(root, width=30)
entry_stock_symbol.grid(row=0, column=1, padx=10, pady=5)
btn_fetch = Button(root, text="Fetch Stock Price", command=get_stock_price)
btn_fetch.grid(row=1, column=0, columnspan=2, pady=10)
text_result = Text(root, height=5, width=50, wrap="word", state="disabled")
text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
