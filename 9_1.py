from enum import Enum

class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5

class StateMachine:
    state = State.A

    def peep(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 1],
            State.C: [State.D, 2],
            State.D: [State.E, 4],
            State.E: [State.F, 6],
            State.F: [State.F, 8]
        })

    def order(self):
        return self.update({
            State.C: [State.A, 3],
            State.D: [State.A, 5],
            State.E: [State.E, 7]
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal

def main():
    return StateMachine()