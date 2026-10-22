A5-K31 — GITHUB PAGES, KHÔNG CẦN BACKEND

CÁCH DÙNG NHANH
1. Giải nén ZIP. Mở index.html để xem; mở admin.html để chọn ảnh.
2. Trình duyệt cần hỗ trợ IndexedDB, dialog và JavaScript. Nếu mở trực tiếp file gặp lỗi bộ nhớ, chạy máy chủ tĩnh bất kỳ (ví dụ VS Code Live Server); đây chỉ là cách phục vụ file, không có backend xử lý nội dung.
3. Trong Quản trị: chọn ảnh, sửa chú thích/album, sắp xếp. Có thể tạo bài đăng trên trang chủ, hoặc lưu bài nháp.
4. Nhấn Xuất website để đăng GitHub. Giải nén ZIP mới, lấy TOÀN BỘ file và thư mục bên trong, tải lên thư mục gốc repo GitHub bằng Add file > Upload files, rồi commit.
5. Settings > Pages > Build and deployment > Deploy from a branch > main > /(root) > Save. Nếu dùng nhánh khác, chọn nhánh đang chứa file.
6. Đợi GitHub triển khai rồi mở link Pages. Lần cập nhật sau lặp lại bước 4. Không tải nguyên ZIP lên repo để chạy website, cần giải nén.

ADMIN VÀ QUYỀN ĐĂNG
- Không có mật khẩu admin đặt trong JavaScript. Website tĩnh không xác thực quyền ghi máy chủ.
- Trang admin là công cụ soạn nội dung; ai mở cũng chỉ sửa bản trên trình duyệt của họ. Chỉ người có quyền ghi repo GitHub mới đăng được bản công khai. Tài khoản admin để xuất bản chính là tài khoản GitHub của bạn.
- Không cần nhập token hoặc mật khẩu GitHub vào website. Commit trên GitHub sau khi đăng nhập tài khoản của bạn.
- Bản chỉnh sửa lưu bằng IndexedDB theo trình duyệt và địa chỉ website. Không đồng bộ giữa máy/trình duyệt, có thể mất khi xóa dữ liệu duyệt web; xuất ZIP thường xuyên để sao lưu.
- Admin trên website được tải cùng bản đã xuất. Nếu đã có bản chỉnh sửa cũ trong trình duyệt, nút Khôi phục bản đã đăng sẽ thay nó bằng nội dung website hiện tại; thao tác này bỏ bản chỉnh sửa cũ.
- Bài nháp không được đưa vào ZIP website công khai. ZIP xuất chỉ chứa bài đã chọn xuất bản và tất cả ảnh trong bản chỉnh sửa. Bài nháp vẫn chỉ trên trình duyệt, không nằm trong bản sao ZIP.

THƯ VIỆN ẢNH
- Trang chủ thông báo chuyển sang Thư viện ảnh sau 10 giây, có nút chuyển ngay hoặc ở lại. Thư viện không tự chuyển trang.
- Bấm bất kỳ ảnh: xem riêng ảnh, zoom +/−, vừa khung, ảnh trước/sau, tải riêng, đóng bằng X hoặc Esc.
- Khi zoom lớn, cuộn/kéo bằng thao tác cuộn trên thiết bị để xem các phần ảnh. Ctrl + cuộn chuột để zoom; bàn phím +/- và trái/phải để điều khiển.
- Tải tất cả ảnh là 1 ZIP có toàn bộ ảnh thư viện, kể cả khi đang lọc. Tên file có số thứ tự tránh trùng tên. Ảnh giữ dữ liệu gốc, không nén lại.
- JPG, PNG, WebP, GIF; không đặt giới hạn số ảnh, dung lượng từng ảnh hay tổng dung lượng trong phần thêm ảnh. Khả năng lưu và xuất phụ thuộc bộ nhớ trình duyệt, thiết bị và giới hạn tệp của GitHub. Ảnh thư viện và slideshow được đóng gói thành file JavaScript riêng chứa dữ liệu ảnh để dùng được cả khi mở trực tiếp file và trên GitHub Pages. Không dùng video/Word trong bản thư viện ảnh này.
- ZIP xuất giữ đường dẫn tương đối, chạy được cả URL username.github.io/repository/.
- Xóa ảnh trong admin loại ảnh khỏi danh sách trong lần xuất kế tiếp; GitHub Upload files không tự xóa file photos cũ trên repo. Nếu muốn xóa dữ liệu ảnh cũ, xóa file photos/<mã-ảnh>.js trên GitHub. Dữ liệu từng commit vẫn có thể còn trong lịch sử Git. Không đăng ảnh riêng tư vào repo công khai.

CẤU TRÚC
index.html, gallery.html, admin.html: các trang.
site.css, home.js, gallery.js, admin.js: giao diện và tương tác.
shared.js, zip.js, draft-store.js: tiện ích, tạo ZIP, lưu bản chỉnh sửa.
gallery-data.js: danh sách ảnh và bài công khai.
photos/: dữ liệu các ảnh được xuất.
site-package.js: bộ file mẫu để nút Xuất website hoạt động không cần máy chủ.
.nojekyll: phục vụ các file tĩnh trực tiếp trên Pages.

Không cần server.py, Python, Supabase hay cơ sở dữ liệu để vận hành website này. Bản mới không tự nhập bài/file của backend Python cũ; chọn lại ảnh và sao chép bài muốn giữ. Chưa triển khai vào repo nào vì chưa được cung cấp quyền truy cập GitHub.

SLIDESHOW TRANG CHỦ
- Lời chào: Chào mừng thầy cô và các bạn đến với trang web! đặt trước phần chuyển trang 10 giây.
- Mặc định slideshow đổi ảnh sau 3 giây. Có nút ảnh trước/sau, chấm chọn ảnh và tạm dừng/tiếp tục.
- Trong Admin: dùng mục Slideshow trang chủ để tải ảnh riêng, sửa chú thích, sắp xếp và xóa. Ảnh slideshow không tự đưa vào Thư viện ảnh.
- Mục Slideshow trang chủ: bật/tắt, thời gian 2–30 giây, Xem trước trang chủ.
- Khi nâng cấp bản cũ, ảnh đã chọn cho slideshow được sao chép sang danh sách slideshow riêng để giữ nội dung. Sau đó hai danh sách sửa độc lập.
- Không có ảnh được chọn thì hiện khung giới thiệu; 1 ảnh thì không tự chuyển.
- Chọn Ở lại trang chủ để xem slideshow lâu hơn. Việc tạm dừng slideshow không dừng bộ đếm chuyển trang 10 giây.
- Sau thay đổi cần Xuất website rồi cập nhật repo GitHub như hướng dẫn trên.

Slideshow phủ toàn chiều rộng trang và ảnh lấp đầy khung (cover). Ảnh khác tỷ lệ khung có thể bị cắt một phần ở mép để không có khoảng trống. Nên dùng ảnh ngang.

KHO ẢNH LỚN 24 GB
Đã bổ sung chế độ liên kết ảnh bên ngoài, phân trang, nhập JSON và liên kết ZIP album. Xem EXTERNAL-STORAGE.txt để thiết lập Cloudflare R2 hoặc kho có URL HTTPS trực tiếp. prepare_gallery.py là công cụ chạy trên máy để tạo thumbnail/bản xem/ZIP và JSON; không cần chạy Python trên hosting. File mẫu sample-external.json dùng domain minh họa.
