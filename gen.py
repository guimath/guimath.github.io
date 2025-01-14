
import os
import text_english, text_french







def event(date, title, sub_title, location, desc, space= '                ', links=None):
    out =  f'{space}<li class="event" data-date="{date}">\n'
    out += f'{space}    <h3>{title}</h3>\n'
    if location != '':
        location = f' <i>{location}</i>'
    link_str = ''
    for link in links:
         link_str += f' <a href="{link["url"]}" target="_blank">{link["type"]}</a>'
    out += f'{space}    <p><strong>{sub_title}</strong>{location}{link_str}</p>\n'
    for t in desc :
        out += f'{space}    <p>{t}</p>\n'
    out += f'{space}</li>\n'
    return out

def timeline(title, lst, first= False, space = '            ') :
    if len(lst) == 0: return ''
    if first : out = f'{space}<h2 class="first-h2">{title}</h2>\n'
    else : out = f'{space}<h2>{title}</h2>\n'
            
    out += f'{space}<ul class="timeline">\n'
    for element in lst :
        if 'links' not in element.keys():
            element['links'] = []
        out += event(
            element['date'], 
            element['title'], 
            element['sub_title'], 
            element['location'], 
            element['desc'],
            space + '    ',
            element['links'])
    return out + f'{space}</ul>\n'


def  generic_item(item, first=False, space='            '):
    if first : out = f'{space}<h3 class="first-h3">{item["name"]}</h3>\n'
    else : out = f'{space}<h3>{item["name"]}</h3>\n'
    for t in item["desc"] :
        out += f'{space}<p>{t}</p>\n'
    if 'level' in item :
        out += f'{space}<div class = "progress-bar">\n'
        out += f'{space}    <div class="fill" style="width: {item["level"]}%;"></div>\n'
        out += f'{space}</div>\n'
        
    return out

def generic_lst(title, lst, first=False, space='            '):
    if len(lst) == 0: return ''
    if first : out = f'{space}<h2 class="first-h2">{title}</h2>\n'
    else : out = f'{space}<h2>{title}</h2>\n'
    out += f'{space}<ul>\n'
    first = True
    for element in lst :
        out += f'{space}<li>\n'
        out +=  generic_item(element, first, space + '   ')
        out += f'{space}</li>\n'
        first = False
    return out + f'{space}</ul>\n'

def save_to_file(text, rel_path):
    abs_path = os.path.dirname(os.path.realpath(__file__))+os.sep+rel_path
    with open(abs_path, mode ='w',encoding='utf-8') as file:  
        file.truncate()
        file.write(text)



def gen(json, eng=True, to_pdf=False, default_dark=False):
    style_sheet = 'dark_theme.css' if default_dark else 'light_theme.css'
    html = f'''
<head>
    <title>GuiMath</title>
    <link rel="icon" href="img/favicon.svg">
    <link href={style_sheet} rel="stylesheet" id="theme-link">
    <script>
        const theme = document.querySelector("#theme-link");
        function lightMode() {{
            if (theme.getAttribute("href") == "light_theme.css") {{
                theme.href = "dark_theme.css";
            }} else {{
                theme.href = "light_theme.css";
            }}
        }}
    </script>
</head>
<body>'''
    if to_pdf:
        first_line= '''<p>
            <svg class="icon-header" "viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M9.83824 18.4467C10.0103 18.7692 10.1826 19.0598 10.3473 19.3173C8.59745 18.9238 7.07906 17.9187 6.02838 16.5383C6.72181 16.1478 7.60995 15.743 8.67766 15.4468C8.98112 16.637 9.40924 17.6423 9.83824 18.4467ZM11.1618 17.7408C10.7891 17.0421 10.4156 16.1695 10.1465 15.1356C10.7258 15.0496 11.3442 15 12.0001 15C12.6559 15 13.2743 15.0496 13.8535 15.1355C13.5844 16.1695 13.2109 17.0421 12.8382 17.7408C12.5394 18.3011 12.2417 18.7484 12 19.0757C11.7583 18.7484 11.4606 18.3011 11.1618 17.7408ZM9.75 12C9.75 12.5841 9.7893 13.1385 9.8586 13.6619C10.5269 13.5594 11.2414 13.5 12.0001 13.5C12.7587 13.5 13.4732 13.5593 14.1414 13.6619C14.2107 13.1384 14.25 12.5841 14.25 12C14.25 11.4159 14.2107 10.8616 14.1414 10.3381C13.4732 10.4406 12.7587 10.5 12.0001 10.5C11.2414 10.5 10.5269 10.4406 9.8586 10.3381C9.7893 10.8615 9.75 11.4159 9.75 12ZM8.38688 10.0288C8.29977 10.6478 8.25 11.3054 8.25 12C8.25 12.6946 8.29977 13.3522 8.38688 13.9712C7.11338 14.3131 6.05882 14.7952 5.24324 15.2591C4.76698 14.2736 4.5 13.168 4.5 12C4.5 10.832 4.76698 9.72644 5.24323 8.74088C6.05872 9.20472 7.1133 9.68686 8.38688 10.0288ZM10.1465 8.86445C10.7258 8.95042 11.3442 9 12.0001 9C12.6559 9 13.2743 8.95043 13.8535 8.86447C13.5844 7.83055 13.2109 6.95793 12.8382 6.2592C12.5394 5.69894 12.2417 5.25156 12 4.92432C11.7583 5.25156 11.4606 5.69894 11.1618 6.25918C10.7891 6.95791 10.4156 7.83053 10.1465 8.86445ZM15.6131 10.0289C15.7002 10.6479 15.75 11.3055 15.75 12C15.75 12.6946 15.7002 13.3521 15.6131 13.9711C16.8866 14.3131 17.9412 14.7952 18.7568 15.2591C19.233 14.2735 19.5 13.1679 19.5 12C19.5 10.8321 19.233 9.72647 18.7568 8.74093C17.9413 9.20477 16.8867 9.6869 15.6131 10.0289ZM17.9716 7.46178C17.2781 7.85231 16.39 8.25705 15.3224 8.55328C15.0189 7.36304 14.5908 6.35769 14.1618 5.55332C13.9897 5.23077 13.8174 4.94025 13.6527 4.6827C15.4026 5.07623 16.921 6.08136 17.9716 7.46178ZM8.67765 8.55325C7.61001 8.25701 6.7219 7.85227 6.02839 7.46173C7.07906 6.08134 8.59745 5.07623 10.3472 4.6827C10.1826 4.94025 10.0103 5.23076 9.83823 5.5533C9.40924 6.35767 8.98112 7.36301 8.67765 8.55325ZM15.3224 15.4467C15.0189 16.637 14.5908 17.6423 14.1618 18.4467C13.9897 18.7692 13.8174 19.0598 13.6527 19.3173C15.4026 18.9238 16.921 17.9186 17.9717 16.5382C17.2782 16.1477 16.3901 15.743 15.3224 15.4467ZM12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21Z"/>
            </svg>
            <a href="https://guimath.gitub.io">guimath.github.io</a></p>
'''
    else :
        if not eng:
            first_line= '''<div class="switches">
                <label class="switch" title="Changer de thème">
                    <input type="checkbox" onclick="lightMode()">
                    <span class="slider round"></span>
                </label>
                <a href="/index.html" class="lang-link" title="English version">🇬🇧</a>
            </div>
'''
        else :
            first_line= '''<div class="switches">
                <label class="switch" title="Swap theme">
                    <input type="checkbox" onclick="lightMode()">
                    <span class="slider round"></span>
                </label>
                <a href="/french-cv.html" class="lang-link" title="Version Française">🇫🇷</a>
            </div>
'''

    html += f'''
    <div class="headr">
        <div class="img-and-title">
            <div class="image-container">
                <img src="img/portrait.webp" alt="Image">
            </div>
            <div class="main_title">
                <p><h1>Guilhem Mathieux</h1></p>
                <p><h3>{json["job_title"]}</h3></p>
            </div>
        </div>
        <div class="infos-div">
            {first_line}
            <p>
                <svg class="icon-header" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.75 5.25L3 6V18L3.75 18.75H20.25L21 18V6L20.25 5.25H3.75ZM4.5 7.6955V17.25H19.5V7.69525L11.9999 14.5136L4.5 7.6955ZM18.3099 6.75H5.68986L11.9999 12.4864L18.3099 6.75Z"/>
                </svg>
                <a href="mailto:guilhem.mathieux.pro@gmail.com">guilhem.mathieux.pro@gmail.com</a>
            </p>
            <p>
                <svg class="icon-header nf" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3 5.5C3 14.0604 9.93959 21 18.5 21C18.8862 21 19.2691 20.9859 19.6483 20.9581C20.0834 20.9262 20.3009 20.9103 20.499 20.7963C20.663 20.7019 20.8185 20.5345 20.9007 20.364C21 20.1582 21 19.9181 21 19.438V16.6207C21 16.2169 21 16.015 20.9335 15.842C20.8749 15.6891 20.7795 15.553 20.6559 15.4456C20.516 15.324 20.3262 15.255 19.9468 15.117L16.74 13.9509C16.2985 13.7904 16.0777 13.7101 15.8683 13.7237C15.6836 13.7357 15.5059 13.7988 15.3549 13.9058C15.1837 14.0271 15.0629 14.2285 14.8212 14.6314L14 16C11.3501 14.7999 9.2019 12.6489 8 10L9.36863 9.17882C9.77145 8.93713 9.97286 8.81628 10.0942 8.64506C10.2012 8.49408 10.2643 8.31637 10.2763 8.1317C10.2899 7.92227 10.2096 7.70153 10.0491 7.26005L8.88299 4.05321C8.745 3.67376 8.67601 3.48403 8.55442 3.3441C8.44701 3.22049 8.31089 3.12515 8.15802 3.06645C7.98496 3 7.78308 3 7.37932 3H4.56201C4.08188 3 3.84181 3 3.63598 3.09925C3.4655 3.18146 3.29814 3.33701 3.2037 3.50103C3.08968 3.69907 3.07375 3.91662 3.04189 4.35173C3.01413 4.73086 3 5.11378 3 5.5Z"/>                
                </svg>
                <a href="tel:+33673779284">(+33) <strong>6 73 77 92 84</strong></a>
            </p>
            <p>
                <svg class="icon-header nf" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 3V6M17 3V6M7.10002 20C7.56329 17.7178 9.58104 16 12 16C14.419 16 16.4367 17.7178 16.9 20M6.2 21H17.8C18.9201 21 19.4802 21 19.908 20.782C20.2843 20.5903 20.5903 20.2843 20.782 19.908C21 19.4802 21 18.9201 21 17.8V8.2C21 7.07989 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V17.8C3 18.9201 3 19.4802 3.21799 19.908C3.40973 20.2843 3.71569 20.5903 4.09202 20.782C4.51984 21 5.07989 21 6.2 21ZM14 11C14 12.1046 13.1046 13 12 13C10.8954 13 10 12.1046 10 11C10 9.89543 10.8954 9 12 9C13.1046 9 14 9.89543 14 11Z"/>
                </svg>
              {json["age"]}
            </p>
        </div>
     </div>
     <div class="main-div-cont"> <div class="main-div">
        <div class="col1">
'''
   


    html += timeline(json['education_title'], json['education_lst'], True)
    html += timeline(json['proj_title'], json['proj_lst'], False)
    html += timeline(json['work_title'], json['work_lst'], False)
    html += '        </div>\n'
    html += '        <div class="col2">\n'

    html += generic_lst(json['language_title'], json['languages_lst'], True)
    html += generic_lst(json['skills_title'], json['skills_lst'], False)
    html += generic_lst(json['interest_title'], json['interest_lst'], False)
    html += '        </div>\n'
    html += '    </div></div>\n'


    html += '''
    <footer>
        <a href="https://www.facebook.com/guilhem.mathieux">
            <svg viewBox="0 0 24 24" class="slogo facebook">
                <path id="primary" d="M14,6h3a1,1,0,0,0,1-1V3a1,1,0,0,0-1-1H14A5,5,0,0,0,9,7v3H7a1,1,0,0,0-1,1v2a1,1,0,0,0,1,1H9v7a1,1,0,0,0,1,1h2a1,1,0,0,0,1-1V14h2.22a1,1,0,0,0,1-.76l.5-2a1,1,0,0,0-1-1.24H13V7A1,1,0,0,1,14,6Z"/>
            </svg>
            @guilhem.mathieux
        </a>
        <a href="http://www.linkedin.com/in/guilhem-mathieux-1277a4185">
            <svg viewBox="0 0 310 310" class="slogo linkedin">
                <path id="XMLID_802_" d="M72.16,99.73H9.927c-2.762,0-5,2.239-5,5v199.928c0,2.762,2.238,5,5,5H72.16c2.762,0,5-2.238,5-5V104.73C77.16,101.969,74.922,99.73,72.16,99.73z"/>
                <path id="XMLID_803_" d="M41.066,0.341C18.422,0.341,0,18.743,0,41.362C0,63.991,18.422,82.4,41.066,82.4c22.626,0,41.033-18.41,41.033-41.038C82.1,18.743,63.692,0.341,41.066,0.341z"/>
                <path id="XMLID_804_" d="M230.454,94.761c-24.995,0-43.472,10.745-54.679,22.954V104.73c0-2.761-2.238-5-5-5h-59.599c-2.762,0-5,2.239-5,5v199.928c0,2.762,2.238,5,5,5h62.097c2.762,0,5-2.238,5-5v-98.918c0-33.333,9.054-46.319,32.29-46.319c25.306,0,27.317,20.818,27.317,48.034v97.204c0,2.762,2.238,5,5,5H305c2.762,0,5-2.238,5-5V194.995C310,145.43,300.549,94.761,230.454,94.761z"/>
            </svg>
            Guilhem Mathieux
        </a>
        <a href="https://github.com/guimath">
            <svg viewBox="0 0 16 16" class="slogo github">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
            @guimath
        </a>
    </footer>
</body>
</html>'''
    return html



def main():
    save_to_file(gen(text_french.TEXT, False), 'french-cv.html')
    save_to_file(gen(text_french.TEXT, False, True), 'french-cv-pdf.html')
    save_to_file(gen(text_french.TEXT, False, True, True), 'french-cv-pdf-dark.html')
    save_to_file(gen(text_english.TEXT, True), 'index.html')

if __name__ == "__main__" :
    main()
