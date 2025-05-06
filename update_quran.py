import requests
import random
import re

# Fetch random verse
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

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Update only the verse section
new_verse_block = f"<!-- quran-verse-start -->\n> 📖 *{verse}* — **{ref}**\n<!-- quran-verse-end -->"
updated_content = re.sub(
    r"<!-- quran-verse-start -->(.*?)<!-- quran-verse-end -->",
    new_verse_block,
    content,
    flags=re.DOTALL,
)

# Write back
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_content)
