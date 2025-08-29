from manim import *
import numpy as np

class Box(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(width=10, height=4, color=WHITE, fill_opacity=0.1, **kwargs)
        self.center()

class Ball(Circle):
    def __init__(self, contenedor, **kwargs):
        super().__init__(radius=0.05, color=BLUE, fill_opacity=0.8, **kwargs)
        self.set_stroke(width=.1, color=RED)
        self.move_to(ORIGIN)

        # Velocidad inicial en X e Y
        random_x= np.random.uniform(-contenedor.width/2 + self.radius, contenedor.width/2 - self.radius)
        random_y= np.random.uniform(-contenedor.height/2 + self.radius, contenedor.height/2 - self.radius)
        self.move_to(np.array([random_x, random_y, 0]))
        self.velocity = rotate_vector(np.array([2, 1, 0]), angle=np.random.uniform(0, 2*PI))
        self.counter = Integer(0)
        self.counter.next_to(self, UP)
        self.path = TracedPath(self.get_center, stroke_color=YELLOW)

         # Función para actualizar la posición de la bola
         # y manejar las colisiones con las paredes del contenedor

        def update_ball(ball, dt):
            pos = ball.get_center()
            ball.counter.next_to(ball, UP)

            # Actualizar posición con la velocidad
            new_pos = pos + self.velocity * dt

            # Colisiones con las paredes horizontales (izquierda/derecha)
            if new_pos[0] + ball.radius > contenedor.width/2:
                self.velocity[0] = -abs(self.velocity[0])  # Rebote izquierda
                ball.counter.increment_value()
            if new_pos[0] - ball.radius < -contenedor.width/2:
                self.velocity[0] = abs(self.velocity[0])   # Rebote derecha
                ball.counter.increment_value()

            # Colisiones con las paredes verticales (arriba/abajo)
            if new_pos[1] + ball.radius > contenedor.height/2:
                self.velocity[1] = -abs(self.velocity[1])  # Rebote abajo
                self.counter.increment_value()
            if new_pos[1] - ball.radius < -contenedor.height/2:
                self.velocity[1] = abs(self.velocity[1])   # Rebote arriba
                self.counter.increment_value()

            # Mover bola a la nueva posición
            ball.move_to(pos + self.velocity * dt)

        self.add_updater(update_ball)

class TwoBalls(Scene):
    def construct(self):
        box = Box()
        balls=VGroup()
        for _ in range(10):
            new_ball=Ball(box)
            new_ball.shift(RIGHT*0.5*_)
            balls.add(new_ball, new_ball.counter, new_ball.path)
        self.add(box, balls)
        self.wait(10)
