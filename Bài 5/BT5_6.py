class Polynomial:
    def __init__(self, coeffs: list):
        self.coeffs = list(coeffs)

    def __str__(self):
        degree = len(self.coeffs) - 1
        terms = []

        for i, coef in enumerate(self.coeffs):
            if coef == 0:
                continue

            power = degree - i

            if power > 1:
                var = f"x^{power}"
            elif power == 1:
                var = "x"
            else:
                var = ""

            if power == 0:
                term = f"{coef}"
            elif coef == 1:
                term = var
            elif coef == -1:
                term = f"-{var}"
            else:
                term = f"{coef}{var}"

            terms.append(term)

        if not terms:
            return "0"

        result = " + ".join(terms)
        result = result.replace("+ -", "- ")

        return result

    def __call__(self, x):
        result = 0
        for coef in self.coeffs:
            result = result * x + coef
        return result

    def __add__(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]

        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b

        new_coeffs = [x + y for x, y in zip(a, b)]

        return Polynomial(new_coeffs)