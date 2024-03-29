# -*- coding: utf-8 -*-
"""Thumbnail_Generator_Flask_Integration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d_etcjukDcaoud8Pr_YjpSJyjejGvuFr
"""

"""Set up Flask: First, you'll need to install Flask and set up a basic Flask application."""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    # TODO: Implement thumbnail generation code here
    return 'Thumbnail generated!'


"""This code sets up a basic Flask application with a single route at "/generate_thumbnail". 
When the route is accessed with a POST request, the "generate_thumbnail" function is executed.

Receive image files: Next, you'll need to modify the "generate_thumbnail" function to receive the image files from the website. 
You can use Flask's "request" object to access the files in the request payload."""


@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    # Receive image files from request
    pattern_overlay_1 = request.files['pattern_overlay_1']
    pattern_overlay_2 = request.files['pattern_overlay_2']
    subject = request.files['subject']

    # TODO: Implement thumbnail generation code here
    return 'Thumbnail generated!'


"""This code uses Flask's "request.files" attribute to access the uploaded files by their input name.

Generate thumbnail: Now that you have the image files, you can execute the Python code to generate the thumbnail."""


from PIL import Image

@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    # Receive image files from request
    pattern_overlay_1 = request.files['pattern_overlay_1']
    pattern_overlay_2 = request.files['pattern_overlay_2']
    subject = request.files['subject']

    # Convert JPEG images to PNG format
    pattern_overlay_1 = Image.open(pattern_overlay_1)
    pattern_overlay_2 = Image.open(pattern_overlay_2)
    subject = Image.open(subject)

    if pattern_overlay_1.format == 'JPEG':
        pattern_overlay_1 = pattern_overlay_1.convert('RGB')
        pattern_overlay_1.save('pattern_overlay_1.png')

    if pattern_overlay_2.format == 'JPEG':
        pattern_overlay_2 = pattern_overlay_2.convert('RGB')
        pattern_overlay_2.save('pattern_overlay_2.png')

    if subject.format == 'JPEG':
        subject = subject.convert('RGB')
        subject.save('subject.png')

    # TODO: Implement thumbnail generation code here
    return 'Thumbnail generated!'


"""This code uses the Python Imaging Library (Pillow) to convert any JPEG images to PNG format. 
The converted images are saved to disk for use in the thumbnail generation code.

Generate thumbnail (cont'd): Now that you have the converted images, you can use them to generate the thumbnail."""


from io import BytesIO

@app.route('/generate_thumbnail', methods=['POST'])
def generate_thumbnail():
    # Receive image files from request
    pattern_overlay_1 = request.files['pattern_overlay_1']
    pattern_overlay_2 = request.files['pattern_overlay_2']
    subject = request.files['subject']

    # Convert JPEG images to PNG format
    pattern_overlay_1 = Image.open(pattern_overlay_1)
    pattern_overlay_2 = Image.open(pattern_overlay_2)
    subject = Image.open(subject)

    if pattern_overlay_1.format == 'JPEG':
        pattern_overlay_1 = pattern_overlay_1.convert('RGB')
        pattern_overlay_1.save('pattern_overlay_1.png

