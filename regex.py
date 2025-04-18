import re

text = "abc\ndaef"
pattern = r'a.'
print(re.findall(pattern, text))


text = 'ab,a,abbcbb,abc'
pattern = r"ab*"
print(re.findall(pattern, text))


text = 'ab,a,abbcbb,abc'
pattern = r"ab+"
print(re.findall(pattern, text))


text = "color colour"
pattern = r"colou?r"
print(re.findall(pattern, text))

pattern = r"\d{3}"
print(re.findall(pattern, '123 45 6789'))

pattern = r'\d{2,4}'
print(re.findall(pattern, '123 45 6789 12345 6'))


# pattern = r"[apple?]"
pattern = r"\b\w*apple\w*\b"
print(re.findall(pattern, 'apple applepie cher*ry banana'))

pattern = r"[^abc]"
print(re.findall(pattern, 'apple applepie cher*ry banana'))

text = "abc 123 _ -"
print(re.findall(r"\d", text))
print(re.findall(r"\D", text))
print(re.findall(r"\w", text))
print(re.findall(r"\W", text))
print(re.findall(r"\s", text))
print(re.findall(r"\S", text))

text = 'gray, grey'
pattern = r'gr(?:a|e)y'
print(re.findall(pattern, text))

text = "cat dog mouse"
pattern = 'cat|dog'
print(re.findall(pattern, text))

text = 'Date: 2025-03-28'
pattern = r"(\d{4})-(\d{2})-(\d{2})"
find_match = re.search(pattern, text)
if find_match:
    year, month, day = find_match.groups()
    print(year)
    print(month)
    print(day)

text = 'Coord: 12.34, 56.78'
pattern = r"(\d+\.\d+),\s*(\d+\.\d+)"
find_match = re.search(pattern, text)
if find_match:
    lat, lon = find_match.groups()
    print(lat)
    print(lon)


text = "Hello Name"
pattern = r"Hello"
if re.match(pattern, text):
    print("Строка начинается с Hello")

pattern = r"Name"
print(re.sub(pattern, "Lastname", text))

pattern = r'\s'
print(re.sub(pattern, '-', text))

text = " apple , cherry; orange. banana"
pattern = r"\s*[,\.;]\s*"
print(re.split(pattern, text))

text = "Hello\nhello\nHELLO"
pattern = r'hello'
print(re.findall(pattern, text, flags=re.IGNORECASE))

text = "Name hello \nLastname hello"
pattern = r"^\w+"
print(re.findall(pattern, text, flags=re.MULTILINE))