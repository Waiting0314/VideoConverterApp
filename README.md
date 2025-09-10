# 🎬 影片轉檔工具 (Video Converter GUI)

一個使用 **Python + Tkinter** 製作的簡易圖形化介面 (GUI) 工具，透過 **FFmpeg** 進行影片批次轉檔。  
支援多種常見格式 (TS / MP4 / MKV / AVI / MOV)，並提供保留或刪除原始檔案的選項。

---

## ✨ 功能特色
- 📂 批次轉檔：選擇資料夾後，自動轉換所有指定格式的影片。  
- 🔄 多格式支援：輸入與輸出格式可選擇 (ts, mp4, mkv, avi, mov)。  
- ⚠️ 防呆檢查：禁止輸入與輸出格式相同，避免重複轉檔。  
- ✅ 可選擇是否保留原始檔案。  
- 📊 內建進度條與狀態顯示。  
- 🖥️ 簡單易用，不需要手動輸入命令列。  

---

## 📦 安裝需求
1. **Python 3.8+**  
2. 安裝必要套件：
   ```bash
   pip install tk
   ```
3. 安裝 **FFmpeg**  
   - Windows 使用者請至 [FFmpeg 官網](https://ffmpeg.org/download.html) 下載並安裝。  
   - 並將 `ffmpeg.exe` 所在路徑加入系統環境變數 `PATH`。  
   - 測試是否安裝成功：
     ```bash
     ffmpeg -version
     ```

---

## 🚀 使用方式
1. 下載專案程式碼：
   ```bash
   git clone https://github.com/Waiting0314/VideoConverterApp.git
   cd <你的專案>
   ```
2. 執行程式：
   ```bash
   python VideoConverterApp.py
   ```
3. 介面操作：
   - 點擊 **選擇資料夾** → 選擇包含影片的資料夾  
   - 選擇 **輸入格式**（例如 ts）  
   - 選擇 **輸出格式**（例如 mp4）  
   - 勾選或取消「保留原始檔案」  
   - 程式會自動批次轉換所有符合條件的影片  

---

## ⚠️ 注意事項
- 本工具僅為 **FFmpeg** 的圖形化封裝，轉檔速度與品質取決於 FFmpeg 的設定。  
- 預設使用：
  ```bash
  ffmpeg -i input -c:v copy -c:a aac output
  ```
  若需要自訂編碼參數，請自行修改程式碼中的 `command` 區塊。  
- 不支援加密或 DRM 保護的影片檔案。  

---

## 📄 授權
本專案使用 MIT License，歡迎自由使用與修改。  
