import matplotlib.pyplot as plt
import numpy as np

# plt.figure()
# plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
# plt.show()

# Numpy를 이용하여 Dummy 데이터 생성 후, sin()을 이용하여 시각화
# t = np.arange(0, 10, 0.01)
# y = np.sin(t)
# plt.plot(t, y)
# plt.show()

# Grid 추가
# plt.plot(t, y)
# plt.grid()
# plt.show()

# x축 y축 라벨
# plt.plot(t, y)
# plt.grid()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.show()

# 제목 추가
# plt.figure(figsize=(10, 6))
# plt.plot(t, y)
# plt.grid()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.title("Sample Graph")
# plt.show()

# sin과 cos 한번에 시각하
# plt.figure(figsize=(10, 6))
# plt.plot(t, np.sin(t))
# plt.plot(t, np.cos(t))
# plt.grid()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.title("Sample Graph")
# plt.show()

# 범례(라벨) 추가
# plt.figure(figsize=(10, 6))
# plt.plot(t, np.sin(t), label='sin')
# plt.plot(t, np.cos(t), label='cos')
# plt.grid()
# plt.legend()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.title("Sample Graph")
# plt.show()

# 선의 모양 두꼐 설정
# plt.figure(figsize=(10, 6))
# plt.plot(t, np.sin(t), lw=3, label='sin')
# plt.plot(t, np.cos(t), 'r', label='cos')
# plt.grid()
# plt.legend()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.title("Sample Graph")
# plt.show()

# x축과 y축에 대한 값 변경(limit)
# plt.figure(figsize=(10, 6))
# plt.plot(t, np.sin(t), lw=3, label='sin')
# plt.plot(t, np.cos(t), 'r', label='cos')
# plt.grid()
# plt.legend()
# plt.xlabel('time')
# plt.ylabel('Amplitude')
# plt.title("Sample Graph")
# plt.xlim(0, np.pi)
# plt.ylim(-1.2, 1.2)
# plt.show()

# 다양한 모양
# t = np.arange(0, 5, 0.5)
# plt.figure(figsize=(10, 6))
# plt.plot(t, t, 'r--')
# plt.plot(t, t**2, 'bs')
# plt.plot(t, t**3, 'g^')
# plt.show()

# 색상, 선스타일 변경 두 번째 방법
# t = [0, 1, 2, 3, 4, 5, 6]
# y = [1, 4, 5, 8, 9, 5, 3]
# plt.figure(figsize=(10, 6))
# plt.plot(t, y, color="green")
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(t, y, color='green', linestyle='dashed')
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(t, y, color='green', linestyle='dashed', marker='o')
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(t, y, color='green', linestyle='dashed', marker='o', markerfacecolor='blue')
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(t, y, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
# plt.show()

# 산점도
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])

plt.figure(figsize=(10, 6))
plt.scatter(t, y)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(t, y, marker=">")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(t, y, marker=">", s=50)
plt.show()

colormap = t

plt.figure(figsize=(10, 6))
plt.scatter(t, y, marker=">", s=50, c=colormap)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(t, y, marker=">", s=50, c=colormap)
plt.colorbar()
plt.show()