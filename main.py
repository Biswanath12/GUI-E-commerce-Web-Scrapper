import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import pandas as pd


def web_scraper(links, output_text):
    data_list = []

    for index, link in enumerate(links, start=1):
        try:
            # Send a GET request to the link
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/122.0.0.0 Safari/537.36'
            }
            response = requests.get(link, headers=headers)
            response.raise_for_status()  # Raise an exception for bad requests

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the HTML snippet
            product_data = extract_product_data(soup)

            # Display the extracted data in the output_text widget
            display_data(output_text, index, product_data)

            # Append the data to the list for Excel file
            data_list.append({
                'Link': link,
                'Product': product_data['Title'],
                'Reviews': product_data['Reviews'],
                'Price': product_data['Price']
            })
        except requests.exceptions.RequestException as e:
            output_text.insert(tk.END, f"Error processing Link {index}: {str(e)}\n")

    # Write the data to an Excel file
    write_to_excel(data_list)


def extract_product_data(soup):
    # Extract product data based on the updated HTML structures
    product_title_element = soup.find('span', {'id': 'productTitle'})
    product_reviews_element = soup.find('span',
                                        {'id': 'acrPopover', 'class': 'reviewCountTextLinkedHistogram noUnderline'})
    product_price_element = soup.find('span', {'class': 'aok-offscreen'})

    # Debugging: Print the entire HTML content of the page
    print("\n--- Entire HTML Content ---\n")
    print(soup.prettify())

    # Check if the elements are found before accessing their text attribute
    product_title = product_title_element.text.strip() if product_title_element else "Title Not Found"

    # Extracting the review text from the title attribute of the span tag
    product_reviews = product_reviews_element.get('title').strip() if product_reviews_element else "Reviews Not Found"

    # Extracting the price text
    product_price = product_price_element.text.strip() if product_price_element else "Price Not Found"

    return {'Title': product_title, 'Reviews': product_reviews, 'Price': product_price}


def display_data(output_text, index, product_data):
    # Display the extracted data in the output_text widget
    output_text.insert(tk.END, f"\nExtracted Data for Link {index}:\n")
    for key, value in product_data.items():
        output_text.insert(tk.END, f"{key}: {value}\n")


def write_to_excel(data_list):
    # Write the data to an Excel file
    output_file_path = "scraped_data.xlsx"
    df = pd.DataFrame(data_list)
    df.to_excel(output_file_path, index=False)
    print(f"Data written to {output_file_path}")


def on_scrape_button_click():
    # Get user input for links
    links_input = link_entry.get("1.0", tk.END)
    links = [link.strip() for link in links_input.split('\n') if link.strip()]

    # Clear the output_text widget before scraping new data
    output_text.delete(1.0, tk.END)

    # Call the web_scraper function with the user-input data
    web_scraper(links, output_text)


# Create the main Tkinter window
root = tk.Tk()
root.title("Web Scraper")

# Create and place widgets in the window
link_label = ttk.Label(root, text="Enter Links (one per line):")
link_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

link_entry = tk.Text(root, wrap=tk.WORD, width=40, height=5)
link_entry.grid(row=0, column=1, padx=10, pady=10)

scrape_button = ttk.Button(root, text="Scrape", command=on_scrape_button_click)
scrape_button.grid(row=1, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, wrap=tk.WORD, width=60, height=15)
output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
