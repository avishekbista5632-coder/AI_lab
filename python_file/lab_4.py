class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment  # Environment is a 2D list representing the room
    def sense(self, location):
        # Sense the dirt at the current location
        return self.environment[location[0]][location[1]] == 'dirty'
    def clean(self, location):
        # Clean the current location
        self.environment[location[0]][location[1]] = 'clean'
    def move(self, location, direction):
        # Move to a new location based on direction
        if direction == 'up':
            return (location[0] - 1, location[1])
        elif direction == 'down':
            return (location[0] + 1, location[1])
        elif direction == 'left':
            return (location[0], location[1] - 1)
        elif direction == 'right':
            return (location[0], location[1] + 1)    
    def run(self, start_location):
        location = start_location
        while True:
            if self.sense(location):
                self.clean(location)
                print(f"Cleaned location {location}")
            else:
                # Move to the next location (this is a simple strategy)
                new_location = self.move(location, 'right')
                if new_location[1] >= len(self.environment[0]):
                    new_location = self.move(location, 'down')
                    if new_location[0] >= len(self.environment):
                        break  # Stop if we've moved beyond the environment
                    else:
                        location = (new_location[0], 0)
                else:
                    location = new_location
# Example environment
environment = [
    ['clean', 'dirty', 'clean'],
    ['dirty', 'clean', 'dirty'],
    ['clean', 'clean', 'dirty']
]
agent = VacuumCleanerAgent(environment)
agent.run((0, 0))
print("Final Environment State:", environment)
