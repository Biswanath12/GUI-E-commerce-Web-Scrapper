
# E-commerce GUI Web Scraper

This web scraper is a Python script with a graphical user interface (GUI) built using Tkinter. Users can input a list of website links into a text field, and upon clicking the "Scrape" button, the script sends HTTP GET requests to each provided link. It then extracts product data such as title, reviews, and price from the HTML content of the pages using BeautifulSoup.

The extracted data is displayed in a text widget within the GUI, and simultaneously, the script compiles this information into a Pandas DataFrame. Finally, the script writes the DataFrame to an Excel file named "scraped_data.xlsx."

In summary, the web scraper allows users to input multiple links, fetch and display product data from these links, and store the extracted information in an Excel file for further analysis.

## Authors

- [@biswanth12](https://github.com/Biswanath12)

## Features

1. **User-Friendly GUI:** The scraper includes a graphical user interface using Tkinter, making it accessible to users without requiring them to interact with the code directly.

2. **Link Input:** Users can input a list of website links into a text field, providing flexibility for scraping multiple pages.

3. **HTTP Requests:** The script uses the 'requests' library to send HTTP GET requests to each provided link, allowing it to access the HTML content of the web pages.

4. **HTML Parsing:** BeautifulSoup is employed to parse the HTML content of the pages, making it easier to navigate and extract specific elements.

5. **Data Extraction:** The scraper extracts product data, including title, reviews, and price, from the HTML content of the web pages.

6. **Data Display:** Extracted data is displayed in real-time within a Tkinter text widget in the GUI, providing users with immediate feedback on the scraping process.

7. **Error Handling:** The script incorporates error handling to manage potential issues during the HTTP request and parsing processes, displaying relevant error messages in the GUI.

8. **Data Compilation:** The extracted data is compiled into a Pandas DataFrame, facilitating further analysis and manipulation.

9. **Excel Output:** The scraper writes the compiled data to an Excel file named "scraped_data.xlsx," allowing users to store and analyze the results outside of the application.

10. **User Notifications:** The GUI informs users about the progress of the scraping process, including successful data extraction and any encountered errors.

11. **Custom User-Agent:** The scraper uses a custom User-Agent header in the HTTP requests to mimic a browser, reducing the likelihood of being blocked by websites that may check for automated requests.

12. **Debugging Information:** For troubleshooting purposes, the script includes an option to print the entire HTML content of the page being processed.

## Usage

1. **Install Required Libraries:**
   Ensure you have the required Python libraries installed. You can install them using the following commands in your terminal or command prompt:
   ```bash
   pip install requests
   pip install beautifulsoup4
   pip install pandas
  


2. **Copy the Script:**
Copy the provided Python script into a new or existing Python file (e.g., web_scraper.py).

3. **Run the Script:**
Execute the script using a Python interpreter. This can be done by navigating to the script's directory in the terminal and running:

```bash
python web_scraper.py
```
4. **GUI Interface:**
A GUI window will open with a text field for entering website links, a "Scrape" button, and an output area to display the results.

5. **Input Website Links:**
Enter the URLs of the websites you want to scrape into the text field, with one link per line.

6. **Click "Scrape":**
Click the "Scrape" button to initiate the scraping process. The script will send requests to each provided link and display the extracted data in the output area.

7. **View Extracted Data:**
The extracted product data, including title, reviews, and price, will be displayed in the GUI in real time. Any errors encountered during the process will also be shown.

8. **Check Excel Output:**
After the scraping process is complete, check the script's output in the terminal for a message indicating that the data has been written to an Excel file ("scraped_data.xlsx").

9. **Review Excel File:**
Open the generated "scraped_data.xlsx" Excel file to review and analyze the compiled data.

10. **Troubleshooting:**
If you encounter any issues during setup or usage, refer to the error messages displayed in the GUI and the debugging information provided in the script.

Note: Ensure that you have an active internet connection, as the script relies on sending HTTP requests to retrieve web page content. Additionally, be aware of website scraping policies and comply with terms of service for the websites you intend to scrape.
