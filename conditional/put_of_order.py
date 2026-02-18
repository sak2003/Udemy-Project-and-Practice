flavours=["Tulsi","out of stock","Lemon","Discontinued","Ginger"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} found")

print("Out of the loop")