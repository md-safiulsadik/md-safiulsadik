import requests
import random
import re

# Dictionary of total ayahs per surah (1-based index)
ayah_counts = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75, 9: 129, 10: 109,
    11: 123, 12: 111, 13: 43, 14: 52, 15: 99, 16: 128, 17: 111, 18: 110, 19: 98, 20: 135,
    21: 112, 22: 78, 23: 118, 24: 64, 25: 77, 26: 227, 27: 93, 28: 88, 29: 69, 30: 60,
    31: 34, 32: 30, 33: 73, 34: 54, 35: 45, 36: 83, 37: 182, 38: 88, 39: 75, 40: 85,
    41: 54, 42: 53, 43: 89, 44: 59, 45: 37, 46: 35, 47: 38, 48: 29, 49: 18, 50: 45,
    51: 60, 52: 49, 53: 62, 54: 55, 55: 78, 56: 96, 57: 29, 58: 22, 59: 24, 60: 13,
    61: 14, 62: 11, 63: 11, 64: 18, 65: 12, 66: 12, 67: 30, 68: 52, 69: 52, 70: 44,
    71: 28, 72: 28, 73: 20, 74: 56, 75: 40, 76: 31, 77: 50, 78: 40, 79: 46, 80: 42,
    81: 29, 82: 19, 83: 36, 84: 25, 85: 22, 86: 17, 87: 19, 88: 26, 89: 30, 90: 20,
    91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19, 97: 5, 98: 8, 99: 8, 100: 11,
    101: 11, 102: 8, 103: 3, 104: 9, 105: 5, 106: 4, 107: 7, 108: 3, 109: 6, 110: 3,
    111: 5, 112: 4, 113: 5, 114: 6
}

def get_random_verse():
    surah = random.randint(1, 114)
    ayah = random.randint(1, ayah_counts[surah])
    api_url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        verse = data['data']['text']
        surah_name = data['data']['surah']['englishName']
        ayah_number = data['data']['numberInSurah']
        return f"> 📖 *{verse}* — **{surah_name} ({surah}:{ayah_number})**"
    except Exception as e:
        print(f"Error fetching verse: {e}")
        return "> 📖 Could not fetch verse at this time. — ****"

def update_readme():
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    verse_text = get_random_verse()
    updated_content = re.sub(
        r"(<!-- quran-verse-start -->)(.*?)(<!-- quran-verse-end -->)",
        rf"\1\n{verse_text}\n\3",
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(updated_content)
    print("✅ README updated with new verse.")

if __name__ == "__main__":
    update_readme()
