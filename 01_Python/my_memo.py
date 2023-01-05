# 주피터 노트북 명령어 (매직 커맨드)
# %%(셀 전체 명령어)
# %%writefile 파일명 -> 실행하면 cell의 내용을 파일에 출력
def memo():
    print("저장할 파일명을 입력하세요.")
    file_name = input("파일명: ")
    print(f"{file_name}에 저장합니다.")
    print("====================================")
    with open(file_name, 'wt', encoding='utf-8') as fw:
        print("저장할 내용을 입력하세요.")
        print('='*30)
        while True:
            line_text = input('>')
            if line_text == "!q":
                break
            fw.write(line_text+'\n')
    print("종료")
