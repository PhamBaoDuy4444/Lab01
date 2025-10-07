#Use Case 1: Đăng nhập/Đăng ký

Use Case ID: UC-001
Primary Actor: Người dùng
Secondary Actor: Hệ thống
Brief Description: Người dùng tạo tài khoản và đăng nhập để truy cập hệ thống.

Preconditions:

    Website chạy ổn định, DB sẵn sàng.

Postconditions:

    Người dùng đăng nhập thành công, hệ thống lưu session/JWT.

Main Success Scenario:

    Người dùng mở form đăng nhập/đăng ký.

    Nhập email, mật khẩu (và tên nếu đăng ký).

    Hệ thống xác thực/khởi tạo tài khoản.

    Tạo phiên → chuyển đến trang chính.

Alternative Flows:

    A1: Sai mật khẩu → báo lỗi.

    A2: Tài khoản tồn tại → gợi ý đăng nhập.

    A3: Quên mật khẩu → gửi email reset.

    Special Requirements:

    Băm mật khẩu (hash).

    Phản hồi < 2 giây.

#Use Case 2: Quản lý Sách (CRUD)

Use Case ID: UC-002
Primary Actor: Admin
Secondary Actor: Hệ thống
Brief Description: Admin thêm, sửa, xóa sách trong thư viện.

Preconditions:

    Admin đăng nhập.

Postconditions:

    Thông tin sách được lưu hoặc cập nhật trong DB.

Main Success Scenario:

    Admin chọn “Quản lý Sách”.

    Nhập thông tin sách (tiêu đề, tác giả, thể loại, ISBN, mô tả).

    Nhấn “Lưu”.

    Hệ thống validate, ghi DB.

    Hiển thị thông báo thành công.

Alternative Flows:

    A1: Thiếu trường → highlight lỗi.

    A2: ISBN trùng → báo lỗi.

Special Requirements:

    Validate ISBN, giới hạn độ dài text.

#Use Case 3: Tìm kiếm & Xem chi tiết Sách

Use Case ID: UC-003
Primary Actor: Người dùng
Secondary Actor: Hệ thống
Brief Description: Người dùng tìm kiếm sách và xem chi tiết nội dung.

Preconditions:

    DB có dữ liệu sách.

Postconditions:

    Kết quả tìm kiếm hiển thị, người dùng xem chi tiết sách.

Main Success Scenario:

    Người dùng nhập từ khóa hoặc chọn bộ lọc (thể loại, tác giả).

    Hệ thống tìm trong DB.

    Hiển thị danh sách kết quả.

    Người dùng chọn 1 sách → xem chi tiết (tên, tác giả, mô tả, ảnh bìa).

Alternative Flows:

    A1: Không có kết quả → gợi ý lại.

    A2: Quá nhiều kết quả → phân trang/sắp xếp.

Special Requirements:

    Tối ưu truy vấn tìm kiếm.

    Thời gian phản hồi < 1 giây.