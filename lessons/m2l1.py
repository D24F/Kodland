'''# Kode ini memungkinkan kita untuk membaca seluruh isi file teks.
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()'''

import os
print(os.listdir('images'))