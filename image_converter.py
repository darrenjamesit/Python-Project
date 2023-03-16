from PIL import Image
import psycopg2
import io
import os

for root, dirs, files in os.walk('path/to/start'):
    print(root)
    print(dirs)
    print(files)