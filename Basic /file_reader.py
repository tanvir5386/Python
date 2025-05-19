# এই কোডের মূল থিম হল একটি টেক্সট ফাইল পড়া
# এখানে 'sample.txt' নামক একটি ফাইল খোলা হচ্ছে এবং এর কন্টেন্ট পড়া হচ্ছে
# তারপর সেই কন্টেন্ট প্রিন্ট করা হচ্ছে

try:
    with open('sample.txt', 'r') as file:
        content = file.read()
    print("File Content:")
    print(content)
except FileNotFoundError:
    print("ত্রুটি: sample.txt not found here ")