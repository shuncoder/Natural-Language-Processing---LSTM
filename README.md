# Vietnamese News Classification with LSTM

Dự án phân loại chủ đề bài báo tiếng Việt dựa trên nội dung tóm tắt, sử dụng mô hình LSTM (Long Short-Term Memory).

## Tổng quan

- **Input**: Tóm tắt (summary) bài báo tiếng Việt
- **Output**: Chủ đề bài báo (Thời sự, Thể thao, Kinh tế, Công nghệ, Y tế, Giáo dục, v.v.)
- **Phương pháp**: LSTM với embedding tiếng Việt
- **Dataset**: Crawl từ các trang tin tức lớn (VnExpress, ZingNews, VietnamNet, DanTri, LaoDong, CafeF)

## Cấu trúc dự án

```
Natural-Language-Processing---LSTM/
├── data/                    # Thư mục chứa dữ liệu
│   └── dataset.csv         # Dataset đã crawl
├── models/                  # Thư mục lưu model
│   └── lstm_classifier.pt  # Model đã train
├── results/                 # Thư mục lưu kết quả đánh giá
│   ├── metrics_*.txt       # Báo cáo metrics
│   └── confusion_matrix_*.png  # Ma trận nhầm lẫn
├── src/                    # Source code
│   ├── __init__.py
│   ├── crawlers.py         # Module crawl dữ liệu
│   ├── preprocess.py       # Module xử lý text tiếng Việt
│   ├── evaluate.py         # Module đánh giá model
│   └── utils.py            # Tiện ích phụ trợ
├── train.ipynb             # Notebook huấn luyện model
├── requirements.txt        # Dependencies
└── .gitignore             # Cấu hình Git
```

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/shuncoder/Natural-Language-Processing---LSTM.git
cd Natural-Language-Processing---LSTM
```

2. Tạo và kích hoạt môi trường ảo (tùy chọn):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

## Thu thập dữ liệu

1. Chạy file `BTL_NLP_dataset.ipynb` để crawl dữ liệu từ các trang tin tức
2. Dữ liệu sẽ được lưu vào `data/dataset.csv`
3. Định dạng dữ liệu:
   - `title`: Tiêu đề bài báo
   - `summary`: Tóm tắt nội dung
   - `label`: Chủ đề bài báo

## Huấn luyện model

1. Chạy notebook `train.ipynb`:
   - Tiền xử lý dữ liệu tiếng Việt
   - Xây dựng vocabulary
   - Train model LSTM
   - Đánh giá và lưu model

2. Kết quả:
   - Model được lưu tại `models/lstm_classifier.pt`
   - Metrics và confusion matrix trong thư mục `results/`

## Đặc điểm kỹ thuật

1. Xử lý text tiếng Việt:
   - Chuẩn hóa Unicode
   - Tokenize từ tiếng Việt
   - Loại bỏ stopwords
   - Tùy chọn: gỡ dấu tiếng Việt

2. Kiến trúc model:
   - Embedding layer
   - Bidirectional LSTM
   - Dropout để tránh overfitting
   - Cross-entropy loss

## Đánh giá

- Accuracy, Precision, Recall, F1-score cho từng chủ đề
- Confusion matrix để phân tích lỗi
- Thử nghiệm với văn bản mới

## Môi trường phát triển

- Python 3.8+
- PyTorch 1.9+
- CUDA (tùy chọn, cho GPU training)

## Tác giả

- shuncoder

## License

MIT License

## Ghi chú

- Dữ liệu lớn (data, models) không được commit lên Git
- Sử dụng Git LFS nếu cần theo dõi file lớn
- Có thể tự động hóa pipeline bằng Makefile hoặc shell script
