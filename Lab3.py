import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Define tourist locations and their coordinates
tourist_destinations = {
    "Jaipur": (26.9124, 75.7873),
    "Udaipur": (24.5854, 73.7125),
    "Jodhpur": (26.2389, 73.0243),
    "Pushkar": (26.4907, 74.5523),
    "Jaisalmer": (26.9157, 70.9083),
    "Mount Abu": (24.5925, 72.7156),
    "Bikaner": (28.0229, 73.3119),
    "Ajmer": (26.4499, 74.6399),
    "Chittorgarh": (24.8887, 74.6269),
    "Ranthambore": (25.8667, 76.3500),
    "Bundi": (25.4415, 75.6405),
    "Alwar": (27.5704, 76.6095),
    "Sawai Madhopur": (25.9928, 76.3425),
    "Barmer": (25.7500, 71.4167),
    "Bharatpur": (27.2156, 77.4930),
    "Sikar": (27.6121, 75.1399),
    "Tonk": (26.1664, 75.7885),
    "Kota": (25.2138, 75.8648),
    "Dungarpur": (23.8406, 73.7149),
    "Bhilwara": (25.3475, 74.6408)
}

# Calculate distance between two locations using their coordinates
def calculate_distance(loc1, loc2):
    lat1, lon1 = tourist_destinations[loc1]
    lat2, lon2 = tourist_destinations[loc2]
    radius = 6371  # Earth radius in kilometers
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(delta_lon / 2) * math.sin(delta_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance

# Generate an initial tour plan (random permutation of locations)
def generate_initial_tour(locations):
    return random.sample(locations, len(locations))

# Calculate the total distance of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += calculate_distance(tour[i], tour[(i + 1) % len(tour)])
    return total_distance

# Plot the tour route on a map
def plot_tour_route(tour, locations):
    tour_coordinates = [tourist_destinations[loc] for loc in tour]
    tour_coordinates.append(tour_coordinates[0])
    lats, lons = zip(*tour_coordinates)
    plt.figure(figsize=(10, 6))
    plt.plot(lons, lats, marker='o', linestyle='-', color='b')
    plt.title('Tour Route')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

# Simulated Annealing algorithm for finding the optimal tour
def simulated_annealing(locations, max_iterations, initial_temperature, cooling_rate):
    current_tour = generate_initial_tour(locations)
    best_tour = current_tour
    current_cost = calculate_total_distance(current_tour)
    best_cost = current_cost
    temperature = initial_temperature

    for i in range(max_iterations):
        new_tour = current_tour[:]
        a, b = random.sample(range(len(new_tour)), 2)
        new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
        new_cost = calculate_total_distance(new_tour)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour
            current_cost = new_cost

        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost

        temperature *= cooling_rate

    return best_tour, best_cost

# Main function
def main():
    locations = list(tourist_destinations.keys())
    max_iterations = 10000
    initial_temperature = 100.0
    cooling_rate = 0.95

    best_tour, best_cost = simulated_annealing(locations, max_iterations, initial_temperature, cooling_rate)

    print("Best Tour Route:")
    print(" -> ".join(best_tour))
    print("Total Distance: {:.2f} km".format(best_cost))
    plot_tour_route(best_tour, tourist_destinations)

main()
