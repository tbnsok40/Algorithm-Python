from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        print(object)
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    print(object)
    pass


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        print(ticket)
        print(agents)
        raise NotImplemented


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented
