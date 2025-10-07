# Lab 04 – Coding giao diện đăng nhập (Form Login)

> Dự án này đáp ứng yêu cầu Lab 04: HTML + CSS + JavaScript, có **Username/Password**, nút **Login**, **Cancel**, **Remember me**, và **kiểm tra dữ liệu** cơ bản.

## Cấu trúc
```
Lab04-Login-Form/
├─ index.html
├─ styles.css
├─ app.js
└─ README.md
```

## Chạy demo trên máy
1. Mở thư mục này bằng **Visual Studio Code**.
2. (Khuyến nghị) Cài extension **Live Server** → click _Go Live_ để chạy `index.html`.
   - Hoặc mở file `index.html` trực tiếp bằng trình duyệt.

## Kiểm tra dữ liệu (validation) gồm:
- Bắt buộc nhập **Username** và **Password**.
- **Username**: chấp nhận dạng email hoặc ký tự thường; yêu cầu độ dài ≥ 3.
- **Password**: độ dài ≥ 6, có kiểm tra độ mạnh cơ bản.
- Hiển thị lỗi dưới mỗi input; disable nút Login trong lúc xử lý.

## Remember me
- Nếu tick **Remember me**, username sẽ được lưu vào `localStorage` và tự điền ở lần sau.

## Nút Cancel
- Xoá dữ liệu đã nhập và bỏ chọn Remember me (không điều hướng ra ngoài).

## Gợi ý nộp GitHub
1. Tạo repo mới trên GitHub.
2. Upload toàn bộ thư mục này.
3. Bật **GitHub Pages** (branch `main`, folder `/root`).
4. Link demo sẽ có dạng: `https://<username>.github.io/<repo-name>/`.

> Lưu ý: Đây chỉ là **demo front-end**, không gọi API thật. Chức năng “đăng nhập thành công” chỉ minh hoạ khi đầu vào hợp lệ.
