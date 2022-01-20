import numpy as np
import cv2 as cv

image = np.random.normal(loc=32767.0, scale=32767.5, size=(5, 5)).astype(np.uint8)
print(image) # Матрица

mask = (1/25)*np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], dtype=np.int8)
print(mask) # Маска

output = cv.filter2D(image, -1, mask, borderType=cv.BORDER_CONSTANT)
print(output) # После фильтрации усредненным фильтром

noise_input=np.std(image)
print(noise_input)

noise_output=np.std(output)
print(noise_output)
#k=noise_input/noise_output
#print(k)

m_median = cv.medianBlur(image,5)
print(m_median) # Фильтрация медианным фильтром
print(m_median [2][2])
noise_median = np.std(m_median)
print(noise_median,'\n')

i_sort = np.sort(image)
print('Sort \n', i_sort[2][2]) #Сортировка на всякий случай