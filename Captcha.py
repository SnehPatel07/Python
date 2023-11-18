from captcha.image import ImageCaptcha
a = "5N3HP473L"
image = ImageCaptcha(width = 500, height = 100)

data = image.generate("5N3HP473L")

image.write(a,"captcha.png")