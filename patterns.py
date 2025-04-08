class Patterns:
    def sqrPattern(self, n):
        for i in range(1, n):
            for j in range(1, n):
                print("* ", end="")
            print()

    def rightAngleTriangle(self, n):
        for i in range(1, n):
            for j in range(i):
                print("* ", end="")
            print()

    def numberTriangleSameColumn(self, n):
        for i in range(n):
            for j in range(1, i + 1):
                print(j, " ", end="")
            print()

    def numberTriangleSameRow(self, n):
        for i in range(n):
            for j in range(1, i + 1):
                print(i, " ", end="")
            print()

    def inverseTriangle(self, n):
        for row in range(n):
            for col in range(n - row):
                print("* ", end="")
            print()

    def inverseNumber(self, n):
        for row in range(1, n + 2):
            for col in range(1, (n + 2) - row):
                print(col, " ", end="")
            print()

    def equiTriangle(self, n):
        for row in range(1, n + 1):
            space = (n) - row
            star = 2 * row - 1
            print(space * " ", star * "*")
        print()

    def inverseEquiTriangle(self, n):
        for row in range(1, n + 1):
            space = row
            star = 2 * (n - row) - 1
            print(space * " ", star * "*")
        print()


sol = Patterns()
# sol.sqrPattern(5)
# sol.rightAngleTriangle(7)
# sol.numberTriangle(7)
# sol.numberTriangleSameRow(7)
# sol.inverseTriangle(6)
# sol.inverseNumber(6)
# sol.equiTriangle(6)
sol.inverseEquiTriangle(6)
