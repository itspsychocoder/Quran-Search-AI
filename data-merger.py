import json
import os

# Assuming all files are in a directory named 'surah_files'
surah_directory = './dat/individual'
merged_data = []

# Read each surah file and append the data to merged_data
for file_name in os.listdir(surah_directory):
    if file_name.endswith('.json'):  # Assuming the files are in JSON format
        file_path = os.path.join(surah_directory, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            surah_data = json.load(file)
            merged_data.append(surah_data)

# Save merged data to a new file
with open('./data/merged_surah_data.json', 'w', encoding='utf-8') as merged_file:
    json.dump(merged_data, merged_file, ensure_ascii=False, indent=4)

print("Data merged and saved successfully!")
