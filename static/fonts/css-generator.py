import glob, os

os.chdir(".")
css_writer = open("./fonts.css", "w")
json_writer = open("./names.json", "w")

json_writer.write('{\n')
for file in glob.glob("*.ttf"):
    file_name = str(file)
    font_name = file_name[:-4]

    font_name = font_name.replace('.', '')

    css_style = "@font-face {font-family: '" + font_name + "';src: local('" + file_name + "'),url('../fonts/" + file_name + "') format('truetype');}\n\n"
    css_writer.write(css_style)

    json_writer.write("'{}': '{}',\n".format(font_name, font_name))

json_writer.write('}')
json_writer.close()

css_writer.close()
