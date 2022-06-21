import pygame
import random

WIDTH, HEIGHT = 600, 600
SIZE = 20
FPS = 30


class Snake:
    def _init_(self):
        self.segments = []
        self.vel_x = 1
        self.vel_y = 0
        self.create_snake()
        self.head = self.segments[0]
        self.alive = True
        self.score = 0

    def create_snake(self):
        x = 300
        for _ in range(3):
            self.add_segment(x, 300)
            x -= SIZE

    def add_segment(self, posx, posy):
        new_segment = pygame.Rect(posx, posy, SIZE, SIZE)
        self.segments.append(new_segment)

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window, (255, 255, 255), segment)

    def update(self):
        if self.alive:
            for i in range(len(self.segments)-1, 0, -1):
                self.segments[i].x = self.segments[i-1].x
                self.segments[i].y = self.segments[i-1].y
            self.head.x += self.vel_x * SIZE
            self.head.y += self.vel_y * SIZE

    def check_collision(self):
        # keluar atau nabrak tembok
        if self.head.left < 0 or self.head.right > WIDTH or self.head.top < 0 or self.head.bottom > HEIGHT:
            self.alive = False
        # cek collision head dengan segments
        for segment in self.segments[1:]:
            if self.head.colliderect(segment):
                self.alive = False

        # cek collision dengan food
        if self.head.colliderect(food.rect):
            self.add_segment(self.segments[-1].x, self.segments[-1].y)
            food.reset_pos()
            self.score += 1
            return True

    def up(self):
        if not self.head.y - self.segments[1].y == SIZE:
            self.vel_x = 0
            self.vel_y = -1

    def down(self):
        if not self.head.y - self.segments[1].y == -SIZE:
            self.vel_x = 0
            self.vel_y = 1

    def left(self):
        if not self.head.x - self.segments[1].x == SIZE:
            self.vel_x = -1
            self.vel_y = 0 