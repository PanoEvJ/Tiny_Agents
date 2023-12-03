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
        # Check if 'role' key exists in new_agent dictionary
        role = new_agent.get('role')
        if role is None:
            return "Missing 'role' key, agent not created"

        new_agent['agent_type'] = 'userproxy' if role == self.chat_initiator else 'assistant'
        new_agent['description'] = f"{role} expert"
        new_agent['human_input_mode'] = ""
        new_agent['skills'] = [role]

        if role not in self.agent_json or not isinstance(self.agent_json[role], list):
            self.agent_json[role] = []
        self.agent_json[role].append(new_agent)
        self._save_to_file()

        return new_agent

    def _read(self, agent_role):
        return self.agent_json.get(agent_role, "Agent role not found")

    def _update(self, agent_role, new_agent):
        if agent_role not in self.agent_json:
            return "Agent role not found"

        new_agent['agent_type'] = 'userproxy' if new_agent['role'] == self.chat_initiator else 'assistant'
        new_agent['description'] = new_agent.get('description', f"{new_agent['role']} expert")
        new_agent['human_input_mode'] = new_agent.get('human_input_mode', "")
        new_agent['skills'] = new_agent.get('skills', [new_agent['role']])

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
            agents = self.agent_json.get(role, [])
            if agents:
                result.extend(agents)  # Ensure that agents is a list of dictionaries
        return result

    def _save_to_file(self):
        with open(FILE_PATH, 'w') as f:
            json.dump(self.agent_json, f, indent=4)



if __name__ == "__main__":
    hr = HumanResources()
    # assert _create() returns a new agent object: {'name': 'finance', 'title': 'finance manager'}
    assert hr._create({"name": "finance", "title": "finance manager"}) == {
        "name": "finance",
        "title": "finance manager",
    }
    # assert _read() returns an agent object: {'name': 'finance', 'title': 'finance manager'}
    assert hr._read("finance") == {"name": "finance", "title": "finance manager"}
    # assert _update() returns an updated agent object: {'name': 'finance', 'title': 'senior finance manager'}
    assert hr._update(
        "finance", {"name": "finance", "title": "senior finance manager"}
    ) == {"name": "finance", "title": "senior finance manager"}
    # assert _delete() returns json all agents without the deleted agent, just check the names of the agents: ['sales', 'marketing', 'engineer']
    temp_json = hr._delete("finance")
    assert list(temp_json.keys()) == ["sales", "marketing", "engineer"]
    # assert select_agents() returns a list of all agents: ['sales', 'marketing', 'engineer']
    assert hr.select_agents() == ["sales", "marketing", "engineer"]

    print("All tests passed!")
