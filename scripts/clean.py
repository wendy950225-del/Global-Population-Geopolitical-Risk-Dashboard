import csv
import json
from pathlib import Path


# 找到專案根目錄
ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = ROOT / "data" / "raw.txt"
OUTPUT_FILE = ROOT / "data" / "cleaned.json"


# 讀取 raw.txt
with open(RAW_FILE, "r", encoding="utf-8") as file:
    lines = []

    for line in file:
        line = line.strip()

        # 忽略空白、註解與來源文字
        if not line:
            continue

        if line.startswith("#"):
            continue

        if line.startswith("Source:"):
            continue

        lines.append(line)


# 將文字轉成資料
reader = csv.DictReader(lines)

records = []

for row in reader:
    records.append({
        "year": int(row["year"]),
        "population_millions": float(row["population_millions"])
    })


# 取得數字
populations = [
    item["population_millions"]
    for item in records
]


# 1. 平均人口
average_population = sum(populations) / len(populations)


# 2. 2024 到 2100 總成長率
start_population = records[0]["population_millions"]
end_population = records[-1]["population_millions"]

growth_rate = (
    (end_population / start_population) - 1
) * 100


# 3. CAGR
start_year = records[0]["year"]
end_year = records[-1]["year"]

years = end_year - start_year

cagr = (
    (end_population / start_population) ** (1 / years) - 1
) * 100


# 各階段成長率
interval_growth = []

for i in range(1, len(records)):
    previous = records[i - 1]
    current = records[i]

    rate = (
        current["population_millions"]
        / previous["population_millions"]
        - 1
    ) * 100

    interval_growth.append({
        "from": previous["year"],
        "to": current["year"],
        "growth_percent": round(rate, 2)
    })


# 整理輸出資料
result = {
    "source": "UN World Population Prospects 2024",
    "scenario": "Medium projection",
    "unit": "million people",
    "records": records,
    "summary": {
        "average_population_millions":
            round(average_population, 2),

        "growth_rate_2024_2100_percent":
            round(growth_rate, 2),

        "cagr_2024_2100_percent":
            round(cagr, 3)
    },
    "interval_growth": interval_growth
}


# 輸出 JSON
with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        result,
        file,
        ensure_ascii=False,
        indent=2
    )


print("資料處理完成！")
print(f"平均人口：{average_population:.2f} million")
print(f"總成長率：{growth_rate:.2f}%")
print(f"CAGR：{cagr:.3f}%")
print(f"JSON 已輸出到：{OUTPUT_FILE}")
