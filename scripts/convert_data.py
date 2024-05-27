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
# - 十六國的德運：《王化與山險》，羅新，2019
# - 金朝的德運：《正統與華夷：中國傳統政治文化研究》，劉浦江，2017
CSV_FILES = {
    'western_han.csv': ('西漢', '漢朝', ('火土', -104)),
    'xin.csv': ('新', '漢朝', '土'),
    'gengshi.csv': ('更始', '漢朝', ''),
    'xin_gengshi_others.csv': ('', '', ''),
    'eastern_han.csv': ('東漢', '漢朝', '火'),
    'eastern_han_others.csv': ('', '', ''),
    'cao_wei.csv': ('曹魏', '三國', '土'),
    'cao_wei_others.csv': ('', '', ''),
    'shu_han.csv': ('蜀漢', '三國', '火'),
    'sun_wu.csv': ('孫吳', '三國', '木'),
    'western_jin.csv': ('西晉', '晉朝', '金'),
    'western_jin_others.csv': ('', '', ''),
    'eastern_jin.csv': ('東晉', '晉朝', '金'),
    'eastern_jin_others.csv': ('', '', ''),
    'han_zhao.csv': ('漢趙', '十六國', ('無水', 319)),
    'han_zhao_others.csv': ('', '', ''),
    'cheng_han.csv': ('成漢', '十六國', ''),
    'former_liang.csv': ('前涼', '十六國', ''),
    'former_liang_others.csv': ('', '', ''),
    'later_zhao.csv': ('後趙', '十六國', '水'),
    'ran_wei.csv': ('冉魏', '十六國', ''),
    'later_zhao_others.csv': ('', '', ''),
    'dai.csv': ('代', '十六國', ''),
    'former_yan.csv': ('前燕', '十六國', ('水木', 364)),
    'former_qin.csv': ('前秦', '十六國', '木'),
    'former_qin_others.csv': ('', '', ''),
    'later_qin.csv': ('後秦', '十六國', '火'),
    'later_yan.csv': ('後燕', '十六國', ''),
    'later_yan_others.csv': ('', '', ''),
    'western_yan.csv': ('西燕', '十六國', ''),
    'western_qin.csv': ('西秦', '十六國', ''),
    'later_liang.csv': ('後涼', '十六國', ''),
    'southern_liang.csv': ('南涼', '十六國', ''),
    'southern_yan.csv': ('南燕', '十六國', ''),
    'southern_yan_others.csv': ('', '', ''),
    'western_liang.csv': ('西涼', '十六國', ''),
    'western_liang_others.csv': ('', '', ''),
    'xia.csv': ('夏', '十六國', ''),
    'northern_yan.csv': ('北燕', '十六國', ''),
    'northern_liang.csv': ('北涼', '十六國', ''),
    'northern_liang_others.csv': ('', '', ''),
    'liu_song.csv': ('劉宋', '南北朝', '水'),
    'liu_song_others.csv': ('', '', ''),
    'southern_qi.csv': ('南齊', '南北朝', '木'),
    'southern_qi_others.csv': ('', '', ''),
    'xiao_liang.csv': ('南梁', '南北朝', '火'),
    'xiao_liang_others.csv': ('', '', ''),
    'western_xiao_liang.csv': ('西梁', '南北朝', ''),
    'southern_chen.csv': ('南陳', '南北朝', '土'),
    'northern_wei.csv': ('北魏', '南北朝', ('土水', 490)),
    'northern_wei_others.csv': ('', '', ''),
    'eastern_wei.csv': ('東魏', '南北朝', '水'),
    'eastern_wei_others.csv': ('', '', ''),
    'western_wei.csv': ('西魏', '南北朝', '水'),
    'northern_qi.csv': ('北齊', '南北朝', '木'),
    'northern_qi_others.csv': ('', '', ''),
    'northern_zhou.csv': ('北周', '南北朝', '木'),
    'northern_zhou_others.csv': ('', '', ''),
    'goguryeo.csv': ('高句麗', '南北朝', ''),
    'goguryeo_others.csv': ('', '', ''),
    'rouran.csv': ('柔然', '南北朝', ''),
    'gaochang.csv': ('高昌', '南北朝', ''),
    'gaochang_others.csv': ('', '', ''),
    'sui.csv': ('隋', '隋朝', '火'),
    'sui_others.csv': ('', '', ''),
    'tang.csv': ('唐', '唐朝', '土'),
    'wu_zhou.csv': ('武周', '唐朝', ''),
    'tang2.csv': ('唐', '唐朝', '土'),
    'tang_others.csv': ('', '', ''),
    'tibet.csv': ('吐蕃', '唐朝', ''),
    'khotan.csv': ('于闐', '唐朝', ''),
    'bohai.csv': ('渤海', '唐朝', ''),
    'dongdan.csv': ('東丹', '唐朝', ''),
    'dingan.csv': ('定安', '唐朝', ''),
    'nanzhao.csv': ('南詔', '唐朝', ''),
    'dachanghe.csv': ('大長和', '唐朝', ''),
    'datianxing.csv': ('大天興', '唐朝', ''),
    'dayining.csv': ('大義寧', '唐朝', ''),
    'dali.csv': ('大理', '唐朝', ''),
    'dazhong.csv': ('大中', '唐朝', ''),
    'dali2.csv': ('後大理', '唐朝', ''),
    'nanzhao_dali_others.csv': ('', '', ''),
    'zhu_liang.csv': ('後梁', '五代十國', '金'),
    'zhu_liang_others.csv': ('', '', ''),
    'hedong.csv': ('河東', '五代十國', ''),
    'later_tang.csv': ('後唐', '五代十國', '土'),
    'later_jin.csv': ('後晉', '五代十國', '金'),
    'later_jin_others.csv': ('', '', ''),
    'later_han.csv': ('後漢', '五代十國', '水'),
    'later_zhou.csv': ('後周', '五代十國', '木'),
    'yang_wu.csv': ('吳', '五代十國', ''),
    'southern_tang.csv': ('南唐', '五代十國', ''),
    'wuyue.csv': ('吳越', '五代十國', ''),
    'ma_chu.csv': ('楚', '五代十國', ''),
    'min.csv': ('閩', '五代十國', ''),
    'min_others.csv': ('', '', ''),
    'southern_han.csv': ('南漢', '五代十國', ''),
    'southern_han_others.csv': ('', '', ''),
    'former_shu.csv': ('前蜀', '五代十國', ''),
    'later_shu.csv': ('後蜀', '五代十國', ''),
    'jingnan.csv': ('荊南', '五代十國', ''),
    'northern_han.csv': ('北漢', '五代十國', ''),
    'northern_song.csv': ('北宋', '宋朝', '火'),
    'northern_song_others.csv': ('', '', ''),
    'southern_song.csv': ('南宋', '宋朝', '火'),
    'southern_song_others.csv': ('', '', ''),
    'liao.csv': ('遼', '遼朝', ''),
    'northern_liao.csv': ('北遼', '遼朝', ''),
    'northwestern_liao.csv': ('西北遼', '遼朝', ''),
    'liao_others.csv': ('', '', ''),
    'western_liao.csv': ('西遼', '遼朝', ''),
    'western_xia.csv': ('西夏', '西夏', ''),
    'western_xia_others.csv': ('', '', ''),
    'jin.csv': ('金', '金朝', ('金土', 1202)),
    'jin_others.csv': ('', '', ''),
    'yuan.csv': ('元', '元朝', ''),
    'northern_yuan.csv': ('北元', '元朝', ''),
    'yuan_others.csv': ('', '', ''),
    'ming.csv': ('明', '明朝', ''),
    'ming_others.csv': ('', '', ''),
    'southern_ming.csv': ('南明', '明朝', ''),
    'southern_ming_others.csv': ('', '', ''),
    'mingzheng.csv': ('明鄭', '明朝', ''),
    'southern_ming_others2.csv': ('', '', ''),
    'jin2.csv': ('後金', '清朝', ''),
    'qing.csv': ('清', '清朝', ''),
    'qing_others.csv': ('', '', ''),
    'minguo.csv': ('民國', '民國', ''),
}

assert len(CSV_FILES) == 128

CHINESE_TO_ENGLISH = {
    '年號': 'name',
    '起訖時間': 'duration',
    '備註': 'remark',
    '君主': 'emperor'
}

era_id = 0
emperor_id = 0
prev_emperor = ''


def parse_emperor_name(emperor_name):
    if len(emperor_name) <= 3:
        return None, emperor_name

    for title in ('帝', '可汗', '祖', '宗'):
        index = emperor_name.find(title)
        if index >= 0:
            return emperor_name[:index + len(title)], emperor_name[index + len(title):]

    for idx in range(2, 4):
        if emperor_name[idx] in ('子主王侯公'):
            return emperor_name[:idx + 1], emperor_name[idx + 1:]

    return None, emperor_name


def parse_duration(duration_str, d, start_key='start', end_key='end'):
    duration = duration_str.split('－')
    start = duration[0]
    end = duration[-1]
    # If `end`` doesn't contain '年', it's in the same year as `start`
    if '年' not in end:
        index = start.find('年')
        end = start[:index + 1] + end
    d[start_key] = start
    d[end_key] = end


def compare_years(literal_year: str, digit_year: int):
    is_negative = False
    year_str = literal_year.split('年')[0]
    if year_str.startswith('前'):
        is_negative = True

    year_str = ''.join([char for char in year_str if char.isdigit()])
    if not year_str:
        raise ValueError('Invalid literal year')

    year = int(year_str)
    if is_negative:
        year = -year

    return (year > digit_year) - (year < digit_year)


def convert(csv_file, attributes, dynasties: list[dict]):
    # Read the CSV file and convert it to a dictionary
    data = []
    with open(csv_file, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(
                {CHINESE_TO_ENGLISH[k]: v for k, v in row.items() if k in CHINESE_TO_ENGLISH})

    emperors = []
    dynasty_emperors = []

    global prev_emperor
    global era_id
    global emperor_id
    for d in data:
        # Add emperor
        # len(set(d.values())) tests whether the element is a valid era
        # or a table title (the values of all keys will be identical)
        if len(set(d.values())) == 1 or 'emperor' in d:
            emperor = {}
            emperor['id'] = emperor_id
            if attributes[0]:
                emperor['dynasty'] = attributes[0]

            # In *_others.csv, emperor name is in a column
            if 'emperor' in d:
                emperor['name'] = d['emperor']
                parse_duration(d['duration'], emperor,
                               'first_regnal_year', 'final_regnal_year')
                del d['emperor']
            else:
                # In all the other tables, emperor takes the entire row
                match = re.match(r"(.+)（([^）]+)）", d['name'])
                if match:
                    name, reign_duration = match.groups()
                    name_tuple = parse_emperor_name(name)
                    if name_tuple[0]:
                        emperor['title'] = name_tuple[0]
                    emperor['name'] = name_tuple[1]

                    parts = reign_duration.split('：')
                    if len(parts) > 1:
                        parse_duration(
                            parts[1], emperor, 'first_regnal_year', 'final_regnal_year')
                else:
                    # If no '在位' in the emperor row
                    emperor['name'] = d['name']

            if emperor['name'] != prev_emperor:
                emperors.append(emperor)
                emperor_id += 1

            if attributes[0]:
                dynasty_emperors += [((emperor['title'] + ' ')
                                      if 'title' in emperor else '') + emperor['name']]

            prev_emperor = emperor['name']

        if len(set(d.values())) > 1:
            parse_duration(d['duration'], d)
            del d['duration']
            d['emperor_id'] = emperor_id - 1

    eras = []
    for d in data:
        if len(set(d.values())) > 1:
            d['id'] = era_id
            era_id += 1

            if d['end'] and attributes[2]:
                if isinstance(attributes[2], tuple):
                    try:
                        if compare_years(d['end'], attributes[2][1]) < 0:
                            if attributes[2][0][0] != '無':
                                d['element'] = attributes[2][0][0]
                        else:
                            d['element'] = attributes[2][0][1]
                    except ValueError:
                        pass
                else:
                    d['element'] = attributes[2]

            eras.append(d)

    # 唐 is split into two parts and 李旦 appears in both.
    # So, we need to handle this special case.
    if attributes[0]:
        dynasty_data = next(
            (d for d in dynasties if d['name'] == attributes[0]), None)

        if dynasty_data:
            for emperor in dynasty_emperors:
                if emperor not in dynasty_data['emperors']:
                    dynasty_data['emperors'].append(emperor)
        else:
            dynasties.append(
                {'name': attributes[0], 'emperors': dynasty_emperors, 'group': attributes[1]})

    return eras, emperors


# Ensure all directory paths are correctly set up
def setup_directories():
    base_dir = Path(__file__).resolve().parent
    input_dir = base_dir / 'data'
    output_dir = base_dir.parent / 'src' / 'data'
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    return input_dir, output_dir


# Save data to JSON file
def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
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

    files_to_save = {
        output_dir / 'emperors.json': emperors,
        output_dir / 'eras.json': eras,
        output_dir / 'dynasties.json': dynasties,
    }

    for file_path, data in files_to_save.items():
        save_to_json(data, file_path)


if __name__ == "__main__":
    main()
