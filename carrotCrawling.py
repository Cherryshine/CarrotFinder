import tkinter as tk
from tkinter import ttk

class CarrotCrawler:
    def __init__(self):
        # 메인 윈도우 생성
        self.root = tk.Tk()
        self.root.title("당근마켓 크롤러")
        self.root.geometry("800x600")

        # 메인 프레임 생성
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 기본 위젯 추가
        self.title_label = ttk.Label(self.main_frame, text="당근마켓 크롤러", font=('Helvetica', 16, 'bold'))
        self.title_label.grid(row=0, column=0, pady=10)

        # 검색 프레임
        self.search_frame = ttk.LabelFrame(self.main_frame, text="검색 설정", padding="5")
        self.search_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

        # 검색어 입력
        self.search_label = ttk.Label(self.search_frame, text="검색어:")
        self.search_label.grid(row=0, column=0, padx=5)
        self.search_entry = ttk.Entry(self.search_frame, width=40)
        self.search_entry.grid(row=0, column=1, padx=5)

        # 검색 버튼
        self.search_button = ttk.Button(self.search_frame, text="검색 시작")
        self.search_button.grid(row=0, column=2, padx=5)

    def run(self):
        # 메인 루프 실행
        self.root.mainloop()

if __name__ == "__main__":
    app = CarrotCrawler()
    app.run() 