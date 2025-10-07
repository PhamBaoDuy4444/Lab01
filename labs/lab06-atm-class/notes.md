# Lab 06 – Thiết kế chi tiết lớp & kiến trúc (Book Management)

**Mục tiêu:** Từ Use Case (UC-001 Đăng nhập/Đăng ký, UC-002 CRUD Sách, UC-003 Tìm kiếm/Xem chi tiết), thiết kế **Class Diagram** và **Package Diagram** cho hệ thống quản lý sách.

## Cấu trúc thư mục
```
/labs/lab06-book-class/
├── class-book.puml
├── package-diagram.puml
└── notes.md   (tệp này)
```

## Công cụ
- VS Code + PlantUML extension (hoặc draw.io nếu muốn vẽ lại theo style riêng).
- (Tuỳ chọn) Graphviz để export ảnh nhanh trong VS Code.

## Hướng dẫn export PNG
1. Mở thư mục này bằng VS Code.
2. Cài **PlantUML** extension.
3. Mở `class-book.puml` → **PlantUML: Export Current Diagram** → chọn **PNG**.
4. Lặp lại với `package-diagram.puml`.
5. Commit cả `.puml` và `.png` lên repo.

## Ghi chú thiết kế

### Class Diagram
- **User**: quản lý tài khoản, gồm `email`, `passwordHash`, `role`. Hai thao tác chính: `register`, `login` (UC-001).
- **Session**: lưu `token` (JWT), phục vụ xác thực & duy trì phiên (UC-001 – postconditions).
- **Book**: thực thể sách, thuộc tính theo UC-002/003; có `validateIsbn(...)` cho special requirements.
- **SearchService**: tìm kiếm & lọc (UC-003). Có thể đưa logic phân trang/sắp xếp vào đây.
- **UserDAO / BookDAO**: mô tả tương tác DB (tuỳ chọn, để rõ phân tầng).

Quan hệ chính:
- `User --> Session`: tạo & dùng phiên sau khi đăng nhập.
- `User --> Book`: Admin thao tác CRUD (UC-002).
- `SearchService --> Book`: trả về danh sách/chi tiết (UC-003).
- `UserDAO --> User`, `BookDAO --> Book`: tầng truy cập dữ liệu.

> Có thể mở rộng thêm `PasswordResetToken` cho flow “Quên mật khẩu (A3 UC-001)”, hoặc thêm `AuditLog` để ghi nhật ký CRUD.

### Package Diagram
- **UI**: trang Login, CRUD Sách, Search, Book Detail.
- **Controller**: `AuthController`, `BookController`, `SearchController` – nhận request từ UI.
- **Service**: `UserService`, `BookService`, `SearchService` – xử lý nghiệp vụ (hash mật khẩu, validate ISBN, tìm kiếm, phân trang).
- **Persistence**: `UserDAO`, `BookDAO` – làm việc với DB.

Luồng phụ thuộc:
- `UI → Controller → Service → Persistence`.

## Mapping Use Case → Thiết kế
- **UC-001 (Login/Register)**: `UserService` (băm mật khẩu), `UserDAO` (tạo/tìm user), `Session` (JWT).
- **UC-002 (CRUD Sách)**: `BookService` (validate dữ liệu/ISBN), `BookDAO` (create/update/delete/find).
- **UC-003 (Tìm kiếm/Xem chi tiết)**: `SearchService` (search/filter, phân trang), `BookDAO` (query).

## Rubric (10 điểm)
- **Đủ lớp & quan hệ (5đ)**: các lớp & associations như trên.
- **Thuộc tính/phương thức đúng (3đ)**: đúng tên/kiểu cơ bản (email, passwordHash, isbn, v.v.) và phương thức chính (login/register, validateIsbn, search/filter).
- **Tài liệu & repo (2đ)**: `notes.md` mô tả; commit `.puml` & `.png` đúng cấu trúc.

---

> Mẹo: Khi export ảnh, nên đặt tên `class-book.png` và `package-diagram.png` để nộp theo chuẩn giống Lab 06.