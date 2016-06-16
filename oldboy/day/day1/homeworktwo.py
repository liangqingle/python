# -*- coding:utf-8 -*-

"""
三级菜单
可依次选择进入各子菜单
所需新知识点：列表、字典
"""
country=["中国",
         "美国",
         "英国"
]


province={"中国":["广东",
                  "广西",
                  "湖南",
                  "湖北",
                  "山东",
                  "山西",
                  "云南",
                  "四川",
                  "安徽",
                  "辽宁"
                    ]
           }  


city={
         "广东":["广州","深圳","珠海"],
         "广西":["南宁","柳州","桂林"],
         "湖南":["长沙","衡阳","湘潭"]
     } 


country_choise = None
province_choise = None
city_choise = None

tmp_province = None
tmp_city = None

countryNum = -1
provinceNum = -1
cityNum = -1

while True:
    if len(country) == 0:
        print("没有可以选择的国家")
        break

    for item in list(enumerate(country)):
        print("%s : %s"%(item[0], item[1]))
    
    country_choise=input("请输入你选择的序号").strip()
    if not country_choise.isdigit():
        if country_choise == "quit":
            break
        else:
            continue
    
    country_choise = int(country_choise)
    countryNum = len(list(enumerate(country)))
    if country_choise < 0 or country_choise >= countryNum:
        continue

    countryname = country[country_choise]
    if not countryname in province:
        print("%s 找不到省份"%countryname)
        continue

    tmp_province = province[countryname]
    if len(tmp_province) == 0:
        print("%s 找不到省份"%countryname)
        continue

    while True:
        for item in list(enumerate(tmp_province)):
            print("%s : %s"%(item[0], item[1]))  

        province_choise = input("请输入你选择的序号")
        province_choise = province_choise.strip()

        if not province_choise.isdigit():
            if province_choise == "quit":
                break
            else:
                continue

        provinceNum = len(list(enumerate(tmp_province)))   
        province_choise = int(province_choise)  
        if province_choise < 0 or province_choise >= provinceNum:
            continue

        provincename = tmp_province[province_choise]    
        if provincename not in city:
            print("找不到省份%s"%(provincename))
            continue

        tmp_city = city[provincename]
        if len(tmp_city) == 0:
            print("没有城市列表")
            continue
        
        while True:
            for item in list(enumerate(tmp_city)):
                print("%s:%s"%(item[0], item[1]))

            city_choise = input("请输入你选择的序号")
            city_choise = city_choise.strip()
            
            if not city_choise.isdigit():
                if city_choise == "quit":
                    break
                else:
                    continue

            cityNum = len(list(enumerate(tmp_city)))
            city_choise = int(city_choise)
   
            if city_choise < 0 or city_choise >= cityNum:
                continue
            else:
                print(tmp_city[city_choise])

    