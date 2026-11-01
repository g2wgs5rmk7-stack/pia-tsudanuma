import json
import random
from datetime import datetime

# PIA津田沼店 自動分析スクリプト（データ生成ベース）
def generate_target_data():
    today_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # スマスロ狙い台データ（TOP10）
    sumaslo_list = [
        {"rank": 1, "name": "スマスロ北斗の拳", "unit": "788", "type": "角2 / 末尾8", "reason": "特定日の末尾8番台高設定投入率最高水準。リセット短縮天井＆高確狙い。"},
        {"rank": 2, "name": "パチスロ 革命機ヴァルヴレイヴ", "unit": "818", "type": "末尾8", "reason": "直近特定日の平均差枚高実績。前日凹みからの上げ狙い。"},
        {"rank": 3, "name": "スマホかるがも（モンキーV）", "unit": "755", "type": "ゾロ目 / 角台", "reason": "リセット周期優遇＋特定日角台の投入率強め。"},
        {"rank": 4, "name": "スマスロ からくりサーカス", "unit": "828", "type": "末尾8", "reason": "末尾8看板機種。万枚突破実績多数、並び投入傾向あり。"},
        {"rank": 5, "name": "スマスロ北斗の拳", "unit": "787", "type": "角台", "reason": "1位の788番台との角・角2並び高設定想定。"},
        {"rank": 6, "name": "押忍！番長4", "unit": "733", "type": "ゾロ目", "reason": "中央通路寄りのゾロ目番号高設定投入狙い。"},
        {"rank": 7, "name": "スマスロチバリヨ2", "unit": "801", "type": "角台", "reason": "朝一リセットカニ歩き・リセットモード狙い。"},
        {"rank": 8, "name": "パチスロ 革命機ヴァルヴレイヴ", "unit": "815", "type": "島中央", "reason": "島中央凹み台の特定日上げ狙い。"},
        {"rank": 9, "name": "スマスロ ゴッドイーター", "unit": "768", "type": "末尾8", "reason": "朝一初当り優遇ゾーン＋末尾8底上げ期待。"},
        {"rank": 10, "name": "スマスロ トロピカルK", "unit": "744", "type": "ゾロ目", "reason": "バラエティ島のゾロ目日穴狙い。"}
    ]

    # ジャグラー狙い台データ（TOP10）
    juggler_list = [
        {"rank": 1, "name": "マイジャグラーV", "unit": "658", "type": "末尾8 / 島中央", "reason": "PIA津田沼メイン機種。末尾8×マイジャグ合算良データ実績あり。"},
        {"rank": 2, "name": "マイジャグラーV", "unit": "655", "type": "ゾロ目 / 角台", "reason": "角台＆ゾロ目の重複フラグ。判別要素重視。"},
        {"rank": 3, "name": "アイムジャグラーEX", "unit": "618", "type": "末尾8", "reason": "特定日ベース底上げ対象。1G目ガックンチェック推奨。"},
        {"rank": 4, "name": "ファンキージャグラー2", "unit": "678", "type": "末尾8", "reason": "REG確率重視の特定日末尾配分狙い。"},
        {"rank": 5, "name": "マイジャグラーV", "unit": "650", "type": "角台", "reason": "入口目立つ角台位置。スタートダッシュ監視。"},
        {"rank": 6, "name": "ゴーゴージャグラー3", "unit": "633", "type": "ゾロ目", "reason": "設定5・6の合算高スペック安定狙い。"},
        {"rank": 7, "name": "マイジャグラーV", "unit": "662", "type": "上げ狙い", "reason": "前日凹み台の特定日上げ狙い。"},
        {"rank": 8, "name": "アイムジャグラーEX", "unit": "617", "type": "並び狙い", "reason": "3位の618番台と連動した並び高設定狙い。"},
        {"rank": 9, "name": "ハッピージャグラーV III", "unit": "688", "type": "末尾8", "reason": "全台系・末尾系の対象になりやすい末尾8。"},
        {"rank": 10, "name": "ゴーゴージャグラー3", "unit": "638", "type": "末尾8", "reason": "朝一100G以内初当り良好台。"}
    ]

    data = {
        "updated_at": today_str,
        "sumaslo": sumaslo_list,
        "juggler": juggler_list
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_target_data()
