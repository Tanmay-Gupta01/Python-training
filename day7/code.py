#1.  For Loop Basics: Write a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)


#2.  String Iteration: Write a program that counts vowels in a string.

s = "elephant"
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count += 1
print(count)


#3.  Accumulator Pattern: Calculate the sum of squares from 1 to 100.

sum = 0
for i in range(1,101):
    sum += i**2
print(sum)

#4.  Nested Loops: Create a multiplication table up to 10x10.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    

#5.  Image Processing: Use PIL to invert the colors of an image.

from PIL import Image, ImageOps

# Open the image
image = Image.open("input.jpg")  # Replace with your image file

# Convert to RGB (to handle grayscale images)
image = image.convert("RGB")

# Invert the colors
inverted_image = ImageOps.invert(image)

# Save the result
inverted_image.save("output.jpg")

# Show the inverted image
inverted_image.show()
