

class State:

    def __init__(self, state_position, current_face, prev=None):
        self.state_position = state_position
        self.current_face = current_face
        self.prev = prev

    def get_prev(self):
        return self.prev
    
    def get_current_face(self):
        return self.current_face
    
    def set_current_face(self, current_face):
        self.prev = self.current_face
        self.current_face = current_face
    
    def increase_position(self):
        self.state_position += 1
    
    def get_position(self):
        return self.state_position
    
    def update_state(self, face):
        self.increase_position()
        self.set_current_face(face)

    def __hash__(self):
        return self.current_face

    def __eq__(self, other):
        return self.current_face

    def __ne__(self, other):
        return not self.current_face == other