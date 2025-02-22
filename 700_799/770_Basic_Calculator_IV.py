import re
from collections import defaultdict
from itertools import product
from typing import List, Optional, Mapping


class Term:
    def __init__(self, expression: Optional[str] = None, init_term: Optional[Mapping[str, int]] = None):
        self.coeffs = defaultdict(int, init_term or {})

        if expression and (expression.isdigit() or (expression.startswith("-") and expression[1:].isdigit())):
            self.coeffs[""] += int(expression)
        elif expression:
            self.coeffs[expression] += 1

    def __add__(self, other: "Term") -> "Term":
        return self._combine(other, True)

    def __sub__(self, other: "Term") -> "Term":
        return self._combine(other, False)

    def __mul__(self, other: "Term") -> "Term":
        multiplied = defaultdict(int)

        for (lvar, lval), (rvar, rval) in product(self.coeffs.items(), other.coeffs.items()):
            merged_var = "*".join(sorted(self._split_var(lvar) + self._split_var(rvar)))
            multiplied[merged_var] += lval * rval

        return Term(init_term=multiplied)

    def get(self) -> List[str]:
        return [
            f"{val}{'*' if var else ''}{var}"
            for var, val in sorted(self.coeffs.items(), key=lambda x: (-len(self._split_var(x[0])), x[0]))
            if val
        ]

    def _combine(self, other: "Term", add: bool) -> "Term":
        merged = self.coeffs.copy()

        for var, val in other.coeffs.items():
            merged[var] += val if add else -val

        return Term(init_term=merged)

    def _split_var(self, var: str) -> List[str]:
        return var.split("*") if var else []


class Solution:
    def basicCalculatorIV(self, expr: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        mappings = dict(zip(evalvars, evalints))
        expr = re.sub(r"[a-z0-9]+", lambda m: f"Term('{mappings.get(m.group(), m.group())}')", expr)

        return eval(expr).get()
