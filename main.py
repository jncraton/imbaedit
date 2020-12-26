import os, sys, io
import PySimpleGUI as sg
from PIL import Image, ImageEnhance

sg.theme("SystemDefault1")

values = {
    "brightness": 1.0,
    "contrast": 1.0,
    "white": 255,
}

window = sg.Window(
    "Title",
    [
        [
            sg.Image(key="image"),
            sg.Column(
                [
                    [
                        sg.Text("Brightness"),
                        sg.Slider(
                            range=(0.0, 2.0),
                            resolution=0.01,
                            default_value=values["brightness"],
                            key="brightness",
                            orientation="h",
                            enable_events=True,
                        ),
                    ],
                    [
                        sg.Text("Contrast"),
                        sg.Slider(
                            range=(0.0, 2.0),
                            resolution=0.01,
                            default_value=values["contrast"],
                            key="contrast",
                            orientation="h",
                            enable_events=True,
                        ),
                    ],
                    [
                        sg.Text("White Level"),
                        sg.Slider(
                            range=(0, 255),
                            resolution=1,
                            default_value=values["white"],
                            key="white",
                            orientation="h",
                            enable_events=True,
                        ),
                    ],
                    [
                        sg.Button("Run"),
                    ],
                ]
            ),
        ]
    ],
)

event, values = window.read(timeout=0)


def set_white_level(pixel, level):
    if sum(pixel) > level * 3:
        return (255, 255, 255)
    else:
        return pixel


def apply_filters(im, values):
    im = ImageEnhance.Brightness(im).enhance(values["brightness"])
    im = ImageEnhance.Contrast(im).enhance(values["contrast"])
    im.putdata([set_white_level(p, values["white"]) for p in im.getdata()])

    return im

with Image.open(sys.argv[1]) as im_orig:
    im_orig.thumbnail((400, 300))
    while True:
        im = apply_filters(im_orig, values)
        b = io.BytesIO()
        im.save(b, "PNG")
        image_bytes = b.getvalue()

        window["image"].update(data=image_bytes)

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Run":
            print("Running batch conversion...")
            break
