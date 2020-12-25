import os, sys, io
import PySimpleGUI as sg
from PIL import Image, ImageEnhance

values = {
    'brightness': 1.0,
    'contrast': 1.0,
}

# https://pysimplegui.readthedocs.io/en/latest/call%20reference/
# https://pillow.readthedocs.io/en/5.1.x/reference/index.html
 
while True:
    with Image.open('01.jpg') as im:
        im = ImageEnhance.Brightness(im).enhance(values['brightness'])
        im = ImageEnhance.Contrast(im).enhance(values['contrast'])
        im.thumbnail((400,300))
        b = io.BytesIO()
        im.save(b, 'PNG')
        image_bytes = b.getvalue()

        print(values)

        event, values = sg.Window('Title',
          [[
            sg.Image(data=image_bytes),
            sg.Column([
                [sg.Text("Brightness"), sg.Slider(range=(0.0,2.0), resolution=.01, default_value=values['brightness'], key="brightness", orientation='h', enable_events=True)],
                [sg.Text("Contrast"), sg.Slider(range=(0.0,2.0), resolution=.01, default_value=values['contrast'], key="contrast", orientation='h')],
            ]),
          ],
          [sg.Submit()]]).read(close=True)

        print(event, values)

        if not event:
            exit(0)
