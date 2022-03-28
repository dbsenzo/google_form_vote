import random
from selenium import webdriver
import threading
import time
from selenium.webdriver.chrome.options import Options



string = "entry.536148030=Lutte+Ouvri%C3%A8re&entry.1879130900=Parti+communiste+Fran%C3%A7ais&entry.934989377=La+r%C3%A9publique+en+marche&entry.1852195556=La+France+insoumise&entry.131601119=Rassemblement+National&entry.1644548102=Reconqu%C3%AAte%21&entry.1146538627=Europe+%C3%A9cologie+les+verts&entry.1358697146=Parti+socialiste&entry.189907889=Les+R%C3%A9publicains&entry.1257410652=R%C3%A9sistons%21&entry.510688687=Nouveau+parti+anticapitaliste&entry.325816330=Debout+la+France&entry.443885144=MITTERAND+FRANCOIS&entry.443885144=CHIRAC+JACQUES&entry.443885144=SARKOZY+NICOLAS&entry.443885144=MELENCHON+JEAN-LUC&entry.443885144=HOLLANDE+FRANCOIS&entry.443885144=MACRON+EMMANUEL&entry.1439574181=les+%C3%A9trangers+qui+vivent+en+France&entry.620764227=18+ans&entry.556137018=4&entry.2055741787=6&entry.717832983=5&entry.1475744703=2&entry.1318818985=1&entry.194877379=3&entry.1714561312=MACRON+EMMANUEL&entry.1714561312=ZEMMOUR+ERIC&entry.1714561312=POUTOU+PHILIPE&entry.1714561312=ARTHAUD+NATHALIE&entry.1714561312=LASSALLE+JEAN&entry.1714561312=PECRESSE+VALERIE&entry.1714561312=JADOT+YANNICK&entry.1714561312=DUPONT-AIGNAN+NICOLAS&entry.1714561312=ROUSSEL+FABIEN&entry.1714561312=HIDALGO+ANNE&dlut=1647985650674&entry.44366011_sentinel=&entry.1409202567_sentinel=&entry.802707709_sentinel=&entry.1428498951_sentinel=&entry.1714561312_sentinel=&entry.717832983_sentinel=&entry.1318818985_sentinel=&entry.194877379_sentinel=&entry.1475744703_sentinel=&entry.2055741787_sentinel=&entry.556137018_sentinel=&entry.620764227_sentinel=&entry.1439574181_sentinel=&entry.443885144_sentinel=&entry.536148030_sentinel=&entry.1879130900_sentinel=&entry.934989377_sentinel=&entry.1257410652_sentinel=&entry.131601119_sentinel=&entry.1644548102_sentinel=&entry.1852195556_sentinel=&entry.1358697146_sentinel=&entry.1146538627_sentinel=&entry.189907889_sentinel=&entry.510688687_sentinel=&entry.325816330_sentinel=&entry.1103281565_sentinel=&entry.592530520_sentinel=&fvv=0&partialResponse=%5Bnull%2Cnull%2C%22-5480487982960307652%22%5D&pageHistory=0&fbzx=-5480487982960307652"

them_old = ["entry.1103281565=%C3%89conomie",
        "entry.1103281565=Travail",
        "entry.1103281565=%C3%89ducation",
        "entry.1103281565=Justice",
        "entry.1103281565=S%C3%A9curit%C3%A9",
        "entry.1103281565=%C3%89cologie",
        "entry.1103281565=Social"]

them = ["entry.1103281565=%C3%89conomie",
        "entry.1103281565=Travail",
        "entry.1103281565=S%C3%A9curit%C3%A9",
        "entry.1103281565=%C3%89cologie"]

sexe = ["entry.44366011=Femme",
        "entry.44366011=Homme"]

avis_meilleur_prog = ["entry.592530520=Un+homme",
                      "entry.592530520=a+%2B+de+30+ans"]

avis_meilleur_prog_toutes = ["entry.592530520=Un+homme",
                      "entry.592530520=Une+femme",
                      "entry.592530520=a+-+de+30+ans",
                      "entry.592530520=a+%2B+de+30+ans",
                      "entry.592530520=n%27a+pas+de+casier+judiciaire",
                      "entry.592530520=est+dans+la+politique+depuis+longtemps"]

etude = ["entry.1428498951=Doctorat",
         "entry.1428498951=BTS",
         "entry.1428498951=BUT (ou DUT)",
         "entry.1428498951=Licence",
         "entry.1428498951=Master",
         "entry.1428498951=BAC Pro",
         "entry.1428498951=Brevet"]

cadre_vie = ["entry.802707709=Cadres+et+professions+intellectuelles+sup%C3%A9rieures",
             "entry.802707709=Ouvriers",
             "entry.802707709=Artisans.+commerçants.+chefs+entreprise",
             "entry.802707709=Agriculture+exploitants",
             "entry.802707709=Employ%C3%A9s"]

texte = "entry.1140952338=."

depart = ["entry.333139798=01+Ain",
          "entry.333139798=02+Aisne",
          "entry.333139798=03+Allier",
          "entry.333139798=04+Alpes+de+Haute+Provence",
          "entry.333139798=05+Hautes+Alpes",
          "entry.333139798=06+Alpes+maritimes",
          "entry.333139798=07+Ard%C3%A8che",
          "entry.333139798=08+Ardennes",
          "entry.333139798=09+Ari%C3%A8ge",
          "entry.333139798=10+Aube",
          "entry.333139798=11+Aude",
          "entry.333139798=12+Aveyron",
          "entry.333139798=13+Bouches+du+rhone",
          "entry.333139798=14+Calvados",
          "entry.333139798=15+Cantal",
          "entry.333139798=16+Charente",
          "entry.333139798=17+Charente+maritime",
          "entry.333139798=18+Cher",
          "entry.333139798=19+Corr%C3%A8ze",
          "entry.333139798=2A+Haute-Corse",
          "entry.333139798=2B+Corse+du+Sud",
          "entry.333139798=21+C%C3%B4te+d%27Or",
          "entry.333139798=22+C%C3%B4tes+d%27Armor",
          "entry.333139798=23+Creuse",
          "entry.333139798=24+Dordogne",
          "entry.333139798=25+Doubs",
          "entry.333139798=26+Dr%C3%B4me",
          "entry.333139798=27+Eure",
          "entry.333139798=28+Eure+et+Loir",
          "entry.333139798=29+Finist%C3%A8re",
          "entry.333139798=30+Gard",
          "entry.333139798=31+Haute+Garonne",
          "entry.333139798=32+Gers",
          "entry.333139798=33+Gironde",
          "entry.333139798=34+H%C3%A9rault",
          "entry.333139798=35+Ille-et-Vilaine",
          "entry.333139798=36+Indre",
          "entry.333139798=37+Indre+et+Loire",
          "entry.333139798=38+Is%C3%A8re",
          "entry.333139798=39+Jura",
          "entry.333139798=40+Landes",
          "entry.333139798=41+Loir-et-Cher",
          "entry.333139798=42+Loire",
          "entry.333139798=43+Haute-Loire",
          "entry.333139798=44+Loire-Atlantique",
          "entry.333139798=45+Loiret",
          "entry.333139798=46+Lot",
          "entry.333139798=47+Lot-et-Garonne",
          "entry.333139798=48+Loz%C3%A8re",
          "entry.333139798=49+Maine-et-Loire",
          "entry.333139798=50+Manche",
          "entry.333139798=51+Marne",
          "entry.333139798=52+Haute-Marne",
          "entry.333139798=53+Mayenne",
          "entry.333139798=54+Meurthe-et-Moselle",
          "entry.333139798=55+Meuse",
          "entry.333139798=56+Morbihan",
          "entry.333139798=57+Moselle",
          "entry.333139798=58+Ni%C3%A8vre",
          "entry.333139798=59+Nord",
          "entry.333139798=60+Oise",
          "entry.333139798=61+Orne",
          "entry.333139798=62+Pas-de-Calais",
          "entry.333139798=63+Puy-de-D%C3%B4me",
          "entry.333139798=64+Pyr%C3%A9n%C3%A9es+Atlantiques",
          "entry.333139798=65+Hautes-Pyr%C3%A9n%C3%A9es",
          "entry.333139798=66+Pyr%C3%A9n%C3%A9es+Orientales",
          "entry.333139798=67+Bas-Rhin",
          "entry.333139798=68+Haut-Rhin",
          "entry.333139798=69+Rh%C3%B4ne",
          "entry.333139798=70+Haute-Sa%C3%B4ne",
          "entry.333139798=71+Sa%C3%B4ne-et-Loire",
          "entry.333139798=72+Sarthe",
          "entry.333139798=73+Savoie",
          "entry.333139798=74+Haute-Savoie",
          "entry.333139798=75+Paris",
          "entry.333139798=76+Seine-Maritime",
          "entry.333139798=77+Seine-et-Marne",
          "entry.333139798=78+Yvelines",
          "entry.333139798=79+Deux-S%C3%A8vres",
          "entry.333139798=80+Somme",
          "entry.333139798=81+Tarn",
          "entry.333139798=82+Tarn-et-Garonne",
          "entry.333139798=83+Var",
          "entry.333139798=84+Vaucluse",
          "entry.333139798=85+Vend%C3%A9e",
          "entry.333139798=86+Vienne",
          "entry.333139798=87+Haute-Vienne",
          "entry.333139798=88+Vosges",
          "entry.333139798=89+Yonne",
          "entry.333139798=90+Territoire+de+Belfort",
          "entry.333139798=91+Essonne",
          "entry.333139798=92+Hauts-de-Seine",
          "entry.333139798=93+Seine-Saint-Denis",
          "entry.333139798=94+Val-de-Marne",
          "entry.333139798=95+Val-d%27Oise"]

tranche = ["entry.1409202567=18+-+25+ans","entry.1409202567=26+-+35+ans","entry.1409202567=46+-+55+ans","entry.1409202567=36+-+45+ans"]



def loop1_10():
    for i in range(0,100000000):
    #link-t = "https://docs.google.com/forms/d/e/1FAIpQLSe_l-EcfP5soISz-tCGjuyTWJgloGerTZQawjT2Q1fFAbjc1Q/viewform?"+string+"&"+sexe[random.randrange(0,2)]+"&"+depart[random.randrange(0,94)]+"&"+them[random.randrange(0,6)]+"&"+cadre_vie[random.randrange(0,3)]+"&"+avis_meilleur_prog[random.randrange(0,5)]+"&"+etude[random.randrange(0,4)]+"&"+texte+"&entry.1409202567=36+-+45+ans"

        chrome_options = Options()
        # incognito window
        chrome_options.add_argument("--incognito")
        link = "https://docs.google.com/forms/d/e/1FAIpQLSe_l-EcfP5soISz-tCGjuyTWJgloGerTZQawjT2Q1fFAbjc1Q/viewform?"+string+"&"+sexe[random.randrange(0,2)]+"&"+depart[random.randrange(0,94)]+"&"+them[random.randrange(0,3)]+"&"+cadre_vie[random.randrange(4)]+"&"+avis_meilleur_prog[random.randrange(0,2)]+"&"+etude[random.randrange(0,6)]+"&"+texte+"&"+tranche[random.randrange(0,4)]
        driver2 = webdriver.Chrome(r'chromedriver.exe')

        driver2.maximize_window()
        driver2.get(link)


        driver2.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        driver2.close

threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
threading.Thread(target=loop1_10).start()
