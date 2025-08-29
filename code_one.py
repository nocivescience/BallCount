from manim import *

class NewtonLaws(Scene):
    def construct(self):
        # Título
        title = Text("Leyes de Newton", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # === Primera Ley de Newton ===
        ley1_title = Text("Primera Ley de Newton", font_size=36, color=BLUE)
        self.play(FadeIn(ley1_title, shift=DOWN))
        self.wait(1)

        formula1 = MathTex(r"F_{\text{neto}} = 0 \implies v = \text{cte}", font_size=42)
        formula1.next_to(ley1_title, DOWN, buff=0.5)
        self.play(Write(formula1))
        self.wait(2)

        # Animación: un objeto que sigue en movimiento
        obj = Square(side_length=0.6, color=WHITE, fill_opacity=0.8)
        obj.shift(LEFT*4)
        self.play(FadeIn(obj))
        self.wait(1)
        self.play(obj.animate.shift(RIGHT*8), run_time=4, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(VGroup(ley1_title, formula1, obj)))

        # === Tercera Ley de Newton ===
        ley3_title = Text("Tercera Ley de Newton", font_size=36, color=RED)
        self.play(FadeIn(ley3_title, shift=DOWN))
        self.wait(1)

        formula3 = MathTex(r"F_{AB} = -F_{BA}", font_size=42)
        formula3.next_to(ley3_title, DOWN, buff=0.5)
        self.play(Write(formula3))
        self.wait(2)

        # Animación: dos objetos empujándose
        A = Circle(radius=0.4, color=BLUE, fill_opacity=0.7)
        B = Circle(radius=0.4, color=GREEN, fill_opacity=0.7)
        A.shift(LEFT*2)
        B.shift(RIGHT*2)

        self.play(FadeIn(A), FadeIn(B))
        self.wait(1)

        # Fuerzas con flechas opuestas
        fA = Arrow(A.get_right(), A.get_right() + RIGHT*1.5, buff=0.1, color=YELLOW)
        fB = Arrow(B.get_left(), B.get_left() + LEFT*1.5, buff=0.1, color=YELLOW)

        self.play(GrowArrow(fA), GrowArrow(fB))
        self.wait(2)

        # Movimiento por acción y reacción
        self.play(A.animate.shift(LEFT*2), B.animate.shift(RIGHT*2), run_time=2)
        self.wait(1)

        self.play(FadeOut(VGroup(ley3_title, formula3, A, B, fA, fB)))

        # Conclusión
        conclusion = Text("La clave: siempre dos cuerpos, no uno solo", font_size=36, color=YELLOW)
        self.play(Write(conclusion))
        self.wait(3)
