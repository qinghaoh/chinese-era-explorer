import copy
import csv
import json
import re
from pathlib import Path

# The source of the data is https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%B9%B4%E5%8F%B7%E5%88%97%E8%A1%A8
# The CSV files are generated by the tool: https://wikitable2csv.ggor.de/
# attributes: [dynasty name, dynasty group]
#
# Elements (德運): https://zh.wikipedia.org/wiki/%E4%BA%94%E5%BE%B7%E7%B5%82%E5%A7%8B%E8%AA%AA
# 參考
# - 十六國德運：《王化與山險》，羅新，2019
# - 金朝德運：《正統與華夷：中國傳統政治文化研究》，劉浦江，2017
CSV_FILES = {
    "western_han.csv": ("西漢", "漢朝", ("火土", -104)),
    "xin.csv": ("新", "漢朝", "土"),
    "gengshi.csv": ("更始", "漢朝", ""),
    "xin_gengshi_others.csv": None,
    "eastern_han.csv": ("東漢", "漢朝", "火"),
    "eastern_han_others.csv": None,
    "cao_wei.csv": ("曹魏", "三國", "土"),
    "cao_wei_others.csv": None,
    "shu_han.csv": ("蜀漢", "三國", "火"),
    "sun_wu.csv": ("孫吳", "三國", "木"),
    "western_jin.csv": ("西晉", "晉朝", "金"),
    "western_jin_others.csv": None,
    "eastern_jin.csv": ("東晉", "晉朝", "金"),
    "eastern_jin_others.csv": None,
    "han_zhao.csv": ("漢趙", "十六國", ("無水", 319)),
    "han_zhao_others.csv": None,
    "cheng_han.csv": ("成漢", "十六國", ""),
    "former_liang.csv": ("前涼", "十六國", ""),
    "former_liang_others.csv": None,
    "later_zhao.csv": ("後趙", "十六國", "水"),
    "ran_wei.csv": ("冉魏", "十六國", ""),
    "later_zhao_others.csv": None,
    "dai.csv": ("代", "十六國", ""),
    "former_yan.csv": ("前燕", "十六國", ("水木", 364)),
    "former_qin.csv": ("前秦", "十六國", "木"),
    "former_qin_others.csv": None,
    "later_qin.csv": ("後秦", "十六國", "火"),
    "later_yan.csv": ("後燕", "十六國", ""),
    "later_yan_others.csv": None,
    "western_yan.csv": ("西燕", "十六國", ""),
    "western_qin.csv": ("西秦", "十六國", ""),
    "later_liang.csv": ("後涼", "十六國", ""),
    "southern_liang.csv": ("南涼", "十六國", ""),
    "southern_yan.csv": ("南燕", "十六國", ""),
    "southern_yan_others.csv": None,
    "western_liang.csv": ("西涼", "十六國", ""),
    "western_liang_others.csv": None,
    "xia.csv": ("夏", "十六國", ""),
    "northern_yan.csv": ("北燕", "十六國", ""),
    "northern_liang.csv": ("北涼", "十六國", ""),
    "northern_liang_others.csv": None,
    "liu_song.csv": ("劉宋", "南北朝", "水"),
    "liu_song_others.csv": None,
    "southern_qi.csv": ("南齊", "南北朝", "木"),
    "southern_qi_others.csv": None,
    "xiao_liang.csv": ("南梁", "南北朝", "火"),
    "xiao_liang_others.csv": None,
    "western_xiao_liang.csv": ("西梁", "南北朝", "火"),
    "southern_chen.csv": ("南陳", "南北朝", "土"),
    "northern_wei.csv": ("北魏", "南北朝", ("土水", 490)),
    "northern_wei_others.csv": None,
    "eastern_wei.csv": ("東魏", "南北朝", "水"),
    "eastern_wei_others.csv": None,
    "western_wei.csv": ("西魏", "南北朝", "水"),
    "northern_qi.csv": ("北齊", "南北朝", "木"),
    "northern_qi_others.csv": None,
    "northern_zhou.csv": ("北周", "南北朝", "木"),
    "northern_zhou_others.csv": None,
    "goguryeo.csv": ("高句麗", "南北朝", ""),
    "goguryeo_others.csv": None,
    "rouran.csv": ("柔然", "南北朝", ""),
    "gaochang.csv": ("高昌", "南北朝", ""),
    "gaochang_others.csv": None,
    "sui.csv": ("隋", "隋朝", "火"),
    "sui_others.csv": None,
    "tang.csv": ("唐", "唐朝", "土"),
    "wu_zhou.csv": ("武周", "唐朝", ""),
    "tang2.csv": ("唐", "唐朝", "土"),
    "tang_others.csv": None,
    "tibet.csv": ("吐蕃", "唐朝", ""),
    "khotan.csv": ("于闐", "唐朝", ""),
    "bohai.csv": ("渤海", "唐朝", ""),
    "dongdan.csv": ("東丹", "唐朝", ""),
    "dingan.csv": ("定安", "唐朝", ""),
    "nanzhao.csv": ("南詔", "唐朝", ""),
    "dachanghe.csv": ("大長和", "唐朝", ""),
    "datianxing.csv": ("大天興", "唐朝", ""),
    "dayining.csv": ("大義寧", "唐朝", ""),
    "dali.csv": ("大理", "唐朝", ""),
    "dazhong.csv": ("大中", "唐朝", ""),
    "dali2.csv": ("後大理", "唐朝", ""),
    "nanzhao_dali_others.csv": None,
    "zhu_liang.csv": ("後梁", "五代十國", "金"),
    "zhu_liang_others.csv": None,
    "hedong.csv": ("河東", "五代十國", ""),
    "later_tang.csv": ("後唐", "五代十國", "土"),
    "later_jin.csv": ("後晉", "五代十國", "金"),
    "later_jin_others.csv": None,
    "later_han.csv": ("後漢", "五代十國", "水"),
    "later_zhou.csv": ("後周", "五代十國", "木"),
    "yang_wu.csv": ("吳", "五代十國", ""),
    "southern_tang.csv": ("南唐", "五代十國", ""),
    "wuyue.csv": ("吳越", "五代十國", ""),
    "ma_chu.csv": ("楚", "五代十國", ""),
    "min.csv": ("閩", "五代十國", ""),
    "min_others.csv": None,
    "southern_han.csv": ("南漢", "五代十國", ""),
    "southern_han_others.csv": None,
    "former_shu.csv": ("前蜀", "五代十國", ""),
    "later_shu.csv": ("後蜀", "五代十國", ""),
    "jingnan.csv": ("荊南", "五代十國", ""),
    "northern_han.csv": ("北漢", "五代十國", ""),
    "northern_song.csv": ("北宋", "宋朝", "火"),
    "northern_song_others.csv": None,
    "southern_song.csv": ("南宋", "宋朝", "火"),
    "southern_song_others.csv": None,
    "liao.csv": ("遼", "遼朝", "水"),
    "northern_liao.csv": ("北遼", "遼朝", "水"),
    "northwestern_liao.csv": ("西北遼", "遼朝", "水"),
    "liao_others.csv": None,
    "western_liao.csv": ("西遼", "遼朝", "水"),
    "western_xia.csv": ("西夏", "西夏", ""),
    "western_xia_others.csv": None,
    "jin.csv": ("金", "金朝", ("金土", 1202)),
    "jin_others.csv": None,
    "yuan.csv": ("元", "元朝", ""),
    "northern_yuan.csv": ("北元", "元朝", ""),
    "yuan_others.csv": None,
    "ming.csv": ("明", "明朝", ""),
    "ming_others.csv": None,
    "southern_ming.csv": ("南明", "明朝", ""),
    "southern_ming_others.csv": None,
    "mingzheng.csv": ("明鄭", "明朝", ""),
    "southern_ming_others2.csv": None,
    "jin2.csv": ("後金", "清朝", ""),
    "qing.csv": ("清", "清朝", ""),
    "qing_others.csv": None,
    "minguo.csv": None,
}

assert len(CSV_FILES) == 128

CHINESE_TO_ENGLISH = {
    "年號": "name",
    "起訖時間": "duration",
    "備註": "remark",
    "君主": "emperor",
}

era_id = 0
emperor_id = 0
dynasty_id = 0
emperors_in_others = []
eras_with_unknown_emperor = []


def parse_emperor_name(emperor_name):
    if len(emperor_name) <= 3:
        return None, emperor_name

    # Special cases
    if emperor_name == "齊安德王高延宗":
        return "齊安德王", "高延宗"

    for title in ("帝", "可汗", "祖", "宗", "公"):
        index = emperor_name.find(title)
        if index >= 0:
            return (
                emperor_name[: index + len(title)],
                emperor_name[index + len(title) :],
            )

    for idx in range(2, 4):
        if emperor_name[idx] in ("子主王侯"):
            return emperor_name[: idx + 1], emperor_name[idx + 1 :]

    return None, emperor_name


def parse_duration(duration_str, d, start_key="start", end_key="end"):
    duration = duration_str.split("－")
    start = duration[0]
    end = duration[-1]
    # If `end` doesn't contain '年', it's in the same year as `start`
    if "年" not in end:
        index = start.find("年")
        end = start[: index + 1] + end
    d[start_key] = start
    d[end_key] = end
    if "duration" in d:
        del d["duration"]


def compare_years(literal_year: str, digit_year: int):
    is_negative = False
    year_str = literal_year.split("年")[0]
    if year_str.startswith("前"):
        is_negative = True

    year_str = "".join([char for char in year_str if char.isdigit()])
    if not year_str:
        raise ValueError("Invalid literal year")

    year = int(year_str)
    if is_negative:
        year = -year

    return (year > digit_year) - (year < digit_year)


def is_duplicate_emperor(curr_emperor, emperors):
    if not emperors:
        return False

    return curr_emperor["name"] == emperors[-1]["name"] and curr_emperor.get(
        "title", ""
    ) == emperors[-1].get("title", "")


def handle_other_dynasties(
    row_data: dict[str, str],
    emperor: dict[str, str],
    emperors: list[dict[str, str]],
    dynasties: list[dict[str, str]],
    data_copy: list[dict[str, str]],
):
    global emperor_id, dynasty_id

    is_matched = False
    is_from_remark = False

    # Create a new dynasty and move an "other" emperor to this new dynasty,
    # if the current emperor is not a duplicate of the previous emperor.
    def move_emperor_to_dynasty(
        emperor_name,
        dynasty_name,
        display_name=None,
        element=None,
        to_create_dynasty=True,
        offset=1,
    ):
        global dynasty_id, emperor_id
        nonlocal is_matched

        dynasty = None
        curr_emperor = emperor

        if curr_emperor and curr_emperor["name"] == emperor_name:
            is_matched = True

            if element:
                row_data["element"] = element

            # If curr_emperor is duplicate of the previous emperor (title + name)
            # and the new dynasty name is the same as the dynasty of the previous emperor,
            # no change is applied to curr_emperor, no new dynasty is created,
            # and curr_emperor is not added to the emperors list.
            if (
                is_duplicate_emperor(curr_emperor, emperors)
                and dynasty_name == emperors[-1]["dynasty_name"]
            ):
                return dynasty

            curr_emperor["dynasty_name"] = dynasty_name

            if to_create_dynasty:
                curr_emperor["dynasty_id"] = dynasty_id
                dynasty = {
                    "id": dynasty_id,
                    "name": dynasty_name,
                    "emperors": [
                        [
                            curr_emperor["id"],
                            (
                                (
                                    curr_emperor["title"] + " "
                                    if "title" in curr_emperor
                                    else ""
                                )
                                + curr_emperor["name"]
                            ),
                        ]
                    ],
                    "group": "其他",
                }
                if display_name:
                    dynasty["display_name"] = display_name

                dynasties.append(dynasty)
                dynasty_id += 1
            else:
                curr_emperor["dynasty_id"] = dynasty_id - offset
                dynasties[-offset]["emperors"].append(
                    [
                        curr_emperor["id"],
                        (
                            (
                                curr_emperor["title"] + " "
                                if "title" in curr_emperor
                                else ""
                            )
                            + curr_emperor["name"]
                        ),
                    ]
                )

            emperors.append(curr_emperor)
            emperor_id += 1

        return dynasty

    # The emperor has more than dynasties. For example, 朱泚.
    # This function also applies to 黃巢, who has one dynasty and one "other" dynasty.
    def move_emperor_based_on_dynasty_dicts(
        emperor_name: str, eras: dict[str, str], dynasty_display_names: dict[str, str]
    ):
        for era, dynasty_name in eras.items():
            if row_data["name"] == era:
                move_emperor_to_dynasty(
                    emperor_name,
                    dynasty_name,
                    dynasty_display_names.get(dynasty_name, ""),
                )
                break

    # The emperors are in succession of the given dynasty
    # `offset` represents the number of dynasties separating the current emperor's dynasty
    # from its first occurrence.
    def move_successive_emperors_to_dynasty(
        successive_emperors: list[str],
        dynasty_name,
        display_name="",
        to_force_existing_dynasty=False,
        offset=1,
    ):
        for idx, emperor_name in enumerate(successive_emperors):
            if emperor and emperor["name"] == emperor_name:
                if to_force_existing_dynasty:
                    pass
                move_emperor_to_dynasty(
                    emperor_name,
                    dynasty_name,
                    display_name,
                    None,
                    False if to_force_existing_dynasty else idx == 0,
                    offset,
                )

    move_emperor_to_dynasty("公孫述", "成家")
    move_emperor_to_dynasty("劉盆子", "漢", "漢（赤眉軍）")
    move_emperor_to_dynasty("公孫淵", "燕", "燕（公孫淵）")
    move_emperor_to_dynasty("司馬倫", "晉", "晉（司馬倫）", "金")
    move_emperor_to_dynasty("劉尼、張昌", "漢", "漢（劉尼）")
    move_emperor_to_dynasty("司馬保", "晉", "晉（司馬保）", "金")
    move_emperor_to_dynasty("句渠知", "大秦", "秦（句渠知）")
    move_emperor_to_dynasty("張琚", "秦", "秦（張琚）")
    move_emperor_to_dynasty("張育", "蜀", "蜀（張育）")
    move_emperor_to_dynasty("張大豫", "涼", "涼（張大豫）")
    move_emperor_to_dynasty("竇衝", "秦", "秦（竇衝）")
    move_successive_emperors_to_dynasty(["翟遼", "翟釗"], "魏", "翟魏")
    move_successive_emperors_to_dynasty(["桓玄", "桓謙"], "楚", "桓楚")
    move_emperor_to_dynasty("慕容詳", "燕", "燕（慕容詳）")
    move_emperor_to_dynasty("慕容麟", "燕", "燕（慕容麟）")
    move_emperor_to_dynasty("蘭汗", "燕", "燕（蘭汗）")
    move_emperor_to_dynasty("李寶", "涼", "後西涼")
    move_emperor_to_dynasty("程道養", "蜀", "蜀（程道養）")
    move_emperor_to_dynasty("楊難當", "大秦", "秦（楊難當）")
    move_emperor_to_dynasty("劉渾", "楚", "楚（劉渾）")
    move_emperor_to_dynasty("劉子勛", "宋", "宋（劉子勛）", "水")
    move_emperor_to_dynasty("唐㝢之", "吳", "吳（唐㝢之）")
    move_emperor_to_dynasty("元愉", "魏", "魏（元愉）", "水")
    move_emperor_to_dynasty("莫折念生", "秦", "秦（莫折念生）")
    move_emperor_to_dynasty("葛榮", "齊", "齊（葛榮）")
    move_emperor_to_dynasty("蕭寶夤", "齊", "齊（蕭寶夤）")
    move_emperor_to_dynasty("邢杲", "漢", "漢（邢杲）")
    move_emperor_to_dynasty("万俟醜奴", "大趙", "趙（万俟醜奴）")
    move_emperor_to_dynasty("元顥", "魏", "魏（元顥）", "水")
    move_emperor_to_dynasty("元悅", "魏", "魏（元悅）", "水")
    move_emperor_to_dynasty("蕭正德", "梁", "蕭正德", "火")
    move_emperor_to_dynasty("侯景", "漢", "漢（侯景）")
    move_emperor_to_dynasty("蕭紀", "梁", "梁（蕭紀）", "火")
    move_emperor_to_dynasty("蕭莊", "梁", "梁（蕭莊）", "火")
    move_emperor_to_dynasty("高紹義", "齊", "齊（高紹義）", "木")
    move_emperor_to_dynasty("林士弘", "楚", "楚（林士弘）")
    move_emperor_to_dynasty("竇建德", "夏", "夏（竇建德）")
    move_emperor_to_dynasty("李密", "魏", "魏（李密）")
    move_emperor_to_dynasty("劉武周", "漢", "漢（劉武周）")
    move_emperor_to_dynasty("薛舉", "秦", "秦（薛舉）")
    move_emperor_to_dynasty("李軌", "涼", "涼（李軌）")
    move_emperor_to_dynasty("蕭銑", "梁", "梁（蕭銑）", "火")
    move_emperor_to_dynasty("梁師都", "梁", "梁（梁師都）")
    move_emperor_to_dynasty("宇文化及", "許", "許（宇文化及）")
    move_emperor_to_dynasty("王世充", "鄭", "鄭（王世充）")
    move_emperor_to_dynasty("朱粲", "楚", "楚（朱粲）")
    move_emperor_to_dynasty("高開道", "燕", "燕（高開道）")
    move_emperor_to_dynasty("沈法興", "梁", "梁（沈法興）")
    move_emperor_to_dynasty("李子通", "吳", "吳（李子通）")
    move_emperor_to_dynasty("輔公祏", "宋", "宋（輔公祏）")
    move_emperor_to_dynasty("李重福", "唐", "唐（李重福）", "土")
    move_successive_emperors_to_dynasty(
        ["安祿山", "安慶緒", "史思明", "史朝義"], "大燕", "大燕（安祿山）"
    )
    move_emperor_to_dynasty("段子璋", "梁", "梁（段子璋）")
    move_emperor_based_on_dynasty_dicts(
        "朱泚", {"應天": "秦", "天皇": "漢"}, {"秦": "秦（朱泚）", "漢": "漢（朱泚）"}
    )
    move_emperor_to_dynasty("李希烈", "楚", "楚（李希烈）")
    move_emperor_based_on_dynasty_dicts(
        "黃巢", {"金統": "大齊"}, {"大齊": "大齊（黃巢）"}
    )
    move_emperor_to_dynasty("劉守光", "大燕", "大燕（劉守光）")
    move_emperor_to_dynasty("李熅", "唐", "唐（李熅）", "土")
    move_emperor_to_dynasty("董昌", "大越羅平")
    move_emperor_to_dynasty("李茂貞", "岐")
    move_emperor_to_dynasty("朱文進", "閩", "閩（朱文進）")
    move_emperor_to_dynasty("張遇賢", "中天八國")
    move_emperor_to_dynasty("李順", "大蜀", "蜀（李順）")
    move_emperor_to_dynasty("王均", "大蜀", "蜀（王均）")
    move_emperor_to_dynasty("王則", "安陽")
    move_emperor_based_on_dynasty_dicts("儂智高", {"景瑞": "南天", "啟曆": "大南"}, {})
    move_emperor_to_dynasty("趙旉", "南宋", "南宋（趙旉）", "火")
    move_emperor_to_dynasty("劉豫", "大齊", "齊（劉豫）")
    move_emperor_to_dynasty("阿謝", "自杞國")
    move_emperor_to_dynasty("耶律留哥", "東遼")
    move_emperor_to_dynasty("蒲鮮萬奴", "東夏")
    move_successive_emperors_to_dynasty(
        ["耶律廝不", "耶律乞奴", "耶律金山"], "東遼", "", True, 2
    )
    move_emperor_to_dynasty("楊鎮龍", "大興")
    move_emperor_to_dynasty("陳空崖", "羅平")
    move_emperor_to_dynasty("徐壽輝", "宋", "宋（徐壽輝）")
    move_emperor_to_dynasty("張士誠", "大周", "大周（張士誠）")
    move_emperor_to_dynasty("韓林兒", "宋", "宋（韓林兒）")
    move_successive_emperors_to_dynasty(["陳友諒", "陳理"], "漢", "陳漢")
    move_emperor_based_on_dynasty_dicts("明玉珍", {"天統": "大夏"}, {"大夏": "明夏"})
    move_successive_emperors_to_dynasty(["明昇"], "明夏", "", True)
    move_emperor_to_dynasty("陳鑑胡", "太平")
    move_emperor_to_dynasty("朱徽煠", "明", "明（朱徽煠）")
    move_emperor_to_dynasty("也先", "元", "元（瓦剌）")
    move_emperor_to_dynasty("王斌", "極樂")
    move_emperor_to_dynasty("劉通", "漢", "漢（劉通）")
    move_emperor_to_dynasty("朱宸濠", "明", "明（朱宸濠）")
    move_emperor_to_dynasty("張璉", "飛龍")
    move_emperor_to_dynasty("蔡伯貫", "大唐", "唐（蔡伯貫）")
    move_emperor_to_dynasty("奢崇明", "大梁", "梁（奢崇明）")
    # 大順 （1643年—1646年）
    # 《甲申纪事》“贼云以水德王，衣服尚蓝。故军中俱穿蓝，官帽亦用蓝。”
    move_emperor_to_dynasty("李自成", "大順", None, "水")
    move_emperor_to_dynasty("張獻忠", "大西")
    move_emperor_to_dynasty("劉公顯", "後漢", "後漢（劉公顯）")
    move_emperor_to_dynasty("朱亨嘉", "南明", "南明（朱亨嘉）")
    move_emperor_to_dynasty("朱以海", "南明", "南明（朱以海）")
    move_emperor_to_dynasty("朱聿𨮁", "南明", "南明（朱聿𨮁）")
    move_emperor_to_dynasty("朱常清", "南明", "南明（朱常清）")
    move_emperor_to_dynasty("宮文彩", "大順", "大順（宮文彩）")
    move_successive_emperors_to_dynasty(["吳三桂", "吳世璠"], "吳周")
    move_emperor_to_dynasty("朱一貴", "大明", "明（朱一貴）")
    move_emperor_to_dynasty("李文成", "大明", "明（李文成）")
    move_emperor_to_dynasty("朱毛俚", "後明", "明（朱毛俚）")
    move_emperor_to_dynasty("洪秀全", "太平天國")
    move_emperor_based_on_dynasty_dicts(
        "陳開", {"洪德": "大成"}, {"大成": "大成（陳開）"}
    )
    move_emperor_to_dynasty("唐景崧、劉永福", "臺灣民主國")
    move_emperor_to_dynasty("八世哲布尊丹巴呼圖克圖", "大蒙古國", "博克多汗國")
    move_emperor_to_dynasty("袁世凱", "中華帝國")
    move_emperor_to_dynasty("察都·若巴", "大清", "清（察都·若巴）")
    move_emperor_to_dynasty("馬士偉", "新明國")
    move_emperor_to_dynasty("溥儀", "滿洲國")

    # This line MUST BE before the invokes of add_emperor_from_remark()
    data_copy.append(row_data)

    # The second emperor is in the remark.
    # The first emperor and second emperor share a same era.
    def add_emperor_from_remark(
        first_emperor_name,
        second_emperor_name,
        dynasty_name,
        display_name,
        first_regnal_year=None,
        final_regnal_year=None,
        first_era_start=None,
        first_era_end=None,
        second_era_start=None,
        second_era_end=None,
    ):
        global dynasty_id, emperor_id
        nonlocal is_from_remark
        if emperor and emperor["name"] == first_emperor_name:
            dynasty = move_emperor_to_dynasty(
                first_emperor_name, dynasty_name, display_name
            )
            # Adjust the following values, because there are more emperors in this "other" dynasty
            if dynasty:
                dynasty_id -= 1
                dynasty["emperors"].append(
                    [
                        emperor["id"] + 1,
                        second_emperor_name,
                    ]
                )

                is_from_remark = True
                row_data["start"] = first_era_start
                row_data["end"] = first_era_end

                second_emperor = {
                    "id": emperor["id"] + 1,
                    "name": second_emperor_name,
                    "dynasty_id": dynasty_id,
                    "dynasty_name": dynasty_name,
                    "first_regnal_year": first_regnal_year,
                    "final_regnal_year": final_regnal_year,
                }
                emperors.append(second_emperor)

                emperor_id += 1
                dynasty_id += 1

                d_copy = copy.deepcopy(row_data)
                d_copy["start"] = second_era_start
                d_copy["end"] = second_era_end
                d_copy["emperor_id"] = second_emperor["id"]
                data_copy.append(d_copy)

    add_emperor_from_remark(
        "沮渠無諱",
        "沮渠安周",
        "涼",
        "涼（沮渠無諱）",
        "444年",
        "460年",
        "443年",
        "444年",
        "444年",
        "460年",
    )

    return is_matched, is_from_remark


def process_eras(data_copy, elements=None):
    global era_id

    eras = []
    for d in data_copy:
        if not is_header(d):
            d["id"] = era_id
            era_id += 1

            if d["end"] and elements:
                if isinstance(elements, tuple):
                    try:
                        if compare_years(d["end"], elements[1]) < 0:
                            if elements[0][0] != "無":
                                d["element"] = elements[0][0]
                        else:
                            d["element"] = elements[0][1]
                    except ValueError:
                        pass
                else:
                    d["element"] = elements

            eras.append(d)
    return eras


def is_header(row_data: dict[str, str]):
    return len(set(row_data.values())) == 1


def has_emperor_info(row_data: dict[str, str], attributes: tuple = None):
    if is_regular_dynasty(attributes):
        return is_header(row_data)
    else:
        return "emperor" in row_data


def is_regular_dynasty(attributes: tuple):
    return bool(attributes)


def process_era_file(csv_file: Path, attributes: tuple, dynasties: list[dict]):
    """
    Processes a CSV file containing dynasty data and updates the dynasties list.

    The csv_file contains data for either:
    1. A single regular dynasty, or
    2. One or more special (other) dynasties.

    The type of data contained in the csv_file is determined by the attributes parameter.

    Args:
        csv_file (Path): The path to the CSV file containing dynasty data.
        attributes (Tuple): Attributes of the data in the CSV file.
        dynasties (List[Dict]): The list of existing dynasties to be updated.

    Returns:
        tuple[list[dict], list[dict]]: A tuple containing processed era data and emperor data.
    """
    global era_id, emperor_id, dynasty_id

    # Read the CSV file and convert it to a list of dictionaries
    with open(csv_file, mode="r", encoding="utf-8-sig") as file:
        data = [
            {
                CHINESE_TO_ENGLISH[k]: v
                for k, v in row.items()
                if k in CHINESE_TO_ENGLISH
            }
            for row in csv.DictReader(file)
        ]

    emperors = []
    data_copy = []

    if is_regular_dynasty(attributes):
        dynasty_name, dynasty_group, elements = attributes
        dynasty_emperors = []
        # 唐 is split into two parts; 李顯 and 李旦 appear in both
        if dynasty_name == "唐" and dynasties[-1]["name"] == "武周":
            dynasty_emperors = dynasties[-2]["emperors"]
            dynasty_id -= 2
        else:
            dynasty = {
                "id": dynasty_id,
                "name": dynasty_name,
                # "emperors": dynasty_emperors,
                "group": dynasty_group,
            }
            dynasties.append(dynasty)

        for d in data:
            # Process emperor
            # The current row contains information about an emperor if
            # it has any cell value that is duplicated across all columns,
            # or it contains a cell in a column named "emperor".
            emperor = {}
            if is_header(d):
                emperor["id"] = emperor_id
                emperor["dynasty_id"], emperor["dynasty_name"] = (
                    dynasty_id,
                    dynasty_name,
                )
                match = re.match(r"(.+)（([^）]+)）", d["name"])
                if match:
                    name, reign_duration = match.groups()
                    name_tuple = parse_emperor_name(name)
                    if name_tuple[0]:
                        emperor["title"] = name_tuple[0]
                    emperor["name"] = name_tuple[1]

                    parts = reign_duration.split("：")
                    if len(parts) > 1:
                        parse_duration(
                            parts[1],
                            emperor,
                            "first_regnal_year",
                            "final_regnal_year",
                        )
                else:
                    emperor["name"] = d["name"]

                dynasty_emperors.append(
                    [
                        emperor["id"],
                        f"{emperor.get('title', '')} {emperor['name']}".strip(),
                    ]
                )

                emperors.append(emperor)
                emperor_id += 1
            else:
                parse_duration(d["duration"], d)
                d["emperor_id"] = emperor_id - 1

            data_copy.append(d)

            if d["name"] == "乾祐" and emperors[-1]["name"] == "劉知遠":
                emperor = {
                    "id": emperor_id,
                    "title": "漢隱帝",
                    "name": "劉承祐",
                    "dynasty_id": dynasty_id,
                    "dynasty_name": dynasty_name,
                    "first_regnal_year": "948年",
                    "final_regnal_year": "951年",
                }
                emperors.append(emperor)
                emperor_id += 1

                dynasty_emperors.append(
                    [
                        emperor["id"],
                        f"{emperor.get('title', '')} {emperor['name']}".strip(),
                    ]
                )

                data_copy[-1].update({"start": "948年正月", "end": "948年正月"})
                data_copy.append(data_copy[-1].copy())
                data_copy[-1].update(
                    {"emperor_id": emperor_id - 1, "start": "948年正月", "end": "950年"}
                )

        eras = process_eras(data_copy, elements)

        if dynasty_name == "唐" and dynasties[-1]["name"] == "武周":
            dynasties[-2]["emperors"] = dynasty_emperors
            dynasty_id += 2
        else:
            dynasties[-1]["emperors"] = dynasty_emperors
            dynasty_id += 1
    else:
        # Other dynasties
        for d in data:
            is_matched = False
            is_from_remark = False
            emperor = {}
            if has_emperor_info(d):
                # Process emperor
                # The current row contains information about an emperor if
                # it has any cell value that is duplicated across all columns,
                # or it contains a cell in a column named "emperor".
                emperor["id"] = emperor_id
                emperor["dynasty_id"], emperor["dynasty_name"] = "其他", "其他"
                emperor["name"] = d["emperor"]
                parse_duration(d["duration"], d)
                del d["emperor"]

                is_matched, is_from_remark = handle_other_dynasties(
                    d, emperor, emperors, dynasties, data_copy
                )

                if not is_matched:
                    emperors_in_others.append(
                        [
                            (
                                emperor["id"] - 1
                                if is_duplicate_emperor(emperor, emperors)
                                else emperor["id"]
                            ),
                            emperor["name"],
                        ]
                    )
            else:
                # no emperor in row data
                is_matched = True
                parse_duration(d["duration"], d)
                eras_with_unknown_emperor.append(d)
                data_copy.append(d)

            if not is_matched and not is_duplicate_emperor(emperor, emperors):
                emperors.append(emperor)
                emperor_id += 1

            if is_from_remark:
                d["emperor_id"] = emperor_id - 2
            else:
                d["emperor_id"] = emperor_id - 1

        eras = process_eras(data_copy)

    return eras, emperors


# Ensure all directory paths are correctly set up
def setup_directories():
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / "data"
    output_dir = base_dir.parent / "src" / "data"
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    return input_dir, output_dir


# Save data to JSON file
def save_to_json(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving file {filename}: {e}")


def main():
    input_dir, output_dir = setup_directories()

    emperors = []
    eras = []
    dynasties = []

    for filename, attributes in CSV_FILES.items():
        filepath = input_dir / filename
        if not filepath.exists():
            print(f"Warning: File {filepath} not found. Skipping.")
            continue

        era_data, emperor_data = process_era_file(filepath, attributes, dynasties)
        eras.extend(era_data)
        emperors.extend(emperor_data)

    # Special cases
    # Process eras with unknown emperors
    unknown_emperor = {
        "id": emperor_id,
        "name": "？",
        "dynasty_id": dynasty_id,
        "dynasty_name": "其他",
    }
    emperors.append(unknown_emperor)
    emperors_in_others.append([unknown_emperor["id"], unknown_emperor["name"]])

    # Add "其他" dynasty
    dynasties.append(
        {
            "id": dynasty_id,
            "name": "其他",
            "emperors": emperors_in_others,
            "group": "其他",
        }
    )

    for emperor in emperors:
        if "dynasty_id" in emperor and emperor["dynasty_id"] == "其他":
            emperor["dynasty_id"] = dynasty_id

    for e in eras_with_unknown_emperor:
        e["emperor_id"] = emperor_id

    files_to_save = {
        output_dir / "emperors.json": emperors,
        output_dir / "eras.json": eras,
        output_dir / "dynasties.json": dynasties,
    }

    for file_path, data in files_to_save.items():
        save_to_json(data, file_path)


if __name__ == "__main__":
    main()
