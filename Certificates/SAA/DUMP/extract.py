import re


def extract_questions_by_keyword(input_file, output_file, keywords):
    """
    특정 키워드가 포함된 문제 덩어리만 새 파일로 저장
    
    :param input_file: str, 원본 문제 파일 경로
    :param output_file: str, 추출한 문제 저장할 파일 경로
    :param keywords: list[str], 찾고 싶은 키워드들 (대소문자 무시)
    """

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 문제 단위로 쪼개기
    # 패턴: 숫자] 로 시작 → ----로 끝
    # re.DOTALL → 개행 포함하여 . 매치
    pattern = re.compile(r'(\d+\].*?)(-+\n)', re.DOTALL)
    matches = pattern.findall(content)

    blocks = []
    for match in matches:
        block_text = match[0]
        blocks.append(block_text.strip())

    # 키워드 포함된 블록만 추출
    matched_blocks = []
    for block in blocks:
        block_lower = block.lower()
        if any(keyword.lower() in block_lower for keyword in keywords):
            matched_blocks.append(block)

    if matched_blocks:
        with open(output_file, 'w', encoding='utf-8') as f:
            for block in matched_blocks:
                f.write(block + '\n\n')
        print(f"총 {len(matched_blocks)}개의 블록이 {output_file} 에 저장되었습니다.")
    else:
        print("키워드가 포함된 블록이 없습니다.")


extract_questions_by_keyword(
    input_file='Certificates\SAA\DUMP\AWS SAA-03 Solution.txt',
    output_file='Certificates\SAA\DUMP\Filtered\Keyword_IAM.txt',
    keywords=['IAM']
)

