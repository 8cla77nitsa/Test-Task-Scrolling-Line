from manim import *

config.pixel_width = 100
config.pixel_height = 100
config.frame_width = 3


class ScrollingLine(Scene):
    def construct(self):
        global mytext
        mytext = mytext.upper().split()
        textgroup = VGroup()
        words = []

        for i in range(len(mytext)):
            if i == 0:
                words.append(Text(mytext[i], font="Arial", font_size=144))
            else:
                word = Text(mytext[i], font="Arial", font_size=144)
                word.next_to(words[i - 1], RIGHT, buff=0.7)
                words.append(word)
            textgroup.add(words[i])

        textgroup.to_edge(RIGHT).shift(RIGHT * textgroup.width + RIGHT * 0.5)
        self.play(
            textgroup.animate.to_edge(LEFT).shift(LEFT * textgroup.width + LEFT * 0.5),
            run_time=3, rate_func=linear)


mytext = "Привет мир!"
