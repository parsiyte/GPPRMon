from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_RTX2060(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 30]
  for i in range(0, 15):
    image_draw.rectangle([(10 + (i*126), 10), (10 + 121 + (i*126), 10 + 121)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((11 + (i*126), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*126), 31), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 46), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 61), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 76), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 91), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 106), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*126), 136), (10 + 121 + (i*126), 10 + 247)], outline = "white", 
                          fill = (l1d_rgb[i+15][0], l1d_rgb[i+15][1], l1d_rgb[i+15][2]))
    image_draw.text((11 + (i*126), 11 + 125), "L1 Data-" + str(i + 15), font = font_l1d, fill=(0,0,0))
    image_draw.text((11 + (i*126), 31 + 125), "H : " + '{:.4f}'.format(l1d[i + 15][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 46 + 125), "HR: " + '{:.4f}'.format(l1d[i + 15][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 61 + 125), "M : " + '{:.4f}'.format(l1d[i + 15][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 76 + 125), "RF: " + '{:.4f}'.format(l1d[i + 15][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 91 + 125), "SM: " + '{:.4f}'.format(l1d[i + 15][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*126), 106 + 125), "MH: " + '{:.4f}'.format(l1d[i + 15][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(10, 265), (1910, 325)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  ## L2 [0, 32]
  ## DRAM [0, 16]
  for i in range(0, 12):
    image_draw.rectangle([(10 + (i*158), 330), (10 + 153 + (i*158), 430)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*158), 331), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*158), 20 + 331), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 331), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 331), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 331), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 331), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 331), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 435), (10 + 153 + (i*158), 600)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11 + (i*158), 436), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    image_draw.text((11 + (i*158), 20 + 436), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 436), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 605), (10 + 153 + (i*158), 705)], outline = "white", 
                          fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    image_draw.text((11 + (i*158), 606), "L2 Cache-" + str(i+12), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    image_draw.text((11 + (i*158), 20 + 606), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 606), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 606), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 606), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 606), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 606), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l1d_data, fill=(0,0,0))

  image_draw.rectangle([(10, 835), (1900, 1055)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 840), 
                  "- TITAN GPU based on Kepler Architecture includes 14 Streaming Multiprocessors (14 L1D caches). ",
                  font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 860), 
                  "- There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.text((18, 860 + 30), "- H: Hits ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 860 + 50), "- M: Misses ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 860 + 70), "- HR: Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 860 + 90), "- RF: Reservation Failures", font = font_info, fill=(255,255,255))
  image_draw.text((18, 860 + 110), "- MH: MSHR Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 860 + 130), "- SM: Sector Misses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 860 + 150), "- RB-H: Row Buffer Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 860 + 170), "- RB-M: Row Buffer Misses", font = font_info, fill=(255,255,255))

  image_draw.rectangle([(1700, 835), (1900, 875)], outline = "white", fill = (0,0,0))
  image_draw.text((1720, 845), " KEPLER = " + str(kernel), font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255,255,255)) 

  return image_draw
