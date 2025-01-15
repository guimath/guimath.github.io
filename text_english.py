# Basically json but directly in python just cause 
TEXT = {
    'language': 'english',
    'job_title' : 'Embedded systems engineer',
    'age' : '24 years old',
    'education_title': 'Education',
    'education_lst' :[
        {
            'title'     :'MSc in Computer Science', 
            'date'      :'From 2023 to 2024',
            'sub_title' :'National University of Singapore', 
            'location'  :'Singapore', 
            'desc'      :['Master of Science by Research in Computer Science'],
        },
        {
            'title'     :'Engineering Diploma', 
            'date'      :'From 2020 to 2023',
            'sub_title' :'Télécom Paris', 
            'location'  :'Palaiseau, France', 
            'desc'      :['Engineering Diploma in Embedded Systems work-study programme'],
        },
        {
            'title'     :'University Diploma of Technology GEII', 
            'date'      :'From 2018 to 2020',
            'sub_title' :'IUT Cachan', 
            'location'  :'Cachan, France', 
            'desc'      :['Electrical Engineering and industrial Computing Diploma'],
        },
        # {
        #     'title'     :'High School Diploma', 
        #     'date'      :'From 2015 to 2018',
        #     'sub_title' :'Jean Baptiste Say', 
        #     'location'  :'Paris, France', 
        #     'desc'      :['High School Diploma in Engineering Sciences'],
        # },
    ],
    'proj_title': 'Tutored Projects',
    'proj_lst' :[
        {
            'title'     :'Master Thesis', 
            'date'      :'2024',
            'sub_title' :'Leveraging Rust for real time low computational robotics', 
            'location'  :'', 
            'desc'      :[
                'Implementation of an optimization based Inverse Kinematics solver and RTT motion planner',
                'Evaluated through simulation and in real-world conditions for a standard grasp motion'
            ],
            'links': [{
                'type': '[github]',
                'url': 'https://github.com/guimath/relaxed_ik_pp'
            },
            {
                'type': '[pdf]',
                'url': 'https://github.com/guimath/relaxed_ik_pp/blob/ranged-ik/master_thesis.pdf'
            }
            ],
        },
        {
            'title'     :'Final Year Project', 
            'date'      :'2023',
            'sub_title' :'SoC Configurable Signal Generator', 
            'location'  :'', 
            'desc'      :[
                'Development of an AXI4 configurable FPGA IP for generating a signal (square or sinewave)',
                'Management of the two CPU cores independently for external ethernet communication and internal real time computing'
            ],
            'links':[{
                'type': '[github]',
                'url': 'https://github.com/guimath/PrimProj'
            }]
        },
        {
            'title'     :'Second Year Project', 
            'date'      :'2022',
            'sub_title' :'Infrastructure and Demonstrations around the LoRa protocol', 
            'location'  :'', 
            'desc'      : [
                'Testing the LoRa communication protocol, gateway registering and deployment',
                'LoRa project guide with examples for multiple situations',
            ],
        },
        {
            'title'     :'Final IUT Project', 
            'date'      :'2020',
            'sub_title' :'France Robotics Cup (National competition)', 
            'location'  :'', 
            'desc'      : [
                'Programming of a Bluetooth debugging solution in C++',
                'Development of an intelligent color sensor (sensor testing, C++ programming, PCB design)',
            ],
        },
    ],
    
    'work_title': 'Work Experience',
    'work_lst' :[
        {
            'title'     :'Apprenticeship', 
            'date'      :'From 2021 to 2023',
            'sub_title' :'Safran Electronics & Defense', 
            'location'  :'Massy, France', 
            'desc'      :['Development of a sensor prototype',
                          'Embedded Software (C), GUI (Python), Communication protocol',
                          'SoC architecture and PCB design'],
        },
        {
            'title'     :'Internship', 
            'date'      :'From April to July 2020',
            'sub_title' :'C2N laboratory', 
            'location'  :'Palaiseau, France', 
            'desc'      :['PCB design for a 3 omega sensor prototype',],
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
                '<strong>Software</strong>  : Rust, Python, C, C++',
                '<strong>HDL</strong>  : Verilog, System Verilog',
                '<strong>Web Dev</strong>: HTML5, CSS3'
            ],
        },
        {
            'name' : 'Operating Systems',
            'desc' : ['<strong>Linux</strong> Ubuntu & Debian',
                      '<strong>Windows</strong> 10 & 11'],
        },
        {
            'name' : 'Development environment',
            'desc' : ['VS code, Vivado/Vitis, µVision, Qt Creator'],
        },
    ],

    'interest_title': 'Interests',
    'interest_lst' : [
        {
            'name' : 'Competitive Programming',
            'desc' : [
                'Participated in the regional selection phase for ICPC: SWERC 2023 in Milan',
            ],
        },
        {
            'name' : 'Climbing',
            'desc' : [
                '3 years of regular practice (mainly bouldering).',
                '6A / V6 level, multiple cliff climbing experiences'
            ],
        },
        {
            'name' : 'Swimming',
            'desc' : ['Weekly training'],
        },
        # {
        #     'name' : 'Handiwork, DIY',
        #     'desc' : ['Building PCs, Ceiling light design and wiring'],
        # },
        {
            'name' : 'Diving',
            'desc' : ['Open water certification for both scuba and freedive'],
        },
        {
            'name' : 'Photography',
            'desc' : ['Amateur photographer, mainly landscapes and wildlife, using a Fujifilm XT200 ',
                      '<a href="https://www.instagram.com/guilhemphotography/" target="_blank">[some of my photos]</a>']
        }
    ],
}