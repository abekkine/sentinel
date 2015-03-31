class Sentinel(object):

    def __init__(self):
        """
        Constructor, for initialization.
        """
        self.nodes_ = []
        self.actions_ = []
        # TODO : more initialization...

    def AddNode(self, name, address):
        """
        Add node for the system to be tracked.
        """
        self.nodes_.append({
            'name' : name,
            'address' : address
        })

    def AddAvailabilityAction(self, conditions, action):
        """
        Add an action which will be taken depending on
        the given conditions.
        - action     : the name of a python module which
                       will be loaded and executed whenever
                       'conditions' are met.
        - conditions : a list of node states defining when
                       then 'action' should be executed.

                     EXAMPLE condition data
                     :[{ 'node': '<node_1_name>', 'state': '<off|on>', 'change': <True|False> }
                      ,{ 'node': '<node_2_name>', 'state': '<off|on>', 'change': <True|False> }
                      ...
                      ,{ 'node': '<node_N_name>', 'state': '<off|on>', 'change': <True|False> }]

                     : If all conditions in list is met, then the action will be executed.
                       When the 'change' field is True, condition is met only when node changing 
                       it's state into given 'state'. Otherwise, condition is met while then node
                       is in given 'state'.
        """
        self.actions_.append({
            'action' : action,
            'conditions' : conditions
        })

    def Run(self):
        """
        Start processing.
        """
        # TODO : Plan execution schema and start running.
        pass
