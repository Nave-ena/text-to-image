from PIL import Image, ImageDraw, ImageFont

# Prompt user for input text
text = input("Enter text to convert to image: ")

# Create image with white background
width, height = 400, 200
img = Image.new("RGB", (width, height), "white")

# Get a drawing context
draw = ImageDraw.Draw(img)

# Choose a font and font size
font = ImageFont.truetype("arial.ttf", 20)

# Calculate text size and position
textwidth, textheight = draw.textsize(text, font)
x = (width - textwidth) / 2
y = (height - textheight) / 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill="black")

# Save the image to a file
img.save("text_image.png")
