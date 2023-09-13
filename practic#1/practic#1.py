class equation_of_a_line:
    """Class - equation of a line"""

    def value_of_dot(self):
        """value of dots"""

        self.list_of_dot = []
        list_of_cord = ["x1", "y1", "x2", "y2"]
        counter = 0
        while len(self.list_of_dot) < 4:
            try:
                value = int(input(f"{list_of_cord[counter]}:"))
                self.list_of_dot.append(value)
                counter += 1
            except ValueError:
                print(f"Please, input number!")
        print(f"""Coordinates of dots: A = ({self.list_of_dot[0]}, {self.list_of_dot[1]})
                     B = ({self.list_of_dot[2]}, {self.list_of_dot[3]})""")
        self.coefficient()

    def coefficient(self):
        """search for odds"""

        self.a = -(self.list_of_dot[1] - self.list_of_dot[3])
        self.b = -(self.list_of_dot[2] - self.list_of_dot[0])
        self.const()

    def const(self):
        """search const"""

        global sign
        c = self.list_of_dot[0] * self.list_of_dot[3] - self.list_of_dot[2] * self.list_of_dot[1]
        if self.b < 0:
            sign = "-"
        elif self.b >= 0:
            sign = "+"
        print(f"{self.a}x {sign} {abs(self.b)}y = {c}")


start = equation_of_a_line()
start.value_of_dot()
