TEXT = {
    'theme_button':'Thème sombre',
    'job_title' : 'Ingénieur logiciel embarqué',
    'age' : '24 ans',
    'education_title': 'Formation',
    'education_lst' : [
        {
            'title'     :'MSc en Informatique', 
            'date'      :'De 2023 à 2024',
            'sub_title' :'National University of Singapore', 
            'location'  :'Singapour', 
            'desc'      :['Master of Science en Double diplôme'],
        },
        {
            'title'     :'Diplôme d\'ingénieur', 
            'date'      :'De 2020 à 2023',
            'sub_title' :'Télécom Paris', 
            'location'  :'Palaiseau, France', 
            'desc'      :['Diplôme d\'ingénieur en systèmes embarqués en alternance'],
        },
        {
            'title'     :'Diplôme universitaire de technologie GEII', 
            'date'      :'De 2018 à 2020',
            'sub_title' :'IUT Cachan', 
            'location'  :'Cachan, France', 
            'desc'      :['Diplôme en génie électrique et informatique industrielle'],
        },
        # {
        #     'title'     :'Baccalauréat', 
        #     'date'      :'De 2015 à 2018',
        #     'sub_title' :'Jean Baptiste Say', 
        #     'location'  :'Paris, France', 
        #     'desc'      :[
        #         'Bac en Sciences et Technologies de l\'Ingénieur',
        #     ],
        # },
    ],
    'proj_title': 'Projets universitaires',
    'proj_lst' : [
        {
            'title'     :'Thèse de Master', 
            'date'      :'2024',
            'sub_title' :'Systèmes robotiques temps réel optimisés en Rust', 
            'location'  :'', 
            'desc'      :[
                'Mise en œuvre d\'un solveur de cinématique inverse (IK) basé sur l\'optimisation et d\'un planificateur de mouvement basé RTT',
                'Évaluation par simulation et en conditions réelles pour un mouvement de préhension standard'
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
            'title'     :'Projet de fin d\'étude', 
            'date'      :'2023',
            'sub_title' :'Générateur de signal configurable SoC', 
            'location'  :'', 
            'desc'      :[
                'Développement d\'une IP FPGA configurable via AXI4 générant un signal (carré ou sinusoïdal)',
                'Gestion des deux cœurs CPU indépendamment pour la communication Ethernet externe et le calcul interne en temps réel'
            ],
            'links':[{
                'type': '[github]',
                'url': 'https://github.com/guimath/PrimProj'
            }]
        },
        {
            'title'     :'Projet de deuxième année', 
            'date'      :'2022',
            'sub_title' :'Infrastructure et démonstrations autour du protocole LoRa', 
            'location'  :'', 
            'desc'      :[
                'Test du protocole de communication LoRa, enregistrement et déploiement des passerelles',
                'Guide de projet LoRa avec des exemples pour plusieurs situations',
            ],
        },
        {
            'title'     :'Projet final IUT', 
            'date'      :'2020',
            'sub_title' :'Coupe de France de la Robotique (compétition nationale)', 
            'location'  :'', 
            'desc'      :[
                'Programmation d\'une solution de débogage Bluetooth en C++',
                'Développement d\'un capteur de couleur intelligent (test de capteur, programmation en C++, conception de circuit imprimé)'
            ],
        }
    ],

    'work_title': 'Expérience professionnelle',
    'work_lst' : [
        {
            'title'     :'Ingénieur alternant prototypage', 
            'date'      :'De 2021 à 2023',
            'sub_title' :'Safran Electronics & Defense', 
            'location'  :'Massy, France', 
            'desc'      :['Logiciel embarqué, développement d\'IHM, architecture SoC, conception de circuit imprimé'],
        },
        {
            'title'     :'Stage technicien électronique', 
            'date'      :'De avril à juillet 2020',
            'sub_title' :'Laboratoire C2N', 
            'location'  :'Palaiseau, France', 
            'desc'      :[
                'Prototype de capteur 3 omega',
            ],
        },
    ],

    'language_title': 'Langues',
    'languages_lst' : [
        # {
        #     'name' : 'Français',
        #     'level': 100,
        #     'desc' : ['Courant (langue maternelle)'],
        # },
        {
            'name' : 'Anglais',
            'level': 90,
            'desc' : [
                'Courant et certifié niveau technique C1',
                'TOEIC : 985 | Linguaskill : 180+'
            ]
        },
        {
            'name' : 'Espagnol',
            'level': 30,
            'desc' : ['Niveau intermédiaire B1'],
        },
    ],
    'skills_title': 'Compétences',
    'skills_lst' : [
        {
            'name' : 'Langages de programmation',
            'desc' : [
                '<strong>Langages de logiciel</strong>  : Rust, Python, C, C++',
                '<strong>HDL</strong>  : Verilog, System Verilog',
                '<strong>Développement web</strong>: HTML5, CSS3'
            ],
        },
        {
            'name' : 'Systèmes d\'exploitation',
            'desc' : ['Linux Ubuntu & Debian, Windows 10 & 11'],
        },
        {
            'name' : 'Environnements de développement',
            'desc' : ['VS code, Vivado/Vitis, µVision, Qt Creator'],
        },
    ],

    'interest_title': 'Intérêts',
    'interest_lst' : [
        {
            'name' : 'Programmation Competitive',
            'desc' : [
                'Participation à la phase de selection pour l\'ICPC : SWERC 2023 à Milan',
            ],
        },
        {
            'name' : 'Escalade',
            'desc' : [
                '3 ans de pratique régulière (principalement le bloc).',
                'Niveau 6A / V6. Expériences multiples d\'escalade en falaise'
            ],
        },
        {
            'name' : 'Natation',
            'desc' : ['Entraînement hebdomadaire'],
        },
        # {
        #     'name' : 'Travaux manuels, bricolage',
        #     'desc' : ['Construction de PC, conception et câblage de luminaires de plafond'],
        # },
        {
            'name' : 'Plongée',
            'desc' : ['Certification de plongée en bouteille et de plongée en apnée (freedive)'],
        },
        {
            'name' : 'Photographie',
            'desc' : ['Photographe amateur, principalement des paysage, avec un Fujifilm XT200 ',
                      '<a href="https://www.instagram.com/guilhemphotography/" target="_blank">[Quelques-unes de mes photos]</a>']
        }
    ],

}