__doc__ = """A collection of constants that help with debugging and testing"""
from src.models import Attribute, Dependacy, Side

DEBUG_MODE = True

DEBUG_ATTRIBUTES = "{A,B,C,D,E,F,G}"

DEBUG_DEPENDANCIES = [
"A->D",
"BD->ED",
"BC->H",
"D->A",
"H->DEF",
"F->B",
"E->C",
"G->HF"
]