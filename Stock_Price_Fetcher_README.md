
# Stock Price Fetcher

This is a simple Python program that fetches and displays the current stock price of a company from Google Finance. The program uses the `requests` library to fetch the stock price data, and `tkinter` for the graphical user interface (GUI). The stock symbol for companies listed on the National Stock Exchange (NSE) of India can be entered, and the current stock price will be displayed.

## Features

- Fetches stock price for a given stock symbol.
- Simple and intuitive graphical user interface (GUI) using Tkinter.
- Displays stock name and price.
- Handles errors gracefully with error messages.

## Requirements

- Python 3.x
- `requests` library: Install via `pip install requests`
- `beautifulsoup4` library: Install via `pip install beautifulsoup4`

## How to Use

1. Clone or download the repository.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the script:
   ```bash
   python stock_price_fetcher.py
   ```
4. Enter the stock symbol (e.g., `RELIANCE`) and click **Fetch Stock Price**.
5. The stock price will be displayed in the text box.

## Example

- Enter stock symbol: `RELIANCE`
- Output: 
   ```text
   Stock Name: RELIANCE
   Stock Price: ₹2,400.45
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, make improvements, or submit issues or pull requests.
