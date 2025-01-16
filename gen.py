
import os
import text_english, text_french
from pathlib import Path
import asyncio
from pyppeteer import launch

ABS_PATH = Path(__file__).parent





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
    abs_path = ABS_PATH / rel_path
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
            <svg class="icon-header" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path id="vector" d="M7.8 12L7.05 12L7.8 12ZM16.2 12H16.95H16.2ZM12 16.2V16.95V16.2ZM14.1729 22.2749L14.3273 23.0088L14.1729 22.2749ZM9.82712 22.2749L9.67269 23.0088L9.82712 22.2749ZM2.27554 8.03225L1.58122 7.74867H1.58122L2.27554 8.03225ZM1.7251 14.1729L0.991173 14.3273L1.7251 14.1729ZM9.82712 1.7251L9.67269 0.991173L9.82712 1.7251ZM14.1729 1.7251L14.3273 0.991174L14.1729 1.7251ZM21.6399 8.07014L21.8576 8.78785L21.6399 8.07014ZM2.35887 8.06976L2.14116 8.78747L2.35887 8.06976ZM21.0312 8.3185C21.4944 9.45344 21.75 10.6959 21.75 12H23.25C23.25 10.4983 22.9553 9.06352 22.42 7.75174L21.0312 8.3185ZM21.75 12C21.75 12.6927 21.6779 13.3678 21.541 14.0184L23.0088 14.3273C23.167 13.5757 23.25 12.7972 23.25 12H21.75ZM21.541 14.0184C20.7489 17.7827 17.7828 20.7489 14.0184 21.541L14.3273 23.0088C18.6735 22.0943 22.0943 18.6735 23.0088 14.3273L21.541 14.0184ZM14.0184 21.541C13.3678 21.6779 12.6927 21.75 12 21.75V23.25C12.7972 23.25 13.5757 23.167 14.3273 23.0088L14.0184 21.541ZM12 21.75C11.3072 21.75 10.6322 21.6779 9.98156 21.541L9.67269 23.0088C10.4242 23.167 11.2028 23.25 12 23.25V21.75ZM2.25 12C2.25 10.6949 2.50601 9.45149 2.96986 8.31584L1.58122 7.74867C1.0451 9.06127 0.75 10.4971 0.75 12H2.25ZM9.98156 21.541C6.21724 20.7489 3.25112 17.7827 2.45903 14.0184L0.991173 14.3273C1.90571 18.6735 5.32647 22.0943 9.67269 23.0088L9.98156 21.541ZM2.45903 14.0184C2.32213 13.3678 2.25 12.6927 2.25 12H0.75C0.75 12.7972 0.83303 13.5757 0.991173 14.3273L2.45903 14.0184ZM2.96986 8.31584C4.17707 5.36016 6.79381 3.1298 9.98155 2.45903L9.67269 0.991173C5.99032 1.76602 2.97369 4.33941 1.58122 7.74867L2.96986 8.31584ZM9.98155 2.45903C10.6322 2.32213 11.3072 2.25 12 2.25V0.75C11.2028 0.75 10.4242 0.83303 9.67269 0.991173L9.98155 2.45903ZM12 2.25C12.6927 2.25 13.3678 2.32213 14.0184 2.45903L14.3273 0.991174C13.5757 0.833031 12.7972 0.75 12 0.75V2.25ZM14.0184 2.45903C17.2071 3.13 19.8245 5.3615 21.0312 8.3185L22.42 7.75174C21.0281 4.34096 18.0108 1.76625 14.3273 0.991174L14.0184 2.45903ZM13.4584 1.95309C13.7482 2.8614 14.8215 6.35621 15.2615 9.5682L16.7476 9.36461C16.289 6.01664 15.1813 2.41835 14.8874 1.49712L13.4584 1.95309ZM15.2615 9.5682C15.3795 10.4292 15.45 11.2568 15.45 12L16.95 12C16.95 11.1681 16.8715 10.269 16.7476 9.36461L15.2615 9.5682ZM21.4222 7.35242C20.2692 7.70212 18.1033 8.3164 15.8685 8.72886L16.1407 10.204C18.4546 9.7769 20.6809 9.14473 21.8576 8.78785L21.4222 7.35242ZM15.8685 8.72886C14.5129 8.97904 13.1579 9.15 12 9.15L12 10.65C13.2874 10.65 14.743 10.4619 16.1407 10.204L15.8685 8.72886ZM15.45 12C15.45 13.1009 15.2954 14.3808 15.0647 15.671L16.5413 15.935C16.7797 14.6019 16.95 13.2252 16.95 12L15.45 12ZM15.0647 15.671C14.5591 18.4992 13.7097 21.2593 13.4584 22.0469L14.8874 22.5029C15.145 21.6956 16.0181 18.8613 16.5413 15.935L15.0647 15.671ZM22.0469 13.4584C21.2593 13.7097 18.4992 14.5591 15.671 15.0647L15.935 16.5413C18.8613 16.0181 21.6956 15.145 22.5029 14.8874L22.0469 13.4584ZM15.671 15.0647C14.3808 15.2954 13.1009 15.45 12 15.45L12 16.95C13.2252 16.95 14.6019 16.7797 15.935 16.5413L15.671 15.0647ZM12 15.45C10.8991 15.45 9.61923 15.2954 8.32897 15.0647L8.06496 16.5413C9.39807 16.7797 10.7748 16.95 12 16.95L12 15.45ZM8.32897 15.0647C5.50076 14.5591 2.74066 13.7097 1.95309 13.4584L1.49712 14.8874C2.30437 15.145 5.13873 16.0181 8.06496 16.5413L8.32897 15.0647ZM7.05 12C7.05 13.2252 7.22032 14.6019 7.45867 15.935L8.93526 15.671C8.70456 14.3808 8.55 13.1009 8.55 12L7.05 12ZM7.45867 15.935C7.98188 18.8613 8.85504 21.6956 9.11261 22.5029L10.5416 22.0469C10.2903 21.2593 9.44094 18.4992 8.93526 15.671L7.45867 15.935ZM9.11261 1.49712C8.81867 2.41835 7.711 6.01664 7.25235 9.36461L8.73846 9.5682C9.17849 6.35621 10.2518 2.8614 10.5416 1.95309L9.11261 1.49712ZM7.25235 9.36461C7.12846 10.269 7.05 11.1681 7.05 12L8.55 12C8.55 11.2568 8.62052 10.4292 8.73846 9.5682L7.25235 9.36461ZM12 9.15C10.8421 9.15 9.4871 8.97904 8.13152 8.72886L7.85929 10.204C9.25697 10.4619 10.7126 10.65 12 10.65L12 9.15ZM8.13152 8.72886C5.89586 8.31625 3.72921 7.70168 2.57657 7.35205L2.14116 8.78747C3.3175 9.14428 5.54457 9.77675 7.85929 10.204L8.13152 8.72886ZM21.38 7.3695C21.3919 7.3633 21.4065 7.35719 21.4222 7.35242L21.8576 8.78785C21.933 8.76498 22.0039 8.73569 22.0712 8.70074L21.38 7.3695ZM1.88425 8.67209C1.96322 8.72038 2.04888 8.75948 2.14116 8.78747L2.57657 7.35205C2.60983 7.36214 2.64048 7.3763 2.66683 7.39242L1.88425 8.67209Z"/>
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

async def generate_pdf(url, pdf_path, scale):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': pdf_path, 'format': 'A4', 'scale': scale, 'printBackground':True})
    await browser.close()

def gen_pdf_all_theme(text, scale=0.75):
    folder = 'pdf_render'
    base_name = f'{text["language"]}_CV'
    html_light= f'z_{base_name}.html'
    html_dark = f'z_{base_name}_dark.html'
    pdf_light = f'{folder}/{base_name}.pdf'
    pdf_dark  = f'{folder}/{base_name}_dark.pdf'
    local_host = 'http://127.0.0.1:5500'
    save_to_file(gen(text, False, True), html_light) # saving to file cause direct html leads to artifacts
    save_to_file(gen(text, False, True, True), html_dark)
    asyncio.get_event_loop().run_until_complete(generate_pdf(f'{local_host}/{html_light}', pdf_light, scale))
    asyncio.get_event_loop().run_until_complete(generate_pdf(f'{local_host}/{html_dark}', pdf_dark, scale))
    os.remove(ABS_PATH / html_light)
    os.remove(ABS_PATH / html_dark)

def main():
    save_to_file(gen(text_french.TEXT, False), 'french-cv.html')
    gen_pdf_all_theme(text_french.TEXT)
    save_to_file(gen(text_english.TEXT, True), 'index.html')
    gen_pdf_all_theme(text_english.TEXT)

if __name__ == "__main__" :
    main()
