import re


def format_saa_dump(input_file, output_file):
    """
    AWS SAA dump 파일을 문제/답/해설 구조로 정리
    """

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 문제 단위로 split
    # 패턴: 숫자] ~ (다음 숫자] 혹은 EOF)
    pattern = re.compile(r"(\d+\].*?)(?=\n\d+\]|$)", re.DOTALL)
    matches = pattern.findall(content)

    formatted_blocks = []

    for block in matches:
        block = block.strip()
        if not block:
            continue

        # 문제 번호
        number_match = re.match(r"(\d+)\]", block)
        if number_match:
            q_number = number_match.group(1)
        else:
            q_number = "N/A"

        # 문제 본문
        # (문제 번호 다음부터 보기를 찾기 전까지)
        # e.g. A. 혹은 B. 로 시작하는 줄 이전까지가 문제
        choices_match = re.search(r"\n[A-Z]\.", block)
        if choices_match:
            q_text = block[:choices_match.start()].strip()
            rest = block[choices_match.start():]
        else:
            # 보기가 없는 경우
            q_text = block
            rest = ""

        # 보기들
        choices = []
        if rest:
            # 보기 패턴 추출
            choice_pattern = re.compile(r"\n([A-Z]\..*?)(?=\n[A-Z]\.|$)", re.DOTALL)
            choices = choice_pattern.findall(rest)

        # 정답
        ans_match = re.search(r"(?<=\n)ans[^\n]*", block, re.IGNORECASE)
        answer_text = ans_match.group(0).strip() if ans_match else ""

        # 해설
        # ans 이후 텍스트 ~ 끝
        explanation = ""
        if ans_match:
            explanation_start = ans_match.end()
            explanation = block[explanation_start:].strip()

        # 보기들도 하나의 문자열로 합침
        choices_str = "\n".join(c.strip() for c in choices) if choices else ""

        # 블록 재구성
        formatted_block = f"### ✅ [{q_number}] 문제\n\n> {q_text}\n\n"
        if choices_str:
            formatted_block += f"**보기:**\n{choices_str}\n\n"
        if answer_text:
            formatted_block += f"**정답:** {answer_text}\n\n"
        if explanation:
            formatted_block += f"**해설:** {explanation}\n"

        formatted_blocks.append(formatted_block)

    # 파일로 저장
    with open(output_file, "w", encoding="utf-8") as f:
        for block in formatted_blocks:
            f.write(block + "\n\n")

    print(f"총 {len(formatted_blocks)}개의 문제가 정리되어 {output_file} 에 저장되었습니다.")

format_saa_dump(
    input_file="Certificates\SAA\DUMP\Filtered\Keyword_IAM.txt",
    output_file="Certificates\SAA\DUMP\Filtered\Formatted_IAM.md"
)