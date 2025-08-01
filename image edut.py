from PIL import Image, ImageFilter

# ইমেজ লোড করুন
image = Image.open("https://1drv.ms/i/c/0eb207ada2c8189d/EYeLQZoiKyBEqvidCXL6IOUB-cDD4QQy3IPytjx2e8Q8wg?e=aoN5sk")

# ইমেজ রিসাইজ করুন
resized_image = image.resize((300, 200))
resized_image.save("resized.jpg")

# ইমেজ রোটেট করুন
rotated_image = image.rotate(45)
rotated_image.save("rotated.jpg")

# ব্লার ফিল্টার প্রয়োগ করুন
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("blurred.jpg")

# গ্রেস্কেল কনভার্ট করুন
grayscale_image = image.convert("L")
grayscale_image.save("grayscale.jpg")

print("ইমেজ এডিটিং সম্পন্ন হয়েছে!")