from termcolor import colored

# def show_highlight(text: str) -> None:
#     """
#     입력된 문자열을 termcolor 로 꾸며서 출력합니다.
#     매개변수: text (str)
#     반환: None — 출력만 수행
#     """
#     print(colored(text, "yellow", "on_red", ["bold"]))    # 화면에 보여주기만 함

# show_highlight("중요 공지!")           # 화면에 출력됨
# msg = show_highlight("중요 공지!")     # 출력은 되지만 msg 에는 아무것도 안 담김
# print(msg)                             # None

def make_highlight(text: str) -> str:
    """
    입력된 문자열을 termcolor 로 꾸며서 돌려줍니다.
    매개변수: text (str)
    반환: str — 꾸민 텍스트
    """
    return colored(text, "yellow", "on_red", ["bold"])    # 꾸민 텍스트를 돌려줌

msg = make_highlight("중요 공지!")     # 화면에 아무것도 안 나옴
print(msg)                             # 중요 공지!  — 돌려받은 값이 msg 에 담김
print(msg + " " + msg)                 # 담아뒀으니 이어 붙여 다시 쓸 수 있음