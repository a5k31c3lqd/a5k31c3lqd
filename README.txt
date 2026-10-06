A5-K31 — CHỈ XEM ẢNH NHẸ TRÊN WEBSITE

1. Mở admin.html, mục Thêm ảnh vào thư viện, chọn ảnh từ máy.
2. Website tự tạo bản xem tối đa 1800px, mục tiêu khoảng 240 KiB và thumbnail 480px, khoảng 28 KiB. Ảnh giữ tỷ lệ, không crop; ảnh gốc trên máy không bị thay đổi. WebP được dùng khi trình duyệt hỗ trợ, nếu không dùng JPEG.
3. Sửa album/chú thích, xem trước thư viện, rồi Xuất website để đăng GitHub. Giải nén và cập nhật repo như trước.
4. Khách xem ảnh ngay trên website, mở riêng và zoom. Không còn nút tải riêng hoặc tải tất cả ảnh.

Ảnh được nén mất dữ liệu; gần giống ảnh gốc khi xem bình thường nhưng zoom sâu không giữ mọi chi tiết. GIF động thành ảnh tĩnh, ảnh có nền trong suốt có thể chuyển nền trắng.

Các ảnh nhẹ được lưu trên GitHub; không cần Drive/R2 nếu tổng website nằm trong giới hạn Pages. 2.000 ảnh ở kích thước mục tiêu có thể chiếm khoảng 700 MiB sau đóng gói Base64, nhưng dung lượng thực tế phụ thuộc ảnh. Kiểm tra ZIP xuất và nội dung giải nén trước khi đăng. ZIP có nén nên kích thước ZIP không bằng kích thước website giải nén. Không đảm bảo mọi bộ 2.000 ảnh đều dưới giới hạn hosting.

Không chọn toàn bộ 24 GB một lần: nên thêm từng album hoặc đợt 50–100 ảnh để giảm rủi ro đầy bộ nhớ trình duyệt. Bộ nhớ bản chỉnh sửa vẫn phụ thuộc thiết bị và IndexedDB. Ảnh được đọc tuần tự và chỉ bản nhẹ được lưu. Bản đã đăng chỉ tải ảnh trên trang đang xem; phân trang 48 ảnh.

Ảnh cũ đã thêm trước nâng cấp không tự nén lại. Muốn giảm dung lượng, xóa bản ảnh cũ và thêm lại từ máy. Không xóa ảnh gốc.

Slideshow tải ảnh riêng và cũng được tạo bản nhẹ. Album Drive cũ vẫn trong mục gấp riêng; nó chỉ mở Drive, không tự nhập ảnh vào website.

Bỏ nút tải không ngăn người xem lưu ảnh bằng trình duyệt/chụp màn hình.

THÊM NHIỀU ẢNH NHANH
Nút chọn ảnh hỗ trợ nhiều file cho cả thư viện và slideshow. Giữ Ctrl/Command để chọn rời rạc, Shift để chọn dãy, Ctrl/Command+A để chọn tất cả trong cửa sổ chọn file. Trên điện thoại dùng trình chọn ảnh hỗ trợ chọn nhiều.
Xử lý 2 ảnh đồng thời, giữ thứ tự đã chọn, lưu một nhóm tối đa 20 ảnh thay vì ghi lại toàn bộ bản chỉnh sửa sau mỗi ảnh. Có thanh tiến độ và số ảnh đã xử lý/đã lưu. Ảnh lỗi được bỏ qua; nếu bộ nhớ đầy thì dừng và giữ các nhóm đã lưu. Tốc độ thực tế phụ thuộc CPU, dung lượng và định dạng ảnh. Không đóng trang khi đang xử lý. Không cần chọn lại các ảnh đã được báo lưu thành công.

CHIA 4 THƯ MỤC ẢNH
Mỗi lần Xuất website, ảnh nhúng được chia đều vào photos/part-1, photos/part-2, photos/part-3, photos/part-4. Ví dụ 2.000 ảnh tương ứng 500 file mỗi thư mục. Slideshow cũng được chia cùng các ảnh; manifest gallery-data.js lưu đường dẫn đúng cho từng ảnh. Website vẫn đọc được bản cũ photos/<id>.js khi manifest chưa có trường file.

Để chuyển ảnh đã đăng: dùng admin mới với bản chỉnh sửa đã lưu, hoặc giữ gallery-data.js/thư mục photos hiện tại rồi mở admin mới và Khôi phục bản đã đăng nếu cần. Xuất lại bộ đầy đủ, rồi thay toàn bộ thư mục photos trong repo bằng photos mới cùng gallery-data.js mới. Giữ bản sao repo trước khi thay. Chỉ di chuyển ảnh bằng tay sẽ không cập nhật đường dẫn manifest. Các file ảnh cũ còn trên repo không tự xóa khi chép đè.
