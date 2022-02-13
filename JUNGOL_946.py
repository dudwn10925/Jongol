country = dict()
for _ in range(int(input())):
    key, val = input().split()
    country[key] = val
print(country.get(input(), 'Unknown Country'))