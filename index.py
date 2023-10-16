import math
import pygame
import sys

# Constants
WIDTH, HEIGHT = 640, 480
MAX_RAY_DEPTH = 5

# Sphere class
class Sphere:
    def __init__(self, center, radius, surface_color, reflection=0, transparency=0, emission_color=None):
        self.center = center
        self.radius = radius
        self.radius2 = radius * radius
        self.surface_color = surface_color
        self.emission_color = emission_color if emission_color else Vec3(0, 0, 0)
        self.transparency = transparency
        self.reflection = reflection

    def intersect(self, rayorig, raydir, t0, t1):
        l = self.center - rayorig
        tca = l.dot(raydir)
        if tca < 0:
            return False
        d2 = l.dot(l) - tca * tca
        if d2 > self.radius2:
            return False
        thc = math.sqrt(self.radius2 - d2)
        t0 = tca - thc
        t1 = tca + thc
        return True

# Vec3 class
class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, value):
        return Vec3(self.x * value, self.y * value, self.z * value)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        length = self.length()
        if length > 0:
            inv_length = 1 / length
            self.x *= inv_length
            self.y *= inv_length
            self.z *= inv_length

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

def mix(a, b, mix):
    return b * mix + a * (1 - mix)

def trace(rayorig, raydir, spheres, depth):
    tnear = float("inf")
    sphere = None

    for s in spheres:
        t0, t1 = float("inf"), float("inf")
        if s.intersect(rayorig, raydir, t0, t1):
            if t0 < 0:
                t0 = t1
            if t0 < tnear:
                tnear = t0
                sphere = s

    if not sphere:
        return Vec3(2, 2, 2)  # Background color

    surface_color = Vec3(0, 0, 0)
    phit = rayorig + raydir * tnear
    nhit = phit - sphere.center
    nhit.normalize()

    bias = 1e-4
    inside = False

    if raydir.dot(nhit) > 0:
        nhit = -nhit
        inside = True

    if (sphere.transparency > 0 or sphere.reflection > 0) and depth < MAX_RAY_DEPTH:
        facingratio = -raydir.dot(nhit)
        fresneleffect = mix(pow(1 - facingratio, 3), 1, 0.1)
        refldir = raydir - nhit * 2 * raydir.dot(nhit)
        refldir.normalize()
        reflection = trace(phit + nhit * bias, refldir, spheres, depth + 1)
        refraction = Vec3(0, 0, 0)

        if sphere.transparency:
            ior = 1.1
            eta = ior if inside else 1 / ior
            cosi = -nhit.dot(raydir)
            k = 1 - eta * eta * (1 - cosi * cosi)
            refrdir = raydir * eta + nhit * (eta * cosi - math.sqrt(k))
            refrdir.normalize()
            refraction = trace(phit - nhit * bias, refrdir, spheres, depth + 1)

        surface_color = (reflection * fresneleffect + refraction * (1 - fresneleffect) * sphere.transparency) * sphere.surface_color
    else:
        for s in spheres:
            if s.emission_color.x > 0:
                transmission = 1
                light_direction = s.center - phit
                light_direction.normalize()
                for j in spheres:
                    if s != j:
                        t0, t1 = float("inf"), float("inf")
                        if j.intersect(phit + nhit * bias, light_direction, t0, t1):
                            transmission = 0
                            break
                surface_color += sphere.surface_color * transmission * max(0, nhit.dot(light_direction)) * s.emission_color

    return surface_color + sphere.emission_color

def save_ppm_image(image, filename):
    with open(filename, "wb") as ppm_file:
        ppm_file.write(bytearray("P6\n", "utf-8"))
        ppm_file.write(bytearray(f"{WIDTH} {HEIGHT}\n255\n", "utf-8"))
        for y in range(HEIGHT):
            for x in range(WIDTH):
                color = image.get_at((x, y))
                ppm_file.write(bytearray([color.r, color.g, color.b]))

def render(spheres):
    image = pygame.Surface((WIDTH, HEIGHT))
    inv_width = 1 / float(WIDTH)
    inv_height = 1 / float(HEIGHT)
    fov = 30
    aspect_ratio = WIDTH / float(HEIGHT)
    angle = math.tan(math.pi * 0.5 * fov / 180.)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            xx = (2 * ((x + 0.5) * inv_width) - 1) * angle * aspect_ratio
            yy = (1 - 2 * ((y + 0.5) * inv_height)) * angle
            raydir = Vec3(xx, yy, -1)
            raydir.normalize()
            color = trace(Vec3(0, 0, 0), raydir, spheres, 0)
            image.set_at((x, y), (int(min(1, color.x) * 255), int(min(1, color.y) * 255), int(min(1, color.z) * 255)))

    save_ppm_image(image, "untitled.ppm")

if __name__ == "__main__":
    spheres = [
        Sphere(Vec3(0.0, -10004, -20), 10000, Vec3(0.20, 0.20, 0.20), 0, 0.0),
        ]
    render(spheres=spheres)
