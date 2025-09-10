# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 20:23:39 2025

@author: WEI TING LIN
"""

import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class VideoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("影片轉檔工具")
        self.root.geometry("420x360")
        self.root.resizable(False, False)

        # 標題
        self.label = tk.Label(root, text="請選擇資料夾進行轉檔", font=("Arial", 12))
        self.label.pack(pady=10)

        # 選擇資料夾按鈕
        self.select_button = tk.Button(root, text="選擇資料夾", command=self.select_folder, font=("Arial", 10), width=20)
        self.select_button.pack(pady=5)

        # 輸入格式選擇
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)
        tk.Label(input_frame, text="輸入格式: ", font=("Arial", 10)).pack(side=tk.LEFT)
        self.input_var = tk.StringVar(value="ts")
        formats = ["ts", "mp4", "mkv", "avi", "mov"]
        self.input_menu = ttk.Combobox(input_frame, textvariable=self.input_var, values=formats, state="readonly", width=8)
        self.input_menu.pack(side=tk.LEFT)

        # 輸出格式選擇
        output_frame = tk.Frame(root)
        output_frame.pack(pady=5)
        tk.Label(output_frame, text="輸出格式: ", font=("Arial", 10)).pack(side=tk.LEFT)
        self.output_var = tk.StringVar(value="mp4")
        self.output_menu = ttk.Combobox(output_frame, textvariable=self.output_var, values=formats, state="readonly", width=8)
        self.output_menu.pack(side=tk.LEFT)

        # 是否保留原始檔案
        self.keep_original = tk.BooleanVar(value=True)
        self.keep_checkbox = tk.Checkbutton(root, text="保留原始檔案", variable=self.keep_original, font=("Arial", 10))
        self.keep_checkbox.pack(pady=5)

        # 進度顯示
        self.progress_label = tk.Label(root, text="", font=("Arial", 10))
        self.progress_label.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            threading.Thread(target=self.convert_files, args=(folder_path,), daemon=True).start()

    def convert_files(self, input_folder):
        if not os.path.exists(input_folder):
            self.show_error("錯誤", f"資料夾不存在:\n{input_folder}")
            return

        input_format = self.input_var.get().lower()
        output_format = self.output_var.get().lower()

        # 防呆：輸入與輸出格式不可相同
        if input_format == output_format:
            self.show_error("格式錯誤", "輸入與輸出格式不可相同！")
            return

        files = os.listdir(input_folder)
        target_files = [f for f in files if f.lower().endswith(f".{input_format}")]

        if not target_files:
            self.show_info("提示", f"資料夾內無 {input_format.upper()} 檔案。")
            return

        total = len(target_files)
        self.progress["value"] = 0
        self.progress["maximum"] = total

        keep_original = self.keep_original.get()

        for idx, in_file in enumerate(target_files, start=1):
            input_path = os.path.join(input_folder, in_file)
            output_file = os.path.splitext(in_file)[0] + f".{output_format}"
            output_path = os.path.join(input_folder, output_file)

            command = [
                "ffmpeg", "-i", input_path,
                "-c:v", "copy",
                "-c:a", "aac",
                output_path
            ]

            self.update_status(f"轉換中: {in_file} ({idx}/{total})")
            try:
                subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            except subprocess.CalledProcessError as e:
                self.show_error("轉檔失敗", f"{in_file} 轉檔失敗。\n錯誤訊息: {e}")
                continue

            # 刪除原檔案（如果使用者不想保留）
            if not keep_original and os.path.exists(input_path):
                try:
                    os.remove(input_path)
                except Exception as e:
                    self.show_error("刪除失敗", f"無法刪除 {in_file}\n錯誤訊息: {e}")

            self.update_progress(idx)

        self.update_status("轉換完成！")
        self.show_info("完成", f"所有 {input_format.upper()} 檔案已轉換成 {output_format.upper()}！")

    def update_status(self, text):
        self.progress_label.config(text=text)
        self.root.update_idletasks()

    def update_progress(self, value):
        self.progress["value"] = value
        self.root.update_idletasks()

    def show_info(self, title, message):
        self.root.after(0, lambda: messagebox.showinfo(title, message))

    def show_error(self, title, message):
        self.root.after(0, lambda: messagebox.showerror(title, message))

def main():
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
