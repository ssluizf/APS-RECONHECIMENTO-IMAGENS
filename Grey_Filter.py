
def greyFilter(img, gamma):
  r,g,b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

  r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

  grayscale_image = r * r_const ** gamma + g * g_const ** gamma + b * b_const ** gamma

  return grayscale_image
