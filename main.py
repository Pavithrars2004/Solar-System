import tkinter as tk
from math import sin, cos, radians
import tkinter.messagebox
import random

class SolarSystemSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System Simulation")

        self.canvas = tk.Canvas(root, width=800, height=800, bg="black")
        self.canvas.pack()

        self.add_stars()  # Add stars before other elements

        self.speed = 1
        self.angle = 0

        self.sun = self.canvas.create_oval(390, 390, 410, 410, fill="yellow")

        self.planets = [
            {"name": "Mercury", "color": "gray", "distance": 50, "size": 5, "speed": 4.74},
            {"name": "Venus", "color": "orange", "distance": 80, "size": 8, "speed": 3.50},
            {"name": "Earth", "color": "blue", "distance": 110, "size": 10, "speed": 2.98},
            {"name": "Mars", "color": "red", "distance": 150, "size": 7, "speed": 2.41},
            {"name": "Jupiter", "color": "brown", "distance": 200, "size": 20, "speed": 1.31},
            {"name": "Saturn", "color": "gold", "distance": 250, "size": 17, "speed": 0.97},
            {"name": "Uranus", "color": "light blue", "distance": 300, "size": 15, "speed": 0.68},
            {"name": "Neptune", "color": "dark blue", "distance": 350, "size": 15, "speed": 0.54}
        ]

        self.orbits = []
        self.planet_objects = []
        self.planet_labels = []  # To store planet name labels
        for planet in self.planets:
            orbit = self.canvas.create_oval(400 - planet["distance"], 400 - planet["distance"], 400 + planet["distance"], 400 + planet["distance"], outline="white")
            self.orbits.append(orbit)
            obj = self.canvas.create_oval(0, 0, planet["size"]*2, planet["size"]*2, fill=planet["color"])
            self.planet_objects.append(obj)
            label = self.canvas.create_text(0, 0, text=planet["name"], fill="white")
            self.planet_labels.append(label)

        self.canvas.bind("<Button-1>", self.show_planet_info)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        self.slow_button = tk.Button(self.control_frame, text="Slow Down", command=self.slow_down)
        self.slow_button.pack(side=tk.LEFT)

        self.speed_button = tk.Button(self.control_frame, text="Speed Up", command=self.speed_up)
        self.speed_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.update_planets()

    def update_planets(self):
        self.angle += self.speed
        for i, planet in enumerate(self.planets):
            angle_rad = radians(self.angle * planet["speed"])
            x = 400 + planet["distance"] * cos(angle_rad)
            y = 400 + planet["distance"] * sin(angle_rad)
            self.canvas.coords(self.planet_objects[i], x - planet["size"], y - planet["size"], x + planet["size"], y + planet["size"])
            self.canvas.coords(self.planet_labels[i], x, y)

        self.root.after(50, self.update_planets)

    def show_planet_info(self, event):
        for i, obj in enumerate(self.planet_objects):
            if self.canvas.bbox(obj)[0] <= event.x <= self.canvas.bbox(obj)[2] and self.canvas.bbox(obj)[1] <= event.y <= self.canvas.bbox(obj)[3]:
                planet = self.planets[i]
                info = f"{planet['name']}:\nDistance from Sun: {planet['distance']} million km\nOrbit Speed: {planet['speed']} km/s"
                tkinter.messagebox.showinfo("Planet Info", info)
                break

    def slow_down(self):
        self.speed = max(1, self.speed - 1)

    def speed_up(self):
        self.speed += 1

    def pause(self):
        self.speed = 0

    def add_stars(self):
        for _ in range(200):  # Adjust the number of stars as needed
            x = random.randint(0, 800)
            y = random.randint(0, 800)
            self.canvas.create_rectangle(x, y, x+1, y+1, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarSystemSimulation(root)
    root.mainloop()
