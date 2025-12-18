import requests
from bs4 import BeautifulSoup
import csv

URL = "https://github.com"
CSV_FILE = "data.csv"

def scrape_data():
    response = requests.get(URL)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage.")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find("h2")

    if not headlines:
        print("No headlines found on the webpage.")
        return
    
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(["ID", "Headline"])

        for index, headline in enumerate(headlines, start = 1):
            write.writerow([index, headline.get_text(strip = True)])
    print(f"Data successfully written to {CSV_FILE}")


if __name__ == "__main__":
    scrape_data()


