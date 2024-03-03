import flet.canvas as cv
from collections import namedtuple


class SizeAwareControl(cv.Canvas):
    def __init__(self, content=None, resize_interval=100, on_resize=None, **kwargs):
        super().__init__(**kwargs)

        self.content = content
        self.resize_interval = resize_interval
        self.resize_callback = on_resize
        self.on_resize = self.__handle_canvas_resize
        self.resize_interval = namedtuple(
            typename="size", field_names=["width", "height"], defaults=[0, 0]
        )

    def __handle_canvas_resize(self, e):
        self.size = (int(e.width), int(e.height))
        self.update()
        if self.resize_callback:
            self.resize_callback(e)
