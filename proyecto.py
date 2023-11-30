import time
import random

class TrafficLight:
    def __init__(self, green_duration, yellow_duration, red_duration):
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.colors = ['GREEN', 'YELLOW', 'RED']
        self.current_color = 'RED'  # Start with red initially
        self.last_color_change = time.time()

    def update(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_color_change

        if self.current_color == 'GREEN' and elapsed_time >= self.green_duration:
            self.current_color = 'YELLOW'
            self.last_color_change = current_time
        elif self.current_color == 'YELLOW' and elapsed_time >= self.yellow_duration:
            self.current_color = 'RED'
            self.last_color_change = current_time
        elif self.current_color == 'RED' and elapsed_time >= self.red_duration:
            self.current_color = 'GREEN'
            self.last_color_change = current_time

    def get_current_color(self):
        return self.current_color

class Car:
    def __init__(self, name):
        self.name = name

    def react_to_traffic_light(self, traffic_light):
        current_color = traffic_light.get_current_color()
        if current_color == 'RED':
            # Probability of 30% for a car to skip the red light
            if random.random() <= 0.3:
                print(f"{self.name}: Raul skipped the red light")
            else:
                print(f"{self.name}: Stopping at red light")
        elif current_color == 'YELLOW':
            print(f"{self.name}: Slowing down for yellow light")
        elif current_color == 'GREEN':
            print(f"{self.name}: Moving through green light")

def simulate_traffic_intersection(green_duration, yellow_duration, red_duration, car_arrival_rate, simulation_time):
    traffic_light = TrafficLight(green_duration, yellow_duration, red_duration)
    cars = []

    start_time = time.time()
    while time.time() - start_time < simulation_time:
        # Update the traffic light state
        traffic_light.update()

        # Create cars at the specified arrival rate
        if random.random() < car_arrival_rate:
            car = Car(f"Car {len(cars) + 1}")
            cars.append(car)
            car.react_to_traffic_light(traffic_light)

        time.sleep(1)  # Simulate 1 second per loop iteration

    print("Simulation ended.")

# Parameters
green_duration = 5  # seconds
yellow_duration = 2  # seconds
red_duration = 4  # seconds
car_arrival_rate = 0.4  # Adjust as needed
simulation_time = 30  # seconds

# Run simulation
simulate_traffic_intersection(green_duration, yellow_duration, red_duration, car_arrival_rate, simulation_time)