import json

def save_to_json(data, filename="user_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"💾 Data saved successfully to {filename}")
