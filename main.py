from manim import *

config.pixel_width = 100
config.pixel_height = 100
config.frame_width = 1


class ScrollingLine(Scene):
    def construct(self):
        global mytext
        mytext.replace(" ", f'<span fgcolor="{BLACK}">_</span>')
        textobject = MarkupText(mytext, font="Arial", font_size=48)
        textobject.to_edge(RIGHT).shift(RIGHT * textobject.width + RIGHT)
        self.play(
            textobject.animate.to_edge(LEFT).shift(LEFT * textobject.width + LEFT),
            run_time=3, rate_func=linear)


mytext = "Привет мир!"
