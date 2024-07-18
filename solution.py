############### Math kütüphanesini kullanarak yaptığım senaryo.

import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 1)]

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)

print(f"Minimum mesafe: {min_distance}")






######### Hiçbir kütüphane kullanmadan yaptığım senaryo

## Noktaların tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 1)]

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)

print(f"Minimum mesafe: {min_distance}")
