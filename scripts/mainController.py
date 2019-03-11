#!/usr/bin/env python
"""
    This Ros Node is the main controller of the UR10 Amazon Picking Challenge Stack
    It acts as both a publusher and subscriber to the various interfaces of the system


"""

import rospy
from std_msgs.msg import String
from visionInterface import VisionInterface

class StateMachine():

    def __init__(self):
        """ Initialisation code """
        # Initialise class variables
        self.node_name = "state_machine"
        self.state = 0
        self.state_mapper = {
            1: self.state_1_object_selection,
            2: self.state_2_vision_sweep,
            3: self.state_3_grasping,
            4: self.state_4_depositing,
            5: self.state_5_completion
        }
        self.num_failures = 0

        # Topics to subscribe to
        self.sub1 = rospy.Subscriber('vision', String, self.vision_callback)

        # Topics State Machine Publishes
        self.pub_state_node_name = 'state_messages'
        self.pub_state_node = rospy.Publisher(self.pub_state_node_name, String, queue_size=10)

    def __enter__(self):
        """ Set up """
        rospy.init_node(self.node_name, anonymous=True)
        self.rate = rospy.Rate(10)
        return self

    def __exit__(self, type, value, traceback):
        """ Tear down """
        pass

    def controller(self):
        """ Main State machine control Loop """
        while not rospy.is_shutdown():
            
            # Test code
            hello_str = "hello world {}".format(rospy.get_time())
            rospy.loginfo(hello_str)
            self.pub_state_node.publish(hello_str)

            
            # State Machine, defined by state_mapper in initialisation, returns state function
            state_function_to_exec = self.state_mapper.get(self.state, lambda: "Invalid State")
            new_state = state_function_to_exec() # Function returns next state
            self.state = new_state
            
            if self.state == 5:
                print("Process Complete")
                break

            # Timings
            self.rate.sleep()

    def state_1_object_selection(self):
        """ Reads the ordered dictionary and selects the next object to grasp

            @return the next state. This will always be state 2 unless we have finished
        """
        
        # TODO

        return 2 # or 5 if complete

    def state_2_vision_sweep(self):
        """ Coordinates between arm movements and vision system to perform the vision sweep necessary
        for the vision system. 

            @return the next state. This may be state 3 for success on receipt of item pose or 1 for
            recognition failure.
        """
        
        # TODO

        return 3 # or 1 on recognition failure

    def state_3_grasping(self):
        """ Coordinates between arm movements and end effector to perform the grasping motion to pick up
        a specified item.

            @return the next state. This may be state 4 on sucess, state 3 on first failure, state 2 on
            second failure, or state 1 on complete failure
        """
        failure = False

        # TODO

        if failure:
            if self.num_failures is 1:
                return 3
            elif self.num_failures is 2:
                return 2
            else:
                return 1
        else:
            return 4

    def state_4_depositing(self):
        """ Coordination between arm movements and end effector to move picked up item from in front of
        shelf to above box to deposit the item safely.

            @return the next state. This may be 1 on sucess, and also 1 on failure
        """
        
        # TODO

        return 1

    def state_5_completion(self):
        """ Tasks to do upon completion, writes pickup output to file """
        
        # TODO
        
        pass
    
    def vision_callback(self):
        """ Callback for the vision messages """
        pass


if __name__ == "__main__":
    """ Run RosNode """
    try:
        with StateMachine() as s:
            s.controller()
            rospy.spin()
    except rospy.ROSInterruptException:
        print("Exception!")

