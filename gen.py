
import os
json = {
    'theme_button':'toggle dark theme',
    'education_title': 'Education',
    'education_lst' :[
        {
        'title'     :'Engineering Diploma', 
        'date'      :'Since 2020',
        'sub_title' :'Télécom ParisTech', 
        'location'  :'Palaiseau, France', 
        'desc'      :['Engineering Diploma in Embedded Systems work-study programme'],
        },
        {
        'title'     :'University Diploma of Technology GEII', 
        'date'      :'From 2018 to 2020',
        'sub_title' :'IUT Cachan', 
        'location'  :'Cachan, France', 
        'desc'      :[
            'Electrical Engineering and industrial Computing Diploma',
            'Ranked 2nd out of 120 students'
        ],
        },
        {
        'title'     :'High School Diploma', 
        'date'      :'From 2015 to 2018',
        'sub_title' :'Jean Baptiste Say', 
        'location'  :'Paris, France', 
        'desc'      :[
            'High School Diploma in Engineering Sciences',
        ],
        },
    ],
    'proj_title': 'Tutored Projects',
    'proj_lst' :[
        {
        'title'     :'Final Year Project', 
        'date'      :'From 2022 to 2023',
        'sub_title' :'SoC Configurable Signal Generator', 
        'location'  :'', 
        'desc'      :[
            'Developement of an FPGA IP configurable via AXI4 generating a signal (square or sinewave)',
            'Management of the two CPU cores independantly for external ethernet communication and internal computing'],
        },
        {
        'title'     :'Second Year Project', 
        'date'      :'2020',
        'sub_title' :'Infrastructure and Demonstrations around the LoRa protocol', 
        'location'  :'', 
        'desc'      :[
            'Testing the LoRa protocol, gateway registering and deployment. LoRa project guide with examples for multiple situations',
        ],
        },
        {
        'title'     :'Final IUT Project', 
        'date'      :'From 2019 to 2020',
        'sub_title' :'France Robotics Cup (National competition)', 
        'location'  :'', 
        'desc'      :[
            'Programming of a Bluetooth debugging solution in C++',
            'Development of an intelligent color sensor (sensor testing, C++ programming, PCB design)',
        ],
        },
    ],
    
    'work_title': 'Work Experience',
    'work_lst' :[
        {
        'title'     :'Apprenticeship', 
        'date'      :'Since 2021',
        'sub_title' :'Safran Electronics & Defense', 
        'location'  :'Massy, France', 
        'desc'      :['Embedded Software, GUI dev, SoC, PCB design'],
        },
        {
        'title'     :'Internship', 
        'date'      :'From April to July 2020',
        'sub_title' :'C2N laboratory', 
        'location'  :'Palaiseau, France', 
        'desc'      :[
            '3 omega sensor prototype',
        ],
        },
    ],

    'language_title': 'Languages',
    'languages_lst' : [
        {
            'name' : 'French',
            'level': 100,
            'desc' : ['Fluent (native tongue)'],
        },
        {
            'name' : 'English',
            'level': 90,
            'desc' : [
                'Fluent and certified technical C1 level',
                'TOEIC : 985 | Linguaskill : 180+'
                ]
        },
        {
            'name' : 'Spanish',
            'level': 30,
            'desc' : ['Intermediate B1 level'],
        },
    ],
    'skills_title': 'Skills',
    'skills_lst' : [
            {
                'name' : 'Programming Languages',
                'desc' : [
                    '<strong>Software Language</strong>  : C, C++, Python, Rust, Java ',
                    '<strong>HDL</strong>  : Verilog, System Verilog',
                    '<strong>Web Dev</strong>: HTML5, CSS3'
                    ],
            },
            {
                'name' : 'Operating Systems',
                'desc' : ['Linux Ubuntu & Debian, Windows 10'],
            },
            {
                'name' : 'Developement environment',
                'desc' : ['VS code, Vivado/Vitis, µVision, MPLAB, Altera, Qt Creator, Eclipse'],
            },
        ],

    'interest_title': 'Interests',
    'interest_lst' : [
            {
                'name' : 'Climbing',
                'desc' : [
                    '3 years of regular practice (mainly bouldering).',
                    '6A / V6 level Multiple cliff climbing experiences'
                    ],
            },
            {
                'name' : 'Swimming',
                'desc' : ['Weekly training'],
            },
            {
                'name' : 'Handiwork, DIY',
                'desc' : ['Building PCs, Ceiling light design and wiring'],
            },
        ],
}

def event(date, title, sub_title, location, desc, space= '                '):
    out =  f'{space}<li class="event" data-date="{date}">\n'
    out += f'{space}    <h3>{title}</h3>\n'
    out += f'{space}    <p><strong>{sub_title}</strong><i> {location}</i></p>\n'
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
        out += event(
            element['date'], 
            element['title'], 
            element['sub_title'], 
            element['location'], 
            element['desc'],
            space + '    ')
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

html = '''
<head>
    <title>guimath</title>
    <link href="light_theme.css" rel="stylesheet" id="theme-link">
</head>
<body>
'''
html += f'    <button onclick="lightMode()">{json["theme_button"]}</button>'
    
html += '''
    <script>
        const theme = document.querySelector("#theme-link");
        function lightMode() {
            if (theme.getAttribute("href") == "light_theme.css") {
                theme.href = "dark_theme.css";
            } else {
                theme.href = "light_theme.css";
            }
        }
    </script>
'''


html += '    <h1>Guilhem Mathieux (WIP)</h1>\n'#TMP

html += '    <div style="display: flex;">\n'
html += '        <div class="col1">\n'
html += timeline(json['education_title'], json['education_lst'], True)
html += timeline(json['proj_title'], json['proj_lst'], False)
html += timeline(json['work_title'], json['work_lst'], False)
html += '        </div>\n'
html += '        <div class="col2">\n'

html += generic_lst(json['language_title'], json['languages_lst'], True)
html += generic_lst(json['skills_title'], json['skills_lst'], False)
html += generic_lst(json['interest_title'], json['interest_lst'], False)
html += '        </div>\n'
html += '    </div>\n'


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
save_to_file(html, 'index.html')
