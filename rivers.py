rivers = {'nile':'egypt',
          'rhine':'germany',
          'amazon':'brazil'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)
