class Mod:
    @staticmethod
    def lift_gate(gate):
        for g in gate:
            g.center_y += 1.0
