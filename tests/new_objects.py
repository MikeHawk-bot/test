from manimlib.imports import *            

class PianoTest(Scene):
    CONFIG = {
    }
    def construct(self):
        keyboard = Keyboard()
        keyboard.to_edge(DOWN)
        self.add(keyboard)
        self.add_foreground_mobject(keyboard.black_keys)
        chord = keyboard.get_chord(0,"D","A","Cs","E")
        chord.set_color(RED)

        pentagram = Pentagram(clefs="gf",pentagram_config={"stroke_width":1},bars=[12,14])
        pentagram.add_key_signature("sharp",n=2)
        pentagram.add_tempo(proportion=3/20)
        pentagram.to_edge(UP)
        chord = ChordMobject(
                    Minim(0,pentagram,"bemol",alteration_buff=-0.2,proportion=5/20),
                    Minim(3,pentagram,"sharp",stem_direction=UP,reference_line=1,proportion=5/20)
                )

        self.add(pentagram,chord)
        note1_1 = Crotchet(2,pentagram,reference_line=0)
        note1_2 = Crotchet(0,pentagram,reference_line=0,alteration="natural",proportion=0.4)
        note2_1 = Crotchet(2,pentagram,reference_line=1,alteration="natural")
        note2_2 = Crotchet(0,pentagram,reference_line=1,proportion=0.4)
        pentagram.add_reference_of_proportion()
        self.add(pentagram.ticks,note1_1,note2_1)

        self.play(
            chord.set_notes,[-2,0],6/20,
            TransformFromCopy(note1_1,note1_2.principal),
            FadeIn(note1_2.alteration),
            TransformFromCopy(note2_1.principal,note2_2),
            )
        self.play(
            note1_2.set_note,4,
            note2_2.set_note,4,
            )
        self.wait()


class MusicTest2(Scene):
    def construct(self):
        pentagram = Pentagram(height=1)
        pentagram.add_key_signature("sharp",2)
        chord = ChordMobject(
                    Minim(0,pentagram,"bemol"),
                    Minim(3,pentagram,"sharp",stem_direction=UP)
                )
        chord.set_proportion(0.3)
        self.add(pentagram,chord)
        self.play(chord[0].alteration.set_color,RED)
        self.wait()
        self.play(
            chord.set_notes,[-2,0],0.4,
            chord.set_color,RED
            )
        self.play(
            chord.set_notes,[-1,4],0.6,
            chord.set_color,ORANGE
            )
        self.play(
            chord.set_notes,[1,1],0.8,
            chord.set_color,TEAL
            )
        self.wait(2)

class MusicNumbers(Scene):
    def construct(self):
        self.bemol = MusicTeX(r"""
        \hsize=120mm
        \parindent 2pt
        \nostartrule
        \NOTes\qu{_e}\en
        """,stroke_width=0,stroke_opacity=0)