from bs4 import BeautifulSoup
import json

def load_html(bulten_html_file_path):
    try:
        with open(bulten_html_file_path) as fp:
            soup = BeautifulSoup(fp.read(), 'html.parser')
    except:

        return False

    return soup

def parse_iddaa_bulten(soup):
    tds = soup.find_all("td")
    len_tds = len(tds)

    dirty_matchs = []
    for i in range(0, len_tds, 43):
        last = i+43
        match = tds[i:last]
        dirty_matchs.append(match)

    # clean
    matches = {}

    for i in range(1,len(dirty_matchs)):
        dirty_match = dirty_matchs[i]
        matches[i] = {}
        matches[i]['lig_kod'] = dirty_match[0].getText()
        matches[i]['saat'] = dirty_match[1].getText()
        matches[i]['mac_kod'] = dirty_match[2].getText()
        matches[i]['ev_sahibi_konuk_takim'] = dirty_match[3].getText()
        matches[i]['mbs'] = dirty_match[4].getText()
        matches[i]['mac_sonucu_1'] = dirty_match[5].getText()
        matches[i]['mac_sonucu_X'] = dirty_match[6].getText()
        matches[i]['mac_sonucu_2'] = dirty_match[7].getText()
        matches[i]['iki_bucuk_gol_alt'] = dirty_match[8].getText()
        matches[i]['iki_bucuk_gol_ust'] = dirty_match[9].getText()
        matches[i]['cifte_sans_1_X'] = dirty_match[10].getText()
        matches[i]['cifte_sans_1_2'] = dirty_match[11].getText()
        matches[i]['cifte_sans_2_X'] = dirty_match[12].getText()
        matches[i]['karsilikli_gol_var'] = dirty_match[13].getText()
        matches[i]['karsilikli_gol_yok'] = dirty_match[14].getText()
        matches[i]['handikapli_ms_1'] = dirty_match[16].getText()
        matches[i]['handikapli_ms_X'] = dirty_match[17].getText()
        matches[i]['handikapli_ms_2'] = dirty_match[18].getText()
        matches[i]['iy_1_5_alt'] = dirty_match[20].getText()
        matches[i]['iy_1_5_ust'] = dirty_match[21].getText()
        matches[i]['ms_1_5_alt'] = dirty_match[22].getText()
        matches[i]['ms_1_5_ust'] = dirty_match[23].getText()
        matches[i]['ms_3_5_alt'] = dirty_match[24].getText()
        matches[i]['ms_3_5_ust'] = dirty_match[25].getText()
        matches[i]['toplam_gol_0_1'] = dirty_match[26].getText()
        matches[i]['toplam_gol_2_3'] = dirty_match[27].getText()
        matches[i]['toplam_gol_4_6'] = dirty_match[28].getText()
        matches[i]['toplam_gol_7_arti'] = dirty_match[29].getText()
        matches[i]['ilk_yari_sonuc_1'] = dirty_match[30].getText()
        matches[i]['ilk_yari_sonuc_X'] = dirty_match[31].getText()
        matches[i]['ilk_yari_sonuc_2'] = dirty_match[32].getText()
        matches[i]['ilk_yari_mac_sonucu_mbs'] = dirty_match[33].getText()
        matches[i]['ilk_yari_mac_sonucu_1_1'] = dirty_match[34].getText()
        matches[i]['ilk_yari_mac_sonucu_X_1'] = dirty_match[35].getText()
        matches[i]['ilk_yari_mac_sonucu_2_1'] = dirty_match[36].getText()
        matches[i]['ilk_yari_mac_sonucu_1_X'] = dirty_match[37].getText()
        matches[i]['ilk_yari_mac_sonucu_X_X'] = dirty_match[38].getText()
        matches[i]['ilk_yari_mac_sonucu_2_X'] = dirty_match[39].getText()
        matches[i]['ilk_yari_mac_sonucu_1_3'] = dirty_match[40].getText()
        matches[i]['ilk_yari_mac_sonucu_X_2'] = dirty_match[41].getText()
        matches[i]['ilk_yari_mac_sonucu_2_2'] = dirty_match[42].getText()

    return matches


html_file_name = "l2019_02_10.html";
iddaa_bulten_path = "htmls/{}".format(html_file_name)
soup = load_html(iddaa_bulten_path)

if soup:
    matches = parse_iddaa_bulten(soup)

    with open("jsons/{}.json".format(html_file_name), "w") as jp:
        json.dump(matches, jp)




