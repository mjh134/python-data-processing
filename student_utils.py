"""student_utils: 提供成绩行解析函数 parse_student."""


def parse_student(line):
    """解析一行 '姓名,成绩' 文本; 校验失败抛出 ValueError."""
    fields = line.split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误: 期望 2 个, 实际 {len(fields)} 个")
    name, score_str = fields[0].strip(), fields[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_str!r}") from None
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
