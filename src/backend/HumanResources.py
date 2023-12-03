import json
import os

# Get the current working directory
CURRENT_DIR = os.getcwd()

# Assuming your 'agents.json' file is in the same directory as the notebook
FILE_PATH = os.path.join(CURRENT_DIR, 'agents.json')

# Check if the file exists and read it, otherwise create an empty dictionary
if os.path.exists(FILE_PATH):
    with open(FILE_PATH) as f:
        sample_agent_json = json.load(f)
else:
    sample_agent_json = {}

class HumanResources():
    def __init__(self, chat_initiator):
        self.agent_json = sample_agent_json
        self.chat_initiator = chat_initiator 

    def __repr__(self):
        return f'{self.agent_json}'

    def _create(self, new_agent):
        if new_agent["role"] in self.agent_json:
            raise ValueError(f"Agent with role '{new_agent['role']}' already exists.")

        new_agent['agent_type'] = 'userproxy' if new_agent['role'] == self.chat_initiator else 'assistant'
        self.agent_json[new_agent["role"]] = new_agent
        self._save_to_file()

        return self.agent_json[new_agent["role"]]

    def _read(self, agent_role):
        return self.agent_json.get(agent_role, "Agent role not found")

    def _update(self, agent_role, new_agent):
        if agent_role not in self.agent_json:
            raise ValueError(f"Agent with role '{agent_role}' does not exist.")

        new_agent['agent_type'] = 'userproxy' if new_agent['role'] == self.chat_initiator else 'assistant'
        self.agent_json[agent_role] = new_agent
        self._save_to_file()
        return self.agent_json[agent_role]

    def _delete(self, agent_role):
        if agent_role not in self.agent_json:
            raise ValueError(f"Agent with role '{agent_role}' does not exist.")
        del self.agent_json[agent_role]
        self._save_to_file()
        return "Agent deleted successfully"

    def agent_object(self, agent_role):
        return self.agent_json.get(agent_role, "Agent role not found")


    def select_agents(self):
        return list(self.agent_json.keys())
    
    def get_complete(self, roles_list):
        result = []
        for role in roles_list:
            for agent_name, agent_details in self.agent_json.items():
                if agent_details['role'] == role:
                    result.append(agent_details)
        return result

    def _save_to_file(self):
        with open(FILE_PATH, 'w') as f:
            json.dump(self.agent_json, f, indent=4)




# Example usage
hr = HumanResources()
new_agent = {"name": "Agent Smith", "role": "Analyst", "description": "Data Analysis"}
hr._create(new_agent)

# Print updated agents
print(hr.select_agents())

    

if __name__ == "__main__":
    hr = HumanResources()
    # assert _create() returns a new agent object: {'name': 'finance', 'title': 'finance manager'}
    assert hr._create({"name": "finance", "title": "finance manager"}) == {'name': 'finance', 'title': 'finance manager'}
    # assert _read() returns an agent object: {'name': 'finance', 'title': 'finance manager'}
    assert hr._read("finance") == {'name': 'finance', 'title': 'finance manager'}
    # assert _update() returns an updated agent object: {'name': 'finance', 'title': 'senior finance manager'}
    assert hr._update("finance", {"name": "finance", "title": "senior finance manager"}) == {'name': 'finance', 'title': 'senior finance manager'}
    # assert _delete() returns json all agents without the deleted agent, just check the names of the agents: ['sales', 'marketing', 'engineer']
    temp_json = hr._delete("finance")
    assert list(temp_json.keys()) == ['sales', 'marketing', 'engineer']
    # assert select_agents() returns a list of all agents: ['sales', 'marketing', 'engineer']
    assert hr.select_agents() == ['sales', 'marketing', 'engineer']

    print("All tests passed!")