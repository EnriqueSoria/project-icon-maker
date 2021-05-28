from typing import Any, Tuple, Optional

from PIL import Image, ImageDraw, ImageFont


class IconMaker:
    size = size_x, size_y = (512, 512)
    bg_color = "white"
    default_font_name: str = 'OpenSansEmoji.ttf'

    project_settings = {
        "position": (int(size_x / 2), int(size_y / 2)),
        "color": "black",
        "size": int(size_y / 2)
    }

    subproject_settings = {
        "position": (0, 0),
        "color": "black",
        "size": 175
    }

    def __init__(self, project: str, subproject: Optional[str] = None):
        self.image = Image.new("RGBA", self.size, self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

        self.draw_icon(**self.project_settings, text=project)
        if subproject:
            self.draw_icon(**self.subproject_settings, text=subproject)

    def draw_icon(self, *, position: Tuple[int, int], text: str, color: Any, size: int):
        self.draw.text(
            xy=position,
            text=text,
            fill=color,
            font=ImageFont.truetype(self.default_font_name, layout_engine=ImageFont.LAYOUT_RAQM),
            embedded_color=True,
        )

    def save(self, name):
        with open(f"./{name}.png", "wb+") as fp:
            self.image.save(fp)


if __name__ == '__main__':
    icon = IconMaker(project="🛒", subproject="🛠", )
    icon.save("test")
