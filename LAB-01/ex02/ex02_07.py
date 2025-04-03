print("Nhập 'done' để kết thúc ")
lines =[]
while True:
    line = input("Nhập dòng văn bản: ")
    if line.strip() == 'done':
        break
    lines.append(line)
print("Các dòng văn bản sau khi chuyển thành công thành chữ hoa:")
for line in lines:
    print(line.upper())
    