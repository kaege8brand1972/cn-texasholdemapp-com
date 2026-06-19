import json
import sys

SITE_DATA = [
    {
        "title": "Texas Holdem App - 德州扑克教程与策略",
        "url": "https://cn-texasholdemapp.com",
        "tags": ["德州扑克app", "扑克策略", "教程", "在线学习"],
        "description": "提供全面的德州扑克规则、技巧、策略分析，适用于新手和进阶玩家。"
    },
    {
        "title": "德州扑克工具集",
        "url": "https://cn-texasholdemapp.com/tools",
        "tags": ["德州扑克app", "概率计算", "手牌评估", "工具"],
        "description": "集成手牌胜率计算、翻牌前范围分析、位置策略等实用工具。"
    },
    {
        "title": "德州扑克社区",
        "url": "https://cn-texasholdemapp.com/community",
        "tags": ["德州扑克app", "论坛", "交流", "牌局分析"],
        "description": "玩家交流社区，可分享牌局、讨论战术、获取专家点评。"
    }
]


def format_summary(entry: dict, index: int) -> str:
    """将单条站点数据格式化为摘要字符串"""
    title = entry.get("title", "无标题")
    url = entry.get("url", "#")
    tags = entry.get("tags", [])
    description = entry.get("description", "")
    tag_str = ", ".join(tags) if tags else "无标签"
    lines = [
        f"【站点 {index + 1}】",
        f"  标题      : {title}",
        f"  链接      : {url}",
        f"  标签      : {tag_str}",
        f"  简介      : {description}",
        ""
    ]
    return "\n".join(lines)


def generate_summary(data: list) -> str:
    """根据站点列表生成结构化摘要"""
    header = "====== 站点摘要 ======\n"
    footer = f"共 {len(data)} 个站点，生成时间: 内部数据\n"
    body_parts = [header]
    for idx, item in enumerate(data):
        body_parts.append(format_summary(item, idx))
    body_parts.append(footer)
    return "\n".join(body_parts)


def search_by_tag(data: list, tag: str) -> list:
    """根据标签筛选站点"""
    tag_lower = tag.lower()
    results = []
    for item in data:
        tags_lower = [t.lower() for t in item.get("tags", [])]
        if tag_lower in tags_lower:
            results.append(item)
    return results


def main():
    print("读取内置站点资料并生成结构化摘要...\n")

    # 输出完整摘要
    full_summary = generate_summary(SITE_DATA)
    print(full_summary)

    # 示例：按标签搜索
    search_tag = "德州扑克app"
    matched = search_by_tag(SITE_DATA, search_tag)
    if matched:
        print(f"\n包含标签「{search_tag}」的站点:")
        for m in matched:
            print(f"  - {m.get('title')} ({m.get('url')})")
    else:
        print(f"\n未找到包含标签「{search_tag}」的站点。")

    # 输出JSON格式以便进一步处理
    print("\n--- JSON 格式输出 ---")
    json_output = json.dumps(SITE_DATA, ensure_ascii=False, indent=2)
    print(json_output)


if __name__ == "__main__":
    main()