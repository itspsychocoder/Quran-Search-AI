import requests
import json
def get_data_from_api(endpoint_url):
    try:
        response = requests.get(endpoint_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


surah = 1


for i in range(76, 115):
    api_endpoint = f"https://api.alquran.cloud/v1/surah/{i}"
    tasfir_endpoint = f"https://cdn.jsdelivr.net/gh/spa5k/tafsir_api@main/tafsir/en-tafisr-ibn-kathir/{i}.json"

    data = get_data_from_api(api_endpoint)
    if data:
        # print(data["data"]["ayahs"])
        pass
    ayat_data = data["data"]["ayahs"]
        
    tafsir_raw_data = get_data_from_api(tasfir_endpoint)
    if tafsir_raw_data:
        pass
        # print(tafsir_raw_data["ayahs"])
    else:
        print("No data found")
    tafsir_data = tafsir_raw_data["ayahs"]
    tafsir_data.sort(key=lambda x: x["ayah"])
    # print(tafsir_data)
    # print(len(ayat_data))


    merged_array = []
    if ayat_data is not None and tafsir_data is not None:
        for obj1, obj2 in zip(ayat_data, tafsir_data):
            obj2_renamed = {**obj2, 'tafsir_text': obj2['text']}  # Rename 'text' to 'tafsir_text'
            del obj2_renamed['text']  # Remove the original 'text' key if it's present
            # Merge the objects
            merged_obj = {**obj1, **obj2_renamed}
            merged_array.append(merged_obj)
    else:
        print("Error: One of the lists is None.")
    # Save the merged array to a JSON file
    file_path = f"./surah-{i}.json"

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(merged_array, json_file, ensure_ascii=False, indent=4)


    print(f"Surah {i} saved at {file_path}\n\n")


        