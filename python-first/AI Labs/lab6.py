class VacuumCleanerAgent:
    def __init__(self):
        self.location = 'A'

    def perceive(self, location, status):
        return [location, status]

    def act(self, percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'
        else:
            return 'Do nothing'


class VacuumCleanerEnvironment:
    def __init__(self):
        self.location_status = {'A': 'Dirty', 'B': 'Dirty'}

    def get_percept(self, agent_location):
        return [agent_location, self.location_status[agent_location]]

    def update_location_status(self, location):
        self.location_status[location] = 'Clean'

    def is_environment_clean(self):
        return all(status == 'Clean' for status in self.location_status.values())

    def run(self, agent):
        agent_location = agent.location
        while not self.is_environment_clean():
            percept = self.get_percept(agent_location)
            action = agent.act(percept)
            print(f'Percept: {percept}, Action: {action}')
            if action == 'Suck':
                self.update_location_status(agent_location)
            elif action == 'Left' or action == 'Right':
                agent_location = 'A' if agent_location == 'B' else 'B'
            elif action == 'Do nothing':
                pass
            else:
                print('Invalid action')
                break
            print(f'Location status: {self.location_status}')


# Create an instance of the agent and the environment
agent = VacuumCleanerAgent()
env = VacuumCleanerEnvironment()

# Run the environment with the agent
env.run(agent)
