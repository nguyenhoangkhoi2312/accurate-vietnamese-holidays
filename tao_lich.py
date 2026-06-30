import datetime
from lunar_python import Lunar

def calculate_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return datetime.date(year, month, day)

def get_solar_from_lunar(year, month, day):
    lunar = Lunar.fromYmd(year, month, day)
    solar = lunar.getSolar()
    return datetime.date(solar.getYear(), solar.getMonth(), solar.getDay())

def write_event(f, start_date, duration_days, summary):
    end_date = start_date + datetime.timedelta(days=duration_days)
    f.write("BEGIN:VEVENT\n")
    f.write(f"DTSTART;VALUE=DATE:{start_date.strftime('%Y%m%d')}\n")
    f.write(f"DTEND;VALUE=DATE:{end_date.strftime('%Y%m%d')}\n")
    f.write(f"SUMMARY:{summary}\n")
    f.write("END:VEVENT\n")

def generate_calendar():
    with open("lich_vietnam_2026_2200.ics", "w", encoding="utf-8") as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//Holidays//Vietnam//VI\n")
        f.write("CALSCALE:GREGORIAN\n")
        f.write("METHOD:PUBLISH\n")

        for year in range(2026, 2201):
            # Sự kiện Dương lịch
            write_event(f, datetime.date(year, 1, 1), 1, "Tết Dương Lịch")
            write_event(f, datetime.date(year, 2, 14), 1, "Ngày Valentine")
            write_event(f, datetime.date(year, 2, 27), 1, "Ngày Thầy thuốc Việt Nam")
            write_event(f, datetime.date(year, 3, 8), 1, "Ngày Quốc tế Phụ nữ")
            write_event(f, datetime.date(year, 3, 26), 1, "Ngày thành lập Đoàn TNCS Hồ Chí Minh")
            write_event(f, datetime.date(year, 4, 30), 1, "Ngày Giải phóng miền Nam, thống nhất đất nước")
            write_event(f, datetime.date(year, 5, 1), 1, "Ngày Quốc tế Lao động (Nghỉ lễ toàn quốc)")
            write_event(f, datetime.date(year, 5, 7), 1, "Chiến thắng Điện Biên Phủ")
            write_event(f, datetime.date(year, 6, 1), 1, "Ngày Quốc tế Thiếu nhi")
            write_event(f, datetime.date(year, 6, 21), 1, "Ngày Báo chí Cách mạng Việt Nam")
            write_event(f, datetime.date(year, 6, 28), 1, "Ngày Gia đình Việt Nam")
            write_event(f, datetime.date(year, 7, 27), 1, "Ngày Thương binh, Liệt sĩ")
            write_event(f, datetime.date(year, 8, 19), 1, "Ngày Cách mạng tháng Tám")
            write_event(f, datetime.date(year, 9, 1), 1, "Nghỉ lễ Quốc khánh bổ sung")
            write_event(f, datetime.date(year, 9, 2), 1, "Ngày Quốc khánh")
            write_event(f, datetime.date(year, 10, 20), 1, "Ngày Phụ nữ Việt Nam")
            write_event(f, datetime.date(year, 11, 20), 1, "Ngày Nhà giáo Việt Nam")
            write_event(f, datetime.date(year, 11, 24), 1, "Ngày Văn hóa Việt Nam")
            write_event(f, datetime.date(year, 12, 22), 1, "Ngày thành lập Quân đội Nhân dân Việt Nam")
            write_event(f, datetime.date(year, 12, 24), 1, "Lễ Giáng Sinh")
            
            easter_date = calculate_easter(year)
            write_event(f, easter_date, 1, "Lễ Phục Sinh")

            # Sự kiện Âm lịch
            try:
                mung_1_tet = get_solar_from_lunar(year, 1, 1)
                
                # Tính lùi để luôn lấy đúng ngày trước Tết bất kể tháng Chạp có 29 hay 30 ngày
                giao_thua = mung_1_tet - datetime.timedelta(days=1)
                ngay_29_tet = mung_1_tet - datetime.timedelta(days=2)
                ngay_28_tet = mung_1_tet - datetime.timedelta(days=3)

                write_event(f, get_solar_from_lunar(year - 1, 12, 23), 1, "Tết ông Công ông Táo (23 tháng Chạp)")
                write_event(f, ngay_28_tet, 1, "28 Tết Nguyên Đán")
                write_event(f, ngay_29_tet, 1, "29 Tết Nguyên Đán")
                write_event(f, giao_thua, 1, "Giao Thừa (Đêm Tất Niên)")
                
                write_event(f, mung_1_tet, 1, "Mùng 1 Tết Nguyên Đán (Nghỉ lễ toàn quốc)")
                write_event(f, mung_1_tet + datetime.timedelta(days=1), 1, "Mùng 2")
                write_event(f, mung_1_tet + datetime.timedelta(days=2), 1, "Mùng 3")
                write_event(f, mung_1_tet + datetime.timedelta(days=3), 1, "Mùng 4")
                write_event(f, mung_1_tet + datetime.timedelta(days=4), 1, "Mùng 5")

                write_event(f, get_solar_from_lunar(year, 1, 15), 1, "Tết Nguyên Tiêu (15 tháng Giêng)")
                write_event(f, get_solar_from_lunar(year, 3, 3), 1, "Tết Hàn Thực (3 tháng 3 Âm lịch)")
                write_event(f, get_solar_from_lunar(year, 3, 10), 1, "Giỗ Tổ Hùng Vương (Nghỉ lễ toàn quốc - 10 tháng 3 Âm lịch)")
                write_event(f, get_solar_from_lunar(year, 4, 15), 1, "Lễ Phật Đản (15 tháng 4 Âm lịch)")
                write_event(f, get_solar_from_lunar(year, 5, 5), 1, "Tết Đoan Ngọ (5 tháng 5 Âm lịch)")
                write_event(f, get_solar_from_lunar(year, 7, 15), 1, "Lễ Vu Lan(15 tháng 7 Âm lịch)")
                write_event(f, get_solar_from_lunar(year, 8, 15), 1, "Tết Trung Thu (15 tháng 8 Âm lịch)")

            except Exception as e:
                print(f"Lỗi khi xử lý âm lịch năm {year}: {e}")

        f.write("END:VCALENDAR\n")
        print("Đã tạo thành công tệp lich_vietnam_2026_2200.ics")

if __name__ == "__main__":
    generate_calendar()
