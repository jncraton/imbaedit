import os, sys, io
import PySimpleGUI as sg
from PIL import Image, ImageEnhance

sg.theme('SystemDefault1')

values = {
    'brightness': 1.0,
    'contrast': 1.0,
}

window = sg.Window('Title',
  [[
    sg.Image(key='image'),
    sg.Column([
        [sg.Text("Brightness"), sg.Slider(range=(0.0,2.0), resolution=.01, default_value=values['brightness'], key="brightness", orientation='h', enable_events=True)],
        [sg.Text("Contrast"), sg.Slider(range=(0.0,2.0), resolution=.01, default_value=values['contrast'], key="contrast", orientation='h', enable_events=True)],
    ]),
  ]])

event, values = window.read(timeout=0)

with Image.open('01.jpg') as im_orig:
    im_orig.thumbnail((400,300))
    while True:
        im = im_orig
        im = ImageEnhance.Brightness(im).enhance(values['brightness'])
        im = ImageEnhance.Contrast(im).enhance(values['contrast'])
        b = io.BytesIO()
        im.save(b, 'PNG')
        image_bytes = b.getvalue()

        window['image'].update(data=image_bytes)

        print(event, values)

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
                break
