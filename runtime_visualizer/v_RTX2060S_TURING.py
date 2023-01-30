from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_RTX2060S(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 33]
  for i in range(0, 17):
    image_draw.rectangle([(10 + (i*111), 10), (10 + 106 + (i*111), 10 + 106)], outline = "white", 
                           fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((11 + (i*111), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*111), 11 + 18), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 11 + 32), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 11 + 46), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 11 + 60), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 11 + 74), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 11 + 88), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*111), 10 + 111), (10 + 106 + (i*111), 10 + 217)], outline = "white", 
                           fill = (l1d_rgb[i+17][0], l1d_rgb[i+17][1], l1d_rgb[i+17][2]))
    image_draw.text((11 + (i*111), 122), "L1 Data-" + str(i + 17), font = font_l1d, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 18), "H : " + '{:.4f}'.format(l1d[i+17][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 32), "HR: " + '{:.4f}'.format(l1d[i+17][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 46), "M : " + '{:.4f}'.format(l1d[i+17][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 60), "RF: " + '{:.4f}'.format(l1d[i+17][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 74), "SM: " + '{:.4f}'.format(l1d[i+17][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*111), 122 + 88), "MH: " + '{:.4f}'.format(l1d[i+17][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(10, 235), (1910, 295)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeMonoBold.ttf', 16)
  ## L2 [0, 31]
  for i in range(0, 8):
    image_draw.rectangle([(10 + (i*237), 300), (10 + 232 + (i*237), 380)],  outline = "white", 
                           fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*237), 301), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) 
    image_draw.text((11 + (i*237), 20 + 301), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 35 + 301), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 50 + 301), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 20 + 301), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 35 + 301), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 50 + 301), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*237), 385), (10 + 232 + (i*237), 465)],  outline = "white", 
                           fill = (l2_rgb[i+8][0], l2_rgb[i+8][1], l2_rgb[i+8][2]))
    image_draw.text((11 + (i*237), 386), "L2 Cache-" + str(i + 8), font = font_l1d, fill=(0, 0, 0)) 
    image_draw.text((11 + (i*237), 20 + 386), "H : " + '{:.4f}'.format(l2[i + 8][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 35 + 386), "HR: " + '{:.4f}'.format(l2[i + 8][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 50 + 386), "M : " + '{:.4f}'.format(l2[i + 8][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 20 + 386), "RF: " + '{:.4f}'.format(l2[i + 8][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 35 + 386), "SM: " + '{:.4f}'.format(l2[i + 8][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 50 + 386), "MH: " + '{:.4f}'.format(l2[i + 8][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*237), 655), (10 + 232 + (i*237), 735)],  outline = "white", 
                           fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
    image_draw.text((11 + (i*237), 656), "L2 Cache-" + str(i + 16), font = font_l1d, fill=(0, 0, 0)) 
    image_draw.text((11 + (i*237), 20 + 656), "H : " + '{:.4f}'.format(l2[i + 16][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 35 + 656), "HR: " + '{:.4f}'.format(l2[i + 16][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 50 + 656), "M : " + '{:.4f}'.format(l2[i + 16][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 20 + 656), "RF: " + '{:.4f}'.format(l2[i + 16][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 35 + 656), "SM: " + '{:.4f}'.format(l2[i + 16][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 50 + 656), "MH: " + '{:.4f}'.format(l2[i + 16][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*237), 740), (10 + 232 + (i*237), 820)],  outline = "white", 
                           fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    image_draw.text((11 + (i*237), 741), "L2 Cache-" + str(i + 24), font = font_l1d, fill=(0, 0, 0)) 
    image_draw.text((11 + (i*237), 20 + 741), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 35 + 741), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*237), 50 + 741), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 20 + 741), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 35 + 741), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 +  115 + (i*237), 50 + 741), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0,0,0))

  ## L2 [0, 31]
  for i in range(0, 16):
    image_draw.rectangle([(10 + (i*118), 470), (10 + 113 + (i*118), 650)],  outline = "white", 
                           fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11 + (i*118), 471), "DRAM Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) 
    image_draw.text((11 + (i*118), 30 + 471), "RB-H " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*118), 50 + 471), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

  image_draw.rectangle([(10, 840), (1910, 1065)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 845), 
                  "- RTX2060S GPU based on Turing Architecture includes 34 Streaming Multiprocessors (34 L1D cache). ",
                  font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 865), 
                  "- There are 16 memory partitions (16 Seperate DRAM Banks) with 2 sub-partitions (32 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.text((18, 865 + 30), "- H: Hits ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 865 + 50), "- M: Misses ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 865 + 70), "- HR: Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 865 + 90), "- RF: Reservation Failures", font = font_info, fill=(255,255,255))
  image_draw.text((18, 865 + 110), "- MH: MSHR Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 865 + 130), "- SM: Sector Misses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 865 + 150), "- RB-H: Row Buffer Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 865 + 170), "- RB-M: Row Buffer Misses", font = font_info, fill=(255,255,255))

  image_draw.rectangle([(1700, 840), (1910, 880)], outline = "white", fill = (0,0,0))
  image_draw.text((1710, 850), " KERNEL = " + str(kernel), font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255,255,255)) 


  return image_draw
