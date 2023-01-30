import numpy as np

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from v_QV100_VOLTA import plot_QV100
from v_GTX480_FERMI import plot_GTX480
from v_TITAN_KEPLER import plot_TITAN
from v_TITANX_PASCAL import plot_TITANX
from v_TITANV_VOLTA import plot_TITANV
from v_RTX2060_TURING import plot_RTX2060
from v_RTX2060S_TURING import plot_RTX2060S
from v_RTX3070_AMPERE import plot_RTX3070

def plot(l1d, l2, dram, plot_type, gpu, kernel):

  l1d_rgb = np.zeros(((len(l1d), 3)), dtype = int)
  for i in range(0, len(l1d)):
    if (np.isnan(l1d[i][0])):
      l1d_rgb[i][0] = 150
      l1d_rgb[i][1] = 150
      l1d_rgb[i][2] = 150
    else:
      l1d_rgb[i][1] = int((l1d[i][0] + l1d[i][1]) * 255)
      l1d_rgb[i][0] = int((l1d[i][2] + l1d[i][4]) * 255)
      l1d_rgb[i][2] = int((l1d[i][3]) * 255)

  l2_rgb = np.zeros(((len(l2), 3)), dtype = int)
  for i in range(0, len(l2)):
    if (np.isnan(l2[i][0])):
      l2_rgb[i][0] = 100
      l2_rgb[i][1] = 100
      l2_rgb[i][2] = 100
    else:
      l2_rgb[i][1] = int((l2[i][0] + l2[i][1]) * 255)
      l2_rgb[i][0] = int((l2[i][2] + l2[i][4]) * 255)
      l2_rgb[i][2] = int(((l2[i][3])) * 255)

  dram_rgb = np.zeros(((len(dram), 3)), dtype = int)
  for i in range(0, len(dram)):
    if (np.isnan(l2[i][0])):
      dram_rgb[i][0] = 200
      dram_rgb[i][1] = 200
      dram_rgb[i][2] = 200
    else:
      dram_rgb[i][1] = int(dram[i][0] * 255)
      dram_rgb[i][0] = int(dram[i][1] * 255)
      dram_rgb[i][2] = 255

  image = Image.new(mode = "RGBA", size = (1920, 1080), color=(100, 100, 100))
  image_draw = ImageDraw.Draw(image)

  if kernel > 0:
    kernel -= 1

  if gpu == 'GTX480': #fermi
    image_draw = plot_GTX480(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'TITAN': #kepler
    image_draw = plot_TITAN(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'TITANX': #pascal
    image_draw = plot_TITANX(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'TITANV': #volta
    image_draw = plot_TITANV(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'QV100': #volta
    image_draw = plot_QV100(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'RTX2060': # turing
    image_draw = plot_RTX2060(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'RTX2060S': #turing
    image_draw = plot_RTX2060S(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
  elif gpu == 'RTX3070': #ampere
    image_draw = plot_RTX3070(image_draw, l1d, l2, dram, kernel,
                             l1d_rgb, l2_rgb, dram_rgb)
#  image.show()
  return image

#plot(None, None, None, None, 'GTX480')