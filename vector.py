from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitud(self):
        coordinates_square = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_square))

    def normalized(self):
        try:
            magnitud = self.magnitud()
            return self.times_scalar(1./magnitud)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print v.plus(w)

v = Vector([7.119,8215])
w = Vector([-8.223,0.878])
print v.minus(w)

v = Vector([1.671,-1.012,-0.378])
c = 7.41
print v.times_scalar(c)

print 'Magnitud'

v = Vector([-0.221, 7.437])
print v.magnitud()

print 'Normalized'

v = Vector([5.581, -2.136])
print v.normalized()
