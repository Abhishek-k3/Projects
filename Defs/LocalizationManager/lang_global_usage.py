
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette

hidden_eye_logo = """
 {1} █████████    ██████████      ██████████    ███████
 {1}        ██            ██              ██         ██
 {1} █████████            ██      ██████████         ██
 {1}        ██            ██      ██                 ██
 {1} █████████            ██      ██████████    ████████████""".format(
    default_palette[4], default_palette[2], default_palette[0])

input_line = "\n{0}Jit Hack>>>  {1}".format(default_palette[0],
                                              default_palette[2])
official_website_link = "".format(
    default_palette[0])
by_darksec = "{0}** BY: 3721 **".format(default_palette[0])
line_of_dots = "{0}...............................".format(default_palette[0])
small_logo = """{1}
       """.format(default_palette[0],
                                              default_palette[2])
invalid_option = "Please choose a valid option."
