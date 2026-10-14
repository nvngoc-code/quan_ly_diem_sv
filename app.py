import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu
data = {
    'Ho_va_ten': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyen_can': [8.0, 9.0, 7.5, 6.0, 8.5, 9.5, 7.0, 8.0, 6.5, 9.0],
    'Giua_ky': [7.0, 8.5, 8.0, 5.5, 9.0, 8.0, 6.5, 7.5, 6.0, 8.5],
    'Cuoi_ky': [7.5, 8.0, 8.5, 5.0, 8.5, 9.0, 7.0, 8.0, 6.5, 9.0]
}

df = pd.DataFrame(data)
df['Tong_ket'] = (0.2 * df['Chuyen_can']) + (0.3 * df['Giua_ky']) + (0.5 * df['Cuoi_ky'])
df['Tong_ket'] = df['Tong_ket'].round(2)

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết của sinh viên")
st.dataframe(df)

# Thống kê
st.subheader("2. Thông tin thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên điểm cao nhất:** {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']})")
st.write(f"- **Sinh viên điểm thấp nhất:** {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']})")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}")

# Danh sách chọn sinh viên
st.subheader("3. Tra cứu thông tin từng sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

st.write(f"Chi tiết điểm của **{selected_student}**:")
st.write(f"- Chuyên cần: {student_info['Chuyen_can']}")
st.write(f"- Giữa kỳ: {student_info['Giua_ky']}")
st.write(f"- Cuối kỳ: {student_info['Cuoi_ky']}")
st.write(f"- **Tổng kết:** {student_info['Tong_ket']}")
st.write(f"- **Xếp loại:** {student_info['Xep_loai']}")

# Trực quan hóa biểu đồ
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Họ và tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
for i, v in enumerate(df['Tong_ket']):
    ax.text(i, v + 0.1, str(v), ha='center', fontsize=9)
st.pyplot(fig)

# Chân trang (Họ tên và MSSV)
st.markdown("---")
st.markdown("<p style='font-size: small; color: gray;'>Người tạo ứng dụng: [Họ Tên Của Bạn] - [MSSV]</p>", unsafe_allow_html=True)
