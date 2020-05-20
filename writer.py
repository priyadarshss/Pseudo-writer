import random

colour = ""
letter_set = "set0"
bool_color = False
letter_type = ""

html_default = [
    "<html><head><style>.lines{width:100%;height:auto;float:left;}#paper{background:white;background-image:url('images/texture1.png');height:auto;float:left;padding:50px 50px;width:90%;}img,span{height:25px;width:10px;float:left;margin-top:5px;margin-bottom:10px;}.clblack{filter:brightness(30%);}.clblue{filter:brightness(100%);}</style></head><body><div id='paper'>"
    ]

with open('write_here.txt', 'r') as textfile:
    for line in textfile:
        lineee = line.strip()
        html_default.append('<div class="lines">')
        for ch in lineee:
            chcode = ord(ch)
            if(chcode == 96):
                if(bool_color):
                    colour = "blue"
                    bool_color = False
                else:
                    colour = "black"
                    bool_color = True
            elif(chcode >= 65 and chcode <= 90):
                letter_type = "caps"
                ch = ch.lower()
            elif(chcode >= 97 and chcode <= 177):
                letter_type = "small"
            elif(chcode >= 48 and chcode <= 57):
                letter_type = "symbers"
                ch = "{}".format(chcode)
            elif(chcode == 32 or chcode == 36):
                html_default.append("<span></span>")
            else:
                letter_type = "symbers"
                ch = "{}".format(chcode)
            if(chcode != 96 and chcode != 32 and chcode != 36):
                html_default.append("<img src='images/letters/{}/{}/{}/{}.png'/>".format(
                    letter_set, colour, letter_type, ch))
        html_default.append('</div>')
html_default.append('</div></body></html>')

with open('job.html', 'w') as job_html:
    job_html.writelines(html_default)
