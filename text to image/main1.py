from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)
# navs- This code shows output in local host (no need for now)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
     
        text = request.form['text']

        # Create a new image and draw the text on it
        img = Image.new('RGB', (500, 500), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', size=30)
        d.text((10,10), text, fill=(0,0,0), font=font)

        # Save the image to a byte stream
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Return the image as a response to the user
        return send_file(img_byte_arr, mimetype='image/png')
    else:
        return '''
            <form method="post">
                <label for="text">Enter your text:</label><br>
                <input type="text" id="text" name="text"><br>
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)


