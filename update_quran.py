import requests
import random
import re

# Fetch random verse from the Quran API
surah = random.randint(1, 114)
ayah = random.randint(1, 286)
response = requests.get(f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad")

if response.status_code == 200:
    data = response.json()
    verse = data['data']['text']
    ref = f"{data['data']['surah']['englishName']} ({surah}:{ayah})"
else:
    verse = "Could not fetch verse at this time."
    ref = ""

# Read the current README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the section between the markers
pattern = r"<!-- quran-verse-start -->(.*?)<!-- quran-verse-end -->"
replacement = f"<!-- quran-verse-start -->\n> 📖 *{verse}* — **{ref}**\n<!-- quran-verse-end -->"
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the updated content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
