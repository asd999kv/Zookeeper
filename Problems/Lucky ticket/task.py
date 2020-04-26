# Save the input in this variable
ticket = [int(i) for i in input()]

# Add up the digits for each half
half1 = ticket[:3]
half2 = ticket[-3:]

# Thanks to you, this code will work
if sum(half1) == sum(half2):
    print("Lucky")
else:
    print("Ordinary")