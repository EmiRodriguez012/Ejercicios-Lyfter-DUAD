class Human:
    def __init__(self, torso):
        self.torso = torso

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Head:
    def __init__(self, eyes, ears, mouth,nose):
        self.eyes = eyes
        self.ears = ears
        self.mouth = mouth
        self.nose = nose

class Eyes:
    def __init__(self, color):
        self.color = color

class Ear:
    def __init__(self, side):
        self.side = side
        
class Mouth:
    def __init__(self):
        pass
        
class Nose:
    def __init__(self):
        pass
class Arm:
    def __init__(self, hand):
        self.hand = hand
        

class Hand:
    def __init__(self, side):
        self.side = side

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Foot:
    def __init__(self,side):
        self.side = side

eyes = Eyes("brown")
left_ear = Ear("left")
right_ear = Ear("right")
nose = Nose()
mouth = Mouth()

head = Head (eyes, [right_ear, left_ear], mouth, nose)

right_hand = Hand("right")
left_hand = Hand("left")

right_arm = Arm (right_hand)
left_arm = Arm (left_hand)

right_foot = Foot ("right")
left_foot = Foot ("left")

right_leg = Leg (right_foot)
left_leg = Leg (left_foot)

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

human = Human (torso)

