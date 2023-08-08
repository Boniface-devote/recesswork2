import requests
import csv
import json
from bs4 import BeautifulSoup

# Function to extract bird species from the website


def extract_bird_species():
    # Replace with the website URL containing bird species data
    url = 'https://xeno-canto.org/collection/species/latest'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Implement web scraping logic here to extract bird species
        species_list = soup.find_all('table', class_='results')
        species_data = []
        for species_table in species_list:
            common_names = species_table.find_all(
                'span', class_='common-name')
            sci_names = species_table.find_all(
                'span', class_='sci-name')
            for common_name, sci_name in zip(common_names, sci_names):
                species_data.append(
                    {'name': common_name.text.strip(), 'scientific': sci_name.text.strip()})
        return species_data
    else:
        print('Failed to fetch data from the website.')
        return []

# Function to generate CSV file


def generate_csv(data):
    csv_filename = 'Birds.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'scientific']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to generate JSON file


def generate_json(data):
    json_filename = 'Birds.json'
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    bird_species_data = extract_bird_species()
    if bird_species_data:
        generate_csv(bird_species_data)
        generate_json(bird_species_data)
        print('CSV and JSON files generated successfully.')
