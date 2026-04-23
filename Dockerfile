# සැහැල්ලු Python 3.11 image එකක් පාවිච්චි කරනවා
FROM python:3.11-slim

# Container එක ඇතුලේ අපේ වැඩ කරන directory එක හදාගන්නවා
WORKDIR /app

# Requirements file එක container එකට copy කරලා libraries ටික install කරගන්නවා
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# අපේ python code ටික container එකට copy කරනවා
COPY . .

# Flask app එක run වෙන port එක expose කරනවා
EXPOSE 5000

# Container එක start වෙද්දි Run වෙන්න ඕන command එක
CMD ["python", "test_sec.py"]