from .models import Dependacy, Side, Attribute


class RuleEngine:
    def __init__(self, dependancies, rules, console=None) -> None:
        self.dependancies = dependancies
        self.rules = rules
        if not console is None:
            self.log = console.output_to_console
        else:
            self.log = print
        pass

    def apply_rules(self, d):
        while d.state == "unknown":
            for r in self.rules:
                if r["test"](d, self.dependancies):
                    self.log(f"Rule Matched: {r['name']}")
                    old_d = Dependacy(d.left_side, d.right_side, d.origin, d.state)
                    d = r["action"](d, self.dependancies)
                    if r["name"] == "CAN_PROVE_SOMETHING":
                        self.log(f"{old_d} is now {d} Because of {d.origin}")
                    elif r["name"] == "CANT_PROVE_ANYTHING":
                        self.log(f"Can't derive any none-trivial attributes from {d.left_side}")
                        self.log("State set to blocked")
                    elif r["name"] == "FD_PROVEN":
                        self.log(f"{d} has been proven")
                    elif r["name"] == "FD_BLOCKED":
                        self.log(f"{d} can't be derived")
                    elif r["name"] == "RIGHTSIDE_EMPTY":
                        self.log("State set to proven")
                    else:
                        self.log(f"{old_d} is now {d}")

            