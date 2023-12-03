import json
import os

# load json file from this file's directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, 'sample_agent.json')
    
with open(FILE_PATH) as f:
    sample_agent_json = json.load(f)

class HumanResources():
    def __init__(self):
        self.agent_json = sample_agent_json

    def __repr__(self):
        return f'{self.agents}'
    
    def _create(self, new_agent):
        self.agent_json[new_agent["name"]] = new_agent
        return self.agent_json[new_agent["name"]]
    
    def _read(self, agent_name):
        return self.agent_json[agent_name]
    
    def _update(self, agent_name, new_agent):
        self.agent_json[agent_name] = new_agent
        return self.agent_json[agent_name]
    
    def _delete(self, agent_name):
        del self.agent_json[agent_name]
        return self.agent_json
    
    def agent_object(self, agent_name):
        return self.agent_json[agent_name]
    
    def select_agents(self):
        return list(self.agent_json.keys())
    

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