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
    "xin_gengshi_others.csv": ("", "", ""),
    "eastern_han.csv": ("東漢", "漢朝", "火"),
    "eastern_han_others.csv": ("", "", ""),
    "cao_wei.csv": ("曹魏", "三國", "土"),
    "cao_wei_others.csv": ("", "", ""),
    "shu_han.csv": ("蜀漢", "三國", "火"),
    "sun_wu.csv": ("孫吳", "三國", "木"),
    "western_jin.csv": ("西晉", "晉朝", "金"),
    "western_jin_others.csv": ("", "", ""),
    "eastern_jin.csv": ("東晉", "晉朝", "金"),
    "eastern_jin_others.csv": ("", "", ""),
    "han_zhao.csv": ("漢趙", "十六國", ("無水", 319)),
    "han_zhao_others.csv": ("", "", ""),
    "cheng_han.csv": ("成漢", "十六國", ""),
    "former_liang.csv": ("前涼", "十六國", ""),
    "former_liang_others.csv": ("", "", ""),
    "later_zhao.csv": ("後趙", "十六國", "水"),
    "ran_wei.csv": ("冉魏", "十六國", ""),
    "later_zhao_others.csv": ("", "", ""),
    "dai.csv": ("代", "十六國", ""),
    "former_yan.csv": ("前燕", "十六國", ("水木", 364)),
    "former_qin.csv": ("前秦", "十六國", "木"),
    "former_qin_others.csv": ("", "", ""),
    "later_qin.csv": ("後秦", "十六國", "火"),
    "later_yan.csv": ("後燕", "十六國", ""),
    "later_yan_others.csv": ("", "", ""),
    "western_yan.csv": ("西燕", "十六國", ""),
    "western_qin.csv": ("西秦", "十六國", ""),
    "later_liang.csv": ("後涼", "十六國", ""),
    "southern_liang.csv": ("南涼", "十六國", ""),
    "southern_yan.csv": ("南燕", "十六國", ""),
    "southern_yan_others.csv": ("", "", ""),
    "western_liang.csv": ("西涼", "十六國", ""),
    "western_liang_others.csv": ("", "", ""),
    "xia.csv": ("夏", "十六國", ""),
    "northern_yan.csv": ("北燕", "十六國", ""),
    "northern_liang.csv": ("北涼", "十六國", ""),
    "northern_liang_others.csv": ("", "", ""),
    "liu_song.csv": ("劉宋", "南北朝", "水"),
    "liu_song_others.csv": ("", "", ""),
    "southern_qi.csv": ("南齊", "南北朝", "木"),
    "southern_qi_others.csv": ("", "", ""),
    "xiao_liang.csv": ("南梁", "南北朝", "火"),
    "xiao_liang_others.csv": ("", "", ""),
    "western_xiao_liang.csv": ("西梁", "南北朝", ""),
    "southern_chen.csv": ("南陳", "南北朝", "土"),
    "northern_wei.csv": ("北魏", "南北朝", ("土水", 490)),
    "northern_wei_others.csv": ("", "", ""),
    "eastern_wei.csv": ("東魏", "南北朝", "水"),
    "eastern_wei_others.csv": ("", "", ""),
    "western_wei.csv": ("西魏", "南北朝", "水"),
    "northern_qi.csv": ("北齊", "南北朝", "木"),
    "northern_qi_others.csv": ("", "", ""),
    "northern_zhou.csv": ("北周", "南北朝", "木"),
    "northern_zhou_others.csv": ("", "", ""),
    "goguryeo.csv": ("高句麗", "南北朝", ""),
    "goguryeo_others.csv": ("", "", ""),
    "rouran.csv": ("柔然", "南北朝", ""),
    "gaochang.csv": ("高昌", "南北朝", ""),
    "gaochang_others.csv": ("", "", ""),
    "sui.csv": ("隋", "隋朝", "火"),
    "sui_others.csv": ("", "", ""),
    "tang.csv": ("唐", "唐朝", "土"),
    "wu_zhou.csv": ("武周", "唐朝", ""),
    "tang2.csv": ("唐", "唐朝", "土"),
    "tang_others.csv": ("", "", ""),
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
    "nanzhao_dali_others.csv": ("", "", ""),
    "zhu_liang.csv": ("後梁", "五代十國", "金"),
    "zhu_liang_others.csv": ("", "", ""),
    "hedong.csv": ("河東", "五代十國", ""),
    "later_tang.csv": ("後唐", "五代十國", "土"),
    "later_jin.csv": ("後晉", "五代十國", "金"),
    "later_jin_others.csv": ("", "", ""),
    "later_han.csv": ("後漢", "五代十國", "水"),
    "later_zhou.csv": ("後周", "五代十國", "木"),
    "yang_wu.csv": ("吳", "五代十國", ""),
    "southern_tang.csv": ("南唐", "五代十國", ""),
    "wuyue.csv": ("吳越", "五代十國", ""),
    "ma_chu.csv": ("楚", "五代十國", ""),
    "min.csv": ("閩", "五代十國", ""),
    "min_others.csv": ("", "", ""),
    "southern_han.csv": ("南漢", "五代十國", ""),
    "southern_han_others.csv": ("", "", ""),
    "former_shu.csv": ("前蜀", "五代十國", ""),
    "later_shu.csv": ("後蜀", "五代十國", ""),
    "jingnan.csv": ("荊南", "五代十國", ""),
    "northern_han.csv": ("北漢", "五代十國", ""),
    "northern_song.csv": ("北宋", "宋朝", "火"),
    "northern_song_others.csv": ("", "", ""),
    "southern_song.csv": ("南宋", "宋朝", "火"),
    "southern_song_others.csv": ("", "", ""),
    "liao.csv": ("遼", "遼朝", "水"),
    "northern_liao.csv": ("北遼", "遼朝", "水"),
    "northwestern_liao.csv": ("西北遼", "遼朝", "水"),
    "liao_others.csv": ("", "", ""),
    "western_liao.csv": ("西遼", "遼朝", "水"),
    "western_xia.csv": ("西夏", "西夏", ""),
    "western_xia_others.csv": ("", "", ""),
    "jin.csv": ("金", "金朝", ("金土", 1202)),
    "jin_others.csv": ("", "", ""),
    "yuan.csv": ("元", "元朝", ""),
    "northern_yuan.csv": ("北元", "元朝", ""),
    "yuan_others.csv": ("", "", ""),
    "ming.csv": ("明", "明朝", ""),
    "ming_others.csv": ("", "", ""),
    "southern_ming.csv": ("南明", "明朝", ""),
    "southern_ming_others.csv": ("", "", ""),
    "mingzheng.csv": ("明鄭", "明朝", ""),
    "southern_ming_others2.csv": ("", "", ""),
    "jin2.csv": ("後金", "清朝", ""),
    "qing.csv": ("清", "清朝", ""),
    "qing_others.csv": ("", "", ""),
    "minguo.csv": ("民國", "民國", ""),
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
prev_emperor = None
emperors_in_others = []
# 唐 is split into two parts; 李顯 and 李旦 appear in both
tang_dynasty = None


def parse_emperor_name(emperor_name):
    if len(emperor_name) <= 3:
        return None, emperor_name

    # Special cases
    if emperor_name == "齊安德王高延宗":
        return "齊安德王", "高延宗"

    for title in ("帝", "可汗", "祖", "宗"):
        index = emperor_name.find(title)
        if index >= 0:
            return (
                emperor_name[: index + len(title)],
                emperor_name[index + len(title) :],
            )

    for idx in range(2, 4):
        if emperor_name[idx] in ("子主王侯公"):
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


def get_dynasty_id(dynasty_name):
    global dynasty_id
    if not dynasty_name:
        return "其他", "其他"
    if dynasty_name == "唐" and tang_dynasty:
        return dynasty_id - 2, "唐"
    return dynasty_id, dynasty_name


def process_emperors(d, attributes):
    global emperor_id, dynasty_id

    emperor = {"id": emperor_id}
    emperor["dynasty_id"], emperor["dynasty_name"] = get_dynasty_id(attributes[0])

    if "emperor" in d:
        emperor["name"] = d["emperor"]
        del d["emperor"]
        emperors_in_others.append(emperor["name"])
    else:
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
                    parts[1], emperor, "first_regnal_year", "final_regnal_year"
                )
        else:
            emperor["name"] = d["name"]

    return emperor


def is_duplicate_emperor(emperor):
    global prev_emperor
    if prev_emperor:
        return emperor["name"] == prev_emperor["name"] and emperor.get(
            "title", ""
        ) == prev_emperor.get("title", "")
    return emperor is None


def process_era_row(d):
    parse_duration(d["duration"], d)
    del d["duration"]
    d["emperor_id"] = emperor_id - 1


def handle_special_cases(d, emperor, emperors, data_copy, dynasties):
    global emperor_id, dynasty_id

    if emperor and emperor["name"] == "侯景":
        # 漢（侯景）
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "漢",
                "emperors": [emperor["name"]],
                "group": "其他",
                "display_name": "漢（侯景）",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "漢"
        dynasty_id += 1
        emperors_in_others.remove(emperor["name"])

    if emperor and emperor["name"] == "安祿山":
        # 大燕（安祿山）
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "大燕",
                "emperors": ["安祿山", "安慶緒"],
                "group": "其他",
                "display_name": "大燕（安祿山）",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "大燕"
        emperors_in_others.remove(emperor["name"])

    if emperor and emperor["name"] == "安慶緒":
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "大燕"
        emperors_in_others.remove(emperor["name"])
        if d["name"] == "天成":
            dynasty_id += 1

    if emperor and emperor["name"] == "劉守光":
        # 桀燕
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "大燕",
                "emperors": [emperor["name"]],
                "group": "其他",
                "display_name": "大燕（劉守光）",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "大燕"
        dynasty_id += 1
        emperors_in_others.remove(emperor["name"])

    if emperor and emperor["name"] == "董昌":
        # 大越羅平國
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "大越羅平國",
                "emperors": [emperor["name"]],
                "group": "其他",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "大越羅平國"
        dynasty_id += 1
        emperors_in_others.remove(emperor["name"])

    if d["name"] == "永昌" and emperor and emperor["name"] == "李自成":
        # 大順 （1643年—1646年）
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "大順",
                "emperors": [emperor["name"]],
                "group": "其他",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "大順"
        dynasty_id += 1
        # 《甲申纪事》“贼云以水德王，衣服尚蓝。故军中俱穿蓝，官帽亦用蓝。”
        d["element"] = "水"
        emperors_in_others.remove(emperor["name"])

    if emperor and emperor["name"] == "洪秀全":
        # 太平天國
        dynasties.append(
            {
                "id": dynasty_id,
                "name": "太平天國",
                "emperors": [emperor["name"]],
                "group": "其他",
            }
        )
        emperor["dynasty_id"] = dynasty_id
        emperor["dynasty_name"] = "太平天國"
        dynasty_id += 1
        emperors_in_others.remove(emperor["name"])

    if d["name"] == "乾祐" and emperor and emperor["name"] == "劉知遠":
        d["start"] = "948年正月"
        d["end"] = "948年正月"
        data_copy.append(d)

        d_copy = copy.deepcopy(d)
        d_copy["start"] = "948年正月"
        d_copy["end"] = "950年"
        d_copy["emperor_id"] = emperor_id
        data_copy.append(d_copy)

        emperors.append(
            {
                "id": emperor_id,
                "dynasty_id": dynasty_id,
                "dynasty_name": "後漢",
                "title": "漢隱帝",
                "name": "劉承祐",
                "first_regnal_year": "948年",
                "final_regnal_year": "951年",
            }
        )
        emperor_id += 1
    else:
        data_copy.append(d)


def process_eras(data_copy, attributes):
    global era_id

    eras = []
    for d in data_copy:
        if len(set(d.values())) > 1:
            d["id"] = era_id
            era_id += 1

            if d["end"] and attributes[2]:
                if isinstance(attributes[2], tuple):
                    try:
                        if compare_years(d["end"], attributes[2][1]) < 0:
                            if attributes[2][0][0] != "無":
                                d["element"] = attributes[2][0][0]
                        else:
                            d["element"] = attributes[2][0][1]
                    except ValueError:
                        pass
                else:
                    d["element"] = attributes[2]

            eras.append(d)
    return eras


def update_dynasties(dynasties, attributes, dynasty_emperors):
    global dynasty_id, tang_dynasty

    if attributes[0] == "唐" and tang_dynasty:
        for emperor in dynasty_emperors:
            if emperor not in tang_dynasty["emperors"]:
                tang_dynasty["emperors"].append(emperor)
    else:
        dynasty = {
            "id": dynasty_id,
            "name": attributes[0],
            "emperors": dynasty_emperors,
            "group": attributes[1],
        }
        dynasties.append(dynasty)
        if attributes[0] == "唐":
            tang_dynasty = dynasty
        dynasty_id += 1


def convert(csv_file, attributes, dynasties: list[dict]):
    global prev_emperor, era_id, emperor_id

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
    dynasty_emperors = []

    data_copy = []
    for d in data:
        emperor = None
        # Check if a row has any cell value that is duplicated across all columns,
        # or if the row contains a cell in a column named "emperor".
        # If either condition is met, process the emperor data.
        if len(set(d.values())) == 1 or "emperor" in d:
            emperor = process_emperors(d, attributes)
            if emperor and not is_duplicate_emperor(emperor):
                emperors.append(emperor)
                emperor_id += 1

            if attributes[0]:
                dynasty_emperors.append(
                    f"{emperor.get('title', '')} {emperor['name']}".strip()
                )

            prev_emperor = emperor

        if len(set(d.values())) > 1:
            process_era_row(d)

        handle_special_cases(d, prev_emperor, emperors, data_copy, dynasties)

    eras = process_eras(data_copy, attributes)

    if attributes[0]:
        update_dynasties(dynasties, attributes, dynasty_emperors)

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

        era_data, emperor_data = convert(filepath, attributes, dynasties)
        eras.extend(era_data)
        emperors.extend(emperor_data)

    # Special cases
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
        if emperor["dynasty_id"] == "其他":
            emperor["dynasty_id"] = dynasty_id

    # 後漢
    for dynasty in dynasties:
        if dynasty["name"] == "後漢":
            dynasty["emperors"].append("漢隱帝 劉承祐")

    files_to_save = {
        output_dir / "emperors.json": emperors,
        output_dir / "eras.json": eras,
        output_dir / "dynasties.json": dynasties,
    }

    for file_path, data in files_to_save.items():
        save_to_json(data, file_path)


if __name__ == "__main__":
    main()
