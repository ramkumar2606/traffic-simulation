class Color:
    @classmethod
    def get(cls, color_indicator):
        if color_indicator == 1:
            return """
                  Red
                
            """
        elif color_indicator == 2:
            return """
                green
            """
        else:
            return """
                yellow
            """