places = ['Ireland', 'New Zealand', 'Singapore', 'Brazil', 'Alaska']
print("Original Order")
print(places)

print("\nAlphabetical:")
print(sorted(places))

print("\nOrignal Order")
print(places)

print("\nReverse alphabetical")
print(sorted(places, reverse=True))

print("\nOrginal Order")
print(places)

print("\nReversed:")
places.reverse()
print(places)

print("\nAphabetical")
places.sort()
print(places)

print("\nReverse Alphabetical")
places.sort(reverse=True)
print(places)
