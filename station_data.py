#해당 시뮬레이션에서 제공하는 역들에 대한 정보
station = {
    "한대앞": {
        "line": [4,"수인분당"],
        "passenger" : 17811,
        "pos" : (50,670),
        "waiting" : 0,
        "name" : "Handaeap",
        "connected" : ["상록수"]
    }, "상록수": {
        "line": [4],
        "passenger" : 41030,
        "pos" : (100,670),
        "waiting" : 0,
        "name" : "Sangnoksu", 
        "connected" : ["한대앞","반월"]
    }, "반월": {
        "line": [4],
        "passenger" : 9397,
        "pos" : (150,670),
        "waiting" : 0,
        "name" : "Banwol", 
        "connected" : ["상록수", "대야미"]
    }, "대야미": {
        "line": [4],
        "passenger" : 9082,
        "pos" : (200,670),
        "waiting" : 0,
        "name" : "Daeyami", 
        "connected" : ["반월", "수리산"]
    }, "수리산": {
        "line": [4],
        "passenger" : 8212,
        "pos" : (250,670),
        "waiting" : 0,
        "name" : "Surisan", 
        "connected" : ["대야미", "산본"]
    }, "산본": {
        "line": [4],
        "passenger" : 37994,
        "pos" : (300,670),
        "waiting" : 0,
        "name" : "Sanbon", 
        "connected" : ["수리산", "금정"]
    }, "금정": {
        "line": [1,4],
        "passenger" : 54239,
        "pos" : (350,670),
        "waiting" : 0,
        "name" : "Geumjeong", 
        "connected" : ["산본","범계","군포","명학"]
    }, "범계": {
        "line": [4],
        "passenger" : 58806,
        "pos" : (400,670),
        "waiting" : 0,
        "name" : "Beomgye", 
        "connected" : ["금정","평촌"]
    }, "평촌": {
        "line": [4],
        "passenger" : 34882,
        "pos" : (450,640),
        "waiting" : 0,
        "name" : "Pyeongchon", 
        "connected" : ["범계","인덕원"]
    }, "인덕원": {
        "line": [4],
        "passenger" : 51897,
        "pos" : (500,610),
        "waiting" : 0,
        "name" : "Indeogwon", 
        "connected" : ["평촌","정부과천청사"]
    }, "정부과천청사": {
        "line": [4],
        "passenger" : 23813,
        "pos" : (550,580),
        "waiting" : 0,
        "name" : "Government Complex Gwacheon", 
        "connected" : ["인덕원","과천"]
    }, "과천": {
        "line": [4],
        "passenger" : 10114,
        "pos" : (600,550),
        "waiting" : 0,
        "name" : "Gwacheon", 
        "connected" : ["정부과천청사","대공원"]
    }, "대공원": {
        "line": [4],
        "passenger" : 10533,
        "pos" : (650,520),
        "waiting" : 0,
        "name" : "Seoul Grand Park", 
        "connected" : ["과천","경마공원"]
    }, "경마공원": {
        "line": [4],
        "passenger" : 13762,
        "pos" : (700,490),
        "waiting" : 0,
        "name" : "Seoul Racecourse Park", 
        "connected" : ["대공원","선바위"]
    }, "선바위": {
        "line": [4],
        "passenger" : 17108,
        "pos" : (750,460),
        "waiting" : 0,
        "name" : "Seonbawi", 
        "connected" : ["경마공원","남태령"]
    }, "남태령": {
        "line": [4],
        "passenger" : 4713+1000,
        "pos" : (750,410),
        "waiting" : 0,
        "name" : "Namtaeryeong", 
        "connected" : ["선바위","사당"]
    }, "사당": {
        "line": [2,4],
        "passenger" : 148872,
        "pos" : (750,360),
        "waiting" : 0,
        "name" : "Sadang", 
        "connected" : ["남태령","이수","낙성대","방배"]
    }, "이수": {
        "line": [4,7],
        "passenger" : 79657,
        "pos" : (750,310),
        "waiting" : 0,
        "name" : "Isu", 
        "connected" : ["사당","동작","남성","내방"]
    }, "동작": {
        "line": [4,9],
        "passenger" : 10516,
        "pos" : (750,260),
        "waiting" : 0,
        "name" : "Dongjak", 
        "connected" : ["이수","이촌","흑석","구반포"]
    }, "이촌": {
        "line": [4,"경의중앙"],
        "passenger" : 30131,
        "pos" : (700,220),
        "waiting" : 0,
        "name" : "Ichon", 
        "connected" : ["동작","신용산"]
    }, "신용산": {
        "line": [4],
        "passenger" : 33699,
        "pos" : (650,180),
        "waiting" : 0,
        "name" : "Shinyongsan", 
        "connected" : ["이촌","삼각지"]
    }, "삼각지": {
        "line": [4,6],
        "passenger" : 23666,
        "pos" : (590,150),
        "waiting" : 0,
        "name" : "Samgakji", 
        "connected" : ["신용산","숙대입구"]
    }, "숙대입구": {
        "line": [4],
        "passenger" : 32465,
        "pos" : (540,120),
        "waiting" : 0,
        "name" : "Sookdae",
        "connected" : ["삼각지","서울역"]
    }, "서울역": {
        "line": [1,4,"경인선","공항철도", "경의중앙"],
        "passenger" : 192179,
        "pos" : (490,90),
        "waiting" : 0,
        "name" : "Seoul", 
        "connected" : ["숙대입구","회현","남영","시청"]
    }, "회현": {
        "line": [4],
        "passenger" : 62950,
        "pos" : (540,60),
        "waiting" : 0,
        "name" : "Hoehyeon", 
        "connected" : ["서울역","명동"]
    }, "명동": {
        "line": [4],
        "passenger" : 80040,
        "pos" : (590,60),
        "waiting" : 0,
        "name" : "Myeongdong", 
        "connected" : ["회현","충무로"]
    }, "충무로": {
        "line": [3,4],
        "passenger" : 63611,
        "pos" : (640,30),
        "waiting" : 0,
        "name" : "Chungmuro", 
        "connected" : ["명동","동대문역사문화공원","동대입구","을지로3가"]
    }, "동대문역사문화공원": {
        "line": [2,4,5],
        "passenger" : 91773,
        "pos" : (690,30),
        "waiting" : 0,
        "name" : "DPP",
        "connected" : ["충무로","동대문","을지로4가","신당"]
    }, "동대문": {
        "line": [1,4,"경인선"],
        "passenger" : 81168,
        "pos" : (690,10),
        "waiting" : 0,
        "name" : "Dongdaemun",
        "connected" : ["동대문역사문화공원"]
    }, "방배": {
        "line": [2],
        "passenger" : 40100,
        "pos" : (800,360),
        "waiting" : 0,
        "name" : "Bangbae",
        "connected" : ["사당","서초"]
    }, "서초": {
        "line": [2],
        "passenger" : 46877,
        "pos" : (850,360),
        "waiting" : 0,
        "name" : "Seocho",
        "connected" : ["방배","교대"]
    }, "교대": {
        "line": [2,3],
        "passenger" : 102287,
        "pos" : (900,360),
        "waiting" : 0,
        "name" : "Gyeodae",
        "connected" : ["서초","강남","고속터미널","남부터미널"]
    }, "강남": {
        "line": [2,"신분당"],
        "passenger" : 237734,
        "pos" : (950,360),
        "waiting" : 0,
        "name" : "Gangnam",
        "connected" : ["교대","역삼"]
    }, "역삼": {
        "line": [2],
        "passenger" : 99387,
        "pos" : (1000,360),
        "waiting" : 0,
        "name" : "Yeoksam",
        "connected" : ["강남","선릉"]
    }, "선릉": {
        "line": [2,"수인분당"],
        "passenger" : 148758,
        "pos" : (1050,360),
        "waiting" : 0,
        "name" : "Seolleung",
        "connected" : ["역삼","삼성","한티","선정릉"]
    }, "삼성": {
        "line": [2],
        "passenger" : 121184,
        "pos" : (1100,360),
        "waiting" : 0,
        "name" : "Samseong",
        "connected" : ["선릉","종합운동장"]
    }, "종합운동장": {
        "line": [2,9],
        "passenger" : 37279,
        "pos" : (1150,360),
        "waiting" : 0,
        "name" : "Sports Complex",
        "connected" : ["삼성","잠실새내","봉은사","삼전"]
    }, "잠실새내": {
        "line": [2],
        "passenger" : 50061,
        "pos" : (1200,330),
        "waiting" : 0,
        "name" : "Jamsilsaenae",
        "connected" : ["종합운동장","잠실"]
    }, "잠실": {
        "line": [2,8],
        "passenger" : 205623,
        "pos" : (1250,300),
        "waiting" : 0,
        "name" : "Jamsil",
        "connected" : ["잠실새내","잠실나루"]
    }, "잠실나루": {
        "line": [2],
        "passenger" : 31988,
        "pos" : (1250,250),
        "waiting" : 0,
        "name" : "Jamsillaru",
        "connected" : ["잠실","강변"]
    }, "강변": {
        "line": [2],
        "passenger" : 90150,
        "pos" : (1250,200),
        "waiting" : 0,
        "name" : "Gangbyeon",
        "connected" : ["잠실나루","구의"]
    }, "구의": {
        "line": [2],
        "passenger" : 47909,
        "pos" : (1250,150),
        "waiting" : 0,
        "name" : "Guui",
        "connected" : ["강변","건대입구"]
    }, "건대입구": {
        "line": [2,7],
        "passenger" : 127066,
        "pos" : (1250,100),
        "waiting" : 0,
        "name" : "Konkuk Univ.",
        "connected" : ["구의","성수","뚝섬유원지","어린이대공원"]
    }, "성수": {
        "line": [2,"성수지선"],
        "passenger" : 60192,
        "pos" : (1190,70),
        "waiting" : 0,
        "name" : "Seongsu",
        "connected" : ["건대입구","뚝섬"]
    }, "뚝섬": {
        "line": [2],
        "passenger" : 39054,
        "pos" : (1130,40),
        "waiting" : 0,
        "name" : "Ttukseom",
        "connected" : ["성수","한양대"]
    }, "낙성대": {
        "line": [2],
        "passenger" : 59167,
        "pos" : (700,360),
        "waiting" : 0,
        "name" : "Nakseongdae",
        "connected" : ["서울대입구","사당"]
    }, "서울대입구": {
        "line": [2],
        "passenger" : 105144,
        "pos" : (650,360),
        "waiting" : 0,
        "name" : "SeoulUniv",
        "connected" : ["봉천","낙성대"]
    }, "봉천": {
        "line": [2],
        "passenger" : 48608,
        "pos" : (600,360),
        "waiting" : 0,
        "name" : "Bongcheon",
        "connected" : ["신림","서울대입구"]
    }, "신림": {
        "line": [2],
        "passenger" : 139189,
        "pos" : (550,360),
        "waiting" : 0,
        "name" : "Shillim",
        "connected" : ["신대방","봉천"]
    }, "신대방": {
        "line": [2],
        "passenger" : 56960,
        "pos" : (500,360),
        "waiting" : 0,
        "name" : "Shindaebang",
        "connected" : ["구로디지털단지","신림"]
    }, "구로디지털단지": {
        "line": [2],
        "passenger" : 126035,
        "pos" : (450,360),
        "waiting" : 0,
        "name" : "GuroDigiCom",
        "connected" : ["대림","신대방"]
    }, "대림": {
        "line": [2,7],
        "passenger" : 81233,
        "pos" : (400,360),
        "waiting" : 0,
        "name" : "Daerim",
        "connected" : ["신도림","구로디지털단지","남구로","신풍"]
    }, "신도림": {
        "line": [1,2,"신정지선","경인선"],
        "passenger" : 126407,
        "pos" : (350,360),
        "waiting" : 0,
        "name" : "Shindorim",
        "connected" : ["문래","대림","구로","영등포"]
    }, "문래": {
        "line": [2],
        "passenger" : 40449,
        "pos" : (300,330),
        "waiting" : 0,
        "name" : "Mullae",
        "connected" : ["영등포구청","신도림"]
    }, "영등포구청": {
        "line": [2,5],
        "passenger" : 52092,
        "pos" : (250,330),
        "waiting" : 0,
        "name" : "YDP-Gu Off.",
        "connected" : ["문래","당산"]
    }, "당산": {
        "line": [2,9],
        "passenger" : 83903,
        "pos" : (200,300),
        "waiting" : 0,
        "name" : "Dangsan",
        "connected" : ["합정","영등포구청","선유도","국회의사당"]
    }, "합정": {
        "line": [2,6],
        "passenger" : 100127,
        "pos" : (200,250),
        "waiting" : 0,
        "name" : "Hapjeong",
        "connected" : ["홍대입구","당산"]
    }, "홍대입구": {
        "line": [2,"경의중앙","공항철도"],
        "passenger" : 205323,
        "pos" : (200,200),
        "waiting" : 0,
        "name" : "Hongik Univ.",
        "connected" : ["신촌","합정"]
    }, "신촌": {
        "line": [2],
        "passenger" : 95972,
        "pos" : (250,170),
        "waiting" : 0,
        "name" : "Sinchon",
        "connected" : ["이대","홍대입구"]
    }, "이대": {
        "line": [2],
        "passenger" : 41008,
        "pos" : (300,140),
        "waiting" : 0,
        "name" : "Ewha Univ.",
        "connected" : ["아현","신촌"]
    }, "아현": {
        "line": [2],
        "passenger" : 21477,
        "pos" : (350,110),
        "waiting" : 0,
        "name" : "Ahyeon",
        "connected" : ["충정로","이대"]
    }, "충정로": {
        "line": [2,5],
        "passenger" : 31686,
        "pos" : (420,70),
        "waiting" : 0,
        "name" : "ChungJno",
        "connected" : ["시청","아현"]
    }, "을지로입구": {
        "line": [2],
        "passenger" : 101199,
        "pos" : (540,40),
        "waiting" : 0,
        "name" : "Euljiro",
        "connected" : ["시청","을지로3가"]
    }, "을지로4가": {
        "line": [2,5],
        "passenger" : 35928,
        "pos" : (640,10),
        "waiting" : 0,
        "name" : "Euljiro 4",
        "connected" : ["을지로3가","동대문역사문화공원"]
    }, "신당": {
        "line": [2,6],
        "passenger" : 48999,
        "pos" : (770,10),
        "waiting" : 0,
        "name" : "Sindang",
        "connected" : ["상왕십리","동대문역사문화공원"]
    }, "상왕십리": {
        "line": [2],
        "passenger" : 28476,
        "pos" : (870,10),
        "waiting" : 0,
        "name" : "SWsimni",
        "connected" : ["왕십리","신당"]
    }, "왕십리": {
        "line": [2,5,"경의중앙","수인분당"],
        "passenger" : 86352,
        "pos" : (970,40),
        "waiting" : 0,
        "name" : "Wangsimni",
        "connected" : ["한양대","상왕십리","서울숲","청량리"]
    }, "한양대": {
        "line": [2],
        "passenger" : 23819,
        "pos" : (1050,40),
        "waiting" : 0,
        "name" : "Hanyang Univ.",
        "connected" : ["왕십리","뚝섬"]
    }, "선유도": {
        "line": [9],
        "passenger" : 13377,
        "pos" : (150,300),
        "waiting" : 0,
        "name" : "Seonyudo",
        "connected" : ["신목동","당산"]
    }, "신목동": {
        "line": [9],
        "passenger" : 7570,
        "pos" : (100,300),
        "waiting" : 0,
        "name" : "Shinmokdong",
        "connected" : ["염창","선유도"]
    }, "염창": {
        "line": [9],
        "passenger" : 33295,
        "pos" : (50,300),
        "waiting" : 0,
        "name" : "Yeomchang",
        "connected" : ["신목동"]
    }, "국회의사당": {
        "line": [9],
        "passenger" : 31983,
        "pos" : (270,270),
        "waiting" : 0,
        "name" : "Assembly",
        "connected" : ["당산","여의도"]
    }, "여의도": {
        "line": [5,9],
        "passenger" : 92136,
        "pos" : (340,240),
        "waiting" : 0,
        "name" : "Yeouido",
        "connected" : ["국회의사당","샛강"]
    }, "샛강": {
        "line": [9],
        "passenger" : 10274,
        "pos" : (420,240),
        "waiting" : 0,
        "name" : "Saetgang",
        "connected" : ["여의도","노량진"]
    }, "노량진": {
        "line": [1,9,"경인선"],
        "passenger" : 107065,
        "pos" : (490,240),
        "waiting" : 0,
        "name" : "Noryangjin",
        "connected" : ["샛강","노들","대방","용산"]
    }, "노들": {
        "line": [9],
        "passenger" : 8780,
        "pos" : (570,240),
        "waiting" : 0,
        "name" : "Nodeul",
        "connected" : ["노량진","흑석"]
    }, "흑석": {
        "line": [9],
        "passenger" : 20442,
        "pos" : (660,260),
        "waiting" : 0,
        "name" : "Heukseok",
        "connected" : ["노들","동작"]
    }, "구반포": {
        "line": [9],
        "passenger" : 6414,
        "pos" : (790,260),
        "waiting" : 0,
        "name" : "Guban",
        "connected" : ["동작","신반포"]
    }, "신반포": {
        "line": [9],
        "passenger" : 6363,
        "pos" : (830,260),
        "waiting" : 0,
        "name" : "Sinban",
        "connected" : ["구반포","고속터미널"]
    }, "고속터미널": {
        "line": [3,7,9],
        "passenger" : 196715,
        "pos" : (870,260),
        "waiting" : 0,
        "name" : "BusTerm",
        "connected" : ["신반포","사평","내방","반포","잠원","교대"]
    }, "사평": {
        "line": [9],
        "passenger" : 6326,
        "pos" : (910,290),
        "waiting" : 0,
        "name" : "Sapyeong",
        "connected" : ["고속터미널","신논현"]
    }, "신논현": {
        "line": [9],
        "passenger" : 66919,
        "pos" : (950,290),
        "waiting" : 0,
        "name" : "Sinnonhyeon",
        "connected" : ["사평","언주"]
    }, "언주": {
        "line": [9],
        "passenger" : 17616,
        "pos" : (990,290),
        "waiting" : 0,
        "name" : "Eonju",
        "connected" : ["신논현","선정릉"]
    }, "선정릉": {
        "line": [9,"수인분당"],
        "passenger" : 33589,
        "pos" : (1030,290),
        "waiting" : 0,
        "name" : "SJ-neung",
        "connected" : ["언주","삼성중앙","선릉","강남구청"]
    }, "삼성중앙": {
        "line": [9],
        "passenger" : 11564,
        "pos" : (1070,290),
        "waiting" : 0,
        "name" : "Samseong Jungang",
        "connected" : ["선정릉","봉은사"]
    }, "봉은사": {
        "line": [9],
        "passenger" : 35975,
        "pos" : (1110,320),
        "waiting" : 0,
        "name" : "Bongeunsa",
        "connected" : ["삼성중앙","종합운동장"]
    }, "삼전": {
        "line": [9],
        "passenger" : 10571,
        "pos" : (1200,360),
        "waiting" : 0,
        "name" : "Samjeon",
        "connected" : ["종합운동장","석촌고분"]
    }, "석촌고분": {
        "line": [9],
        "passenger" : 9443,
        "pos" : (1250,360),
        "waiting" : 0,
        "name" : "Gobun",
        "connected" : ["삼전","석촌"]
    }, "석촌": {
        "line": [8,9],
        "passenger" : 29384,
        "pos" : (1300,360),
        "waiting" : 0,
        "name" : "Seokchon",
        "connected" : ["석촌고분","송파나루"]
    }, "송파나루": {
        "line": [9],
        "passenger" : 7644,
        "pos" : (1350,360),
        "waiting" : 0,
        "name" : "Songpanaru",
        "connected" : ["석촌","한성백제"]
    }, "한성백제": {
        "line": [9],
        "passenger" : 4152+1300,
        "pos" : (1400,360),
        "waiting" : 0,
        "name" : "Baekje",
        "connected" : ["송파나루","올림픽공원"]
    }, "올림픽공원": {
        "line": [5,9],
        "passenger" : 25188,
        "pos" : (1450,360),
        "waiting" : 0,
        "name" : "Olympic",
        "connected" : ["한성백제"]
    }, "신풍": {
        "line": [7],
        "passenger" : 23600,
        "pos" : (450,330),
        "waiting" : 0,
        "name" : "Sinpung",
        "connected" : ["대림","보라매"]
    }, "보라매": {
        "line": [7],
        "passenger" : 19546,
        "pos" : (500,310),
        "waiting" : 0,
        "name" : "Boramae",
        "connected" : ["신풍","신대방삼거리"]
    }, "신대방삼거리": {
        "line": [7],
        "passenger" : 33476,
        "pos" : (540,310),
        "waiting" : 0,
        "name" : "SDBsamgeori",
        "connected" : ["보라매","장승배기"]
    }, "장승배기": {
        "line": [7],
        "passenger" : 21826,
        "pos" : (580,310),
        "waiting" : 0,
        "name" : "JSbaegi",
        "connected" : ["신대방삼거리","상도"]
    }, "상도": {
        "line": [7],
        "passenger" : 23715,
        "pos" : (620,310),
        "waiting" : 0,
        "name" : "Sangdo",
        "connected" : ["장승배기","숭실대입구"]
    }, "숭실대입구": {
        "line": [7],
        "passenger" : 30871,
        "pos" : (660,310),
        "waiting" : 0,
        "name" : "Soongsil",
        "connected" : ["상도","남성"]
    }, "남성": {
        "line": [7],
        "passenger" : 23045,
        "pos" : (700,310),
        "waiting" : 0,
        "name" : "Namseong",
        "connected" : ["숭실대입구","이수"]
    }, "내방": {
        "line": [7],
        "passenger" : 28315,
        "pos" : (810,310),
        "waiting" : 0,
        "name" : "Naebang",
        "connected" : ["이수","고속터미널"]
    }, "반포": {
        "line": [7],
        "passenger" : 13183,
        "pos" : (920,230),
        "waiting" : 0,
        "name" : "Banpo",
        "connected" : ["고속터미널","논현"]
    }, "논현": {
        "line": [7],
        "passenger" : 39726,
        "pos" : (970,230),
        "waiting" : 0,
        "name" : "Nonhyeon",
        "connected" : ["반포","학동"]
    }, "학동": {
        "line": [7],
        "passenger" : 43807,
        "pos" : (1020,230),
        "waiting" : 0,
        "name" : "Hakdong",
        "connected" : ["논현","강남구청"]
    }, "강남구청": {
        "line": [7,"수인분당"],
        "passenger" : 54509,
        "pos" : (1070,230),
        "waiting" : 0,
        "name" : "G-gu Off.",
        "connected" : ["학동","청담","선정릉","압구정로데오"]
    }, "청담": {
        "line": [7],
        "passenger" : 41605,
        "pos" : (1120,200),
        "waiting" : 0,
        "name" : "Cheongdam",
        "connected" : ["강남구청","뚝섬유원지"]
    }, "뚝섬유원지": {
        "line": [7],
        "passenger" : 18826,
        "pos" : (1190,150),
        "waiting" : 0,
        "name" : "TtukPark",
        "connected" : ["청담","건대입구"]
    }, "어린이대공원": {
        "line": [7],
        "passenger" : 31848,
        "pos" : (1300,100),
        "waiting" : 0,
        "name" : "ChildPark",
        "connected" : ["건대입구","군자"]
    }, "군자": {
        "line": [5,7],
        "passenger" : 50649,
        "pos" : (1350,70),
        "waiting" : 0,
        "name" : "Gunja",
        "connected" : ["어린이대공원","중곡"]
    }, "중곡": {
        "line": [7],
        "passenger" : 20060,
        "pos" : (1400,40),
        "waiting" : 0,
        "name" : "Junggok",
        "connected" : ["군자","용마산"]
    }, "용마산": {
        "line": [7],
        "passenger" : 12435,
        "pos" : (1450,10),
        "waiting" : 0,
        "name" : "Yongmasan",
        "connected" : ["중곡"]
    }, "남구로": {
        "line": [7],
        "passenger" : 33002,
        "pos" : (350,390),
        "waiting" : 0,
        "name" : "Namguro",
        "connected" : ["가산디지털단지","대림"]
    }, "가산디지털단지": {
        "line": [1,7],
        "passenger" : 130234,
        "pos" : (300,420),
        "waiting" : 0,
        "name" : "GaDiDan",
        "connected" : ["철산","남구로","독산","구로"]
    }, "철산": {
        "line": [7],
        "passenger" : 48722,
        "pos" : (250,420),
        "waiting" : 0,
        "name" : "Cheolsan",
        "connected" : ["광명사거리","가산디지털단지"]
    }, "광명사거리": {
        "line": [7],
        "passenger" : 52082,
        "pos" : (200,420),
        "waiting" : 0,
        "name" : "G-sageori",
        "connected" : ["천왕","철산"]
    }, "천왕": {
        "line": [7],
        "passenger" : 18721,
        "pos" : (150,420),
        "waiting" : 0,
        "name" : "Cheonwang",
        "connected" : ["온수","광명사거리"]
    }, "온수": {
        "line": ["경인선",7],
        "passenger" : 37868,
        "pos" : (100,420),
        "waiting" : 0,
        "name" : "Onsu",
        "connected" : ["까치울","천왕","역곡","오류동"]
    }, "까치울": {
        "line": [7],
        "passenger" : 15082,
        "pos" : (50,420),
        "waiting" : 0,
        "name" : "KKachiul",
        "connected" : ["온수"]
    }, "청량리": {
        "line": [1,"경인선","수인분당","경의중앙","경춘선"],
        "passenger" : 88031,
        "pos" : (970,10),
        "waiting" : 0,
        "name" : "Cheongyangni",
        "connected" : ["왕십리"]
    }, "서울숲": {
        "line": ["수인분당"],
        "passenger" : 17523,
        "pos" : (1020,90),
        "waiting" : 0,
        "name" : "Seoulsup",
        "connected" : ["압구정로데오","왕십리"]
    }, "압구정로데오": {
        "line": ["수인분당"],
        "passenger" : 35047,
        "pos" : (1070,150), #1070 230
        "waiting" : 0,
        "name" : "A-guRodeo",
        "connected" : ["강남구청","서울숲"]
    }, "한티": {
        "line": ["수인분당"],
        "passenger" : 30614,
        "pos" : (1050,410),
        "waiting" : 0,
        "name" : "Hanti",
        "connected" : ["도곡","선릉"]
    }, "도곡": {
        "line": [3,"수인분당"],
        "passenger" : 25584,
        "pos" : (1050,460),
        "waiting" : 0,
        "name" : "Dogok",
        "connected" : ["구룡","한티","매봉","대치"]
    }, "구룡": {
        "line": ["수인분당"],
        "passenger" : 3442+2000,
        "pos" : (1050,500),
        "waiting" : 0,
        "name" : "Guryong",
        "connected" : ["개포동","도곡"]
    }, "개포동": {
        "line": ["수인분당"],
        "passenger" : 6891,
        "pos" : (1110,500),
        "waiting" : 0,
        "name" : "Gaepodong",
        "connected" : ["대모산입구","구룡"]
    }, "대모산입구": {
        "line": ["수인분당"],
        "passenger" : 6526,
        "pos" : (1170,500),
        "waiting" : 0,
        "name" : "Daemosan",
        "connected" : ["수서","개포동"]
    }, "수서": {
        "line": [3,"수인분당"],
        "passenger" : 69028,
        "pos" : (1240,500),
        "waiting" : 0,
        "name" : "Suseo",
        "connected" : ["복정","대모산입구","일원","가락시장"]
    }, "복정": {
        "line": [8,"수인분당"],
        "passenger" : 21345,
        "pos" : (1300,550),
        "waiting" : 0,
        "name" : "Bokjeong",
        "connected" : ["가천대","수서"]
    }, "가천대": {
        "line": ["수인분당"],
        "passenger" : 20142,
        "pos" : (1300,600),
        "waiting" : 0,
        "name" : "Gachon Univ.",
        "connected" : ["태평","복정"]
    }, "태평": {
        "line": ["수인분당"],
        "passenger" : 28397,
        "pos" : (1300,650),
        "waiting" : 0,
        "name" : "Taepyeong",
        "connected" : ["모란","가천대"]
    }, "모란": {
        "line": [8,"수인분당"],
        "passenger" : 54977,
        "pos" : (1300,700),
        "waiting" : 0,
        "name" : "Moran",
        "connected" : ["태평"]
    }, "군포": {
        "line": [1],
        "passenger" : 14694,
        "pos" : (350,720),
        "waiting" : 0,
        "name" : "Gunpo",
        "connected" : ["금정"]
    }, "명학": {
        "line": [1],
        "passenger" : 19836,
        "pos" : (350,630),
        "waiting" : 0,
        "name" : "Myeonghak",
        "connected" : ["금정","안양"]
    }, "안양": {
        "line": [1],
        "passenger" : 54852,
        "pos" : (350,590),
        "waiting" : 0,
        "name" : "Anyang",
        "connected" : ["명학","관악"]
    }, "관악": {
        "line": [1],
        "passenger" : 16788,
        "pos" : (340,550),
        "waiting" : 0,
        "name" : "Gwanak",
        "connected" : ["안양","석수"]
    }, "석수": {
        "line": [1],
        "passenger" : 21936,
        "pos" : (330,510),
        "waiting" : 0,
        "name" : "Seoksu",
        "connected" : ["관악","금천구청"]
    }, "금천구청": {
        "line": [1,"광명셔틀"],
        "passenger" : 24555,
        "pos" : (320,480),
        "waiting" : 0,
        "name" : "Geumgu Off.",
        "connected" : ["석수","독산"]
    }, "독산": {
        "line": [1],
        "passenger" : 33135,
        "pos" : (310,450),
        "waiting" : 0,
        "name" : "Doksan",
        "connected" : ["금천구청","가산디지털단지"]
    }, "구로": {
        "line": [1,"경인선"],
        "passenger" : 41166,
        "pos" : (310,390),
        "waiting" : 0,
        "name" : "Guro",
        "connected" : ["가산디지털단지","신도림","구일"]
    }, "영등포": {
        "line": [1,"경인선"],
        "passenger" : 102391,
        "pos" : (400,330),
        "waiting" : 0,
        "name" : "YDP",
        "connected" : ["신도림","신길"]
    }, "신길": {
        "line": [1,5,"경인선"],
        "passenger" : 21930,
        "pos" : (430,300),
        "waiting" : 0,
        "name" : "Singil",
        "connected" : ["영등포","대방"]
    }, "대방": {
        "line": [1,"경인선"],
        "passenger" : 29363,
        "pos" : (460,270),
        "waiting" : 0,
        "name" : "Daebang",
        "connected" : ["신길","노량진"]
    }, "용산": {
        "line": [1,"경인선","경의중앙"],
        "passenger" : 86313,
        "pos" : (490,190),
        "waiting" : 0,
        "name" : "Yongsan",
        "connected" : ["노량진","남영"]
    }, "남영": {
        "line": [1,"경인선"],
        "passenger" : 21412,
        "pos" : (490,140),
        "waiting" : 0,
        "name" : "Namyeong",
        "connected" : ["용산","서울역"]
    }, "시청": {
        "line": [1,"경인선",2],
        "passenger" : 102616,
        "pos" : (490,40),
        "waiting" : 0,
        "name" : "City Hall",
        "connected" : ["서울역","종각","을지로입구","충정로"]
    }, "종각": {
        "line": [1,"경인선"],
        "passenger" : 86177,
        "pos" : (490,10),
        "waiting" : 0,
        "name" : "Jonggak",
        "connected" : ["시청"]
    }, "구일": {
        "line": ["경인선"],
        "passenger" : 16587,
        "pos" : (250,390),
        "waiting" : 0,
        "name" : "Guil",
        "connected" : ["개봉","구로"]
    }, "개봉": {
        "line": ["경인선"],
        "passenger" : 48462,
        "pos" : (200,390),
        "waiting" : 0,
        "name" : "Gaebong",
        "connected" : ["오류동","구일"]
    }, "오류동": {
        "line": ["경인선"],
        "passenger" : 24706,
        "pos" : (150,390),
        "waiting" : 0,
        "name" : "Oryudong",
        "connected" : ["온수","개봉"]
    }, "역곡": {
        "line": ["경인선"],
        "passenger" : 61883,
        "pos" : (50,450),
        "waiting" : 0,
        "name" : "Oryudong",
        "connected" : ["온수"]
    }, "가락시장": {
        "line": [3,8],
        "passenger" : 36897,
        "pos" : (1300,460),
        "waiting" : 0,
        "name" : "G-Market",
        "connected" : ["수서","경찰병원"]
    }, "경찰병원": {
        "line": [3],
        "passenger" : 15441,
        "pos" : (1350,460),
        "waiting" : 0,
        "name" : "PolHosp.",
        "connected" : ["가락시장","오금"]
    }, "오금": {
        "line": [3,5],
        "passenger" : 20165,
        "pos" : (1400,460),
        "waiting" : 0,
        "name" : "Ogeum",
        "connected" : ["경찰병원"]
    }, "일원": {
        "line": [3],
        "passenger" : 20058,
        "pos" : (1240,460),
        "waiting" : 0,
        "name" : "Irwon",
        "connected" : ["대청","수서"]
    }, "대청": {
        "line": [3],
        "passenger" : 19710,
        "pos" : (1200,460),
        "waiting" : 0,
        "name" : "Daecheong",
        "connected" : ["학여울","일원"]
    }, "학여울": {
        "line": [3],
        "passenger" : 5705,
        "pos" : (1150,460),
        "waiting" : 0,
        "name" : "HYW",
        "connected" : ["대치","대청"]
    }, "대치": {
        "line": [3],
        "passenger" : 24926,
        "pos" : (1100,460),
        "waiting" : 0,
        "name" : "Daechi",
        "connected" : ["도곡","학여울"]
    }, "매봉": {
        "line": [3],
        "passenger" : 22290,
        "pos" : (1000,460),
        "waiting" : 0,
        "name" : "Maebong",
        "connected" : ["양재","도곡"]
    }, "양재": {
        "line": [3,"신분당"],
        "passenger" : 100028,
        "pos" : (950,460),
        "waiting" : 0,
        "name" : "Yangjae",
        "connected" : ["남부터미널","매봉"]
    }, "남부터미널": {
        "line": [3],
        "passenger" : 70384,
        "pos" : (950,410),
        "waiting" : 0,
        "name" : "Nambu",
        "connected" : ["교대","양재"]
    }, "잠원": {
        "line": [3],
        "passenger" : 12877,
        "pos" : (870,210),
        "waiting" : 0,
        "name" : "Jamwon",
        "connected" : ["신사","고속터미널"]
    }, "신사": {
        "line": [3],
        "passenger" : 68540,
        "pos" : (870,160),
        "waiting" : 0,
        "name" : "Sinsa",
        "connected" : ["압구정","잠원"]
    }, "압구정": {
        "line": [3],
        "passenger" : 69908,
        "pos" : (870,110),
        "waiting" : 0,
        "name" : "Apgujeong",
        "connected" : ["옥수","신사"]
    }, "옥수": {
        "line": [3,"경의중앙"],
        "passenger" : 20878,
        "pos" : (870,60),
        "waiting" : 0,
        "name" : "Oksu",
        "connected" : ["금호","압구정"]
    }, "금호": {
        "line": [3],
        "passenger" : 16919,
        "pos" : (820,60),
        "waiting" : 0,
        "name" : "Geumho",
        "connected" : ["약수","옥수"]
    }, "약수": {
        "line": [3,6],
        "passenger" : 36351,
        "pos" : (770,60),
        "waiting" : 0,
        "name" : "Yaksu",
        "connected" : ["동대입구","금호"]
    }, "동대입구": {
        "line": [3],
        "passenger" : 25182,
        "pos" : (710,60),
        "waiting" : 0,
        "name" : "Dongguk Univ.",
        "connected" : ["충무로","약수"]
    }, "을지로3가": {
        "line": [2,3],
        "passenger" : 68609,
        "pos" : (590,10),
        "waiting" : 0,
        "name" : "Euljiro 3",
        "connected" : ["충무로","종로3가","을지로입구","을지로4가"]
    }, "종로3가": {
        "line": [1,3,"경인선"],
        "passenger" : 125348,
        "pos" : (540,10),
        "waiting" : 0,
        "name" : "Jongno 3",
        "connected" : ["을지로3가"]
    },
}
