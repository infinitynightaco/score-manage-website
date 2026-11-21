# 八科加權成績管理系統

**Eight Subject Weighted Grade Manager**

## 專案介紹

這是一個使用 Python Flask 開發的網頁成績管理系統。

使用者可以輸入八個科目的成績，系統會自動計算加權總點數與加權平均，並透過圖表呈現各科成績分布。

## 使用技術

- Python
- Flask
- HTML
- CSS
- JavaScript
- Chart.js

## 目前功能（Version 1.0）

- 八科成績輸入
- 自動計算加權總點數
- 自動計算加權平均
- 顯示最高分與最低分
- 四張成績統計卡片
- 八科成績長條圖
- 手機版響應式排版
- 成績輸入範圍驗證

## 科目與權重

| 科目 | 權重 |
|---|---:|
| 國文 | 4 |
| 英文 | 4 |
| 數學A | 4 |
| 物理 | 2 |
| 化學 | 2 |
| 歷史 | 2 |
| 地理 | 2 |
| 公民 | 3 |

## 安裝與執行

### 1. 複製專案

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. 建立虛擬環境

```bash
python -m venv .venv
```

### 3. 啟動虛擬環境（Windows PowerShell）

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. 安裝套件

```bash
pip install -r requirements.txt
```

### 5. 啟動網站

```bash
python app.py
```

### 6. 開啟瀏覽器

```text
http://127.0.0.1:5000
```

## 開發紀錄

- Version 1.0：完成八科加權計算、統計卡片、成績分布圖及響應式版面。

## 未來規劃

- 成績等級分析
- 弱科分析
- 個人化學習建議
- 歷次成績紀錄

---

本專案為個人 Python 學習與作品集練習。