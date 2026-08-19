import sys
sys.path.append("src")
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from core.processor import run_and_save

def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

class SalesCsvConsolidatorApp:
    def __init__(self, root):
        root.title("売上CSV統合ツール")
        root.geometry("400x200")

        self.select_button = tk.Button(root, text="入力フォルダを選択", command=self.select_and_run)
        self.select_button.pack(pady=(20, 0), anchor="w", padx=20)

        self.result_label = tk.Label(root, text="", justify="left", wraplength=360)
        self.result_label.pack(pady=(20, 0), anchor="w", padx=20)
    
    def select_and_run(self):
        input_dir = select_folder()
        if not input_dir:
            self.result_label.config(text="フォルダ選択がキャンセルされました")
            return

        print("入力フォルダ:", input_dir)
        folder_name = Path(input_dir).name
        output_path = Path("samples/output/統合売上データ.csv")
        try:
            merged, success, error, total = run_and_save(input_dir, output_path)
            print(merged)
            print(f"成功:{success}/{total}")
            print(f"失敗:{error}/{total}")

            lines = [
                f"入力フォルダ: {folder_name}",
                "",
                f"成功:{success}/{total} 失敗:{error}/{total}",
                f"出力先: {output_path}",
            ]
            self.result_label.config(text="\n".join(lines))
        except ValueError as e:
            print(f"エラー: {e}")
            self.result_label.config(text=f"エラー: {e}")

def main():
    root = tk.Tk()
    SalesCsvConsolidatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
