from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_TITAN(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)

  ## L1D [0, 14]
  for i in range(0, 14):
    image_draw.rectangle([(10 + (i*136), 10), (10 + 130 + (i*136), 10 + 130)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((11 + (i*136), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*136), 30), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*136), 45), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*136), 60), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*136), 75), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*136), 90), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*136), 105), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(10, 155), (1900, 205)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 160), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 160), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 160), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 160), "NOCs", font = font_NOCs, fill=(0, 0, 0))

#  ## L2 [0, 23]
  for i in range(0, 8):
    image_draw.rectangle([(10 + (i*236), 10 + 215), (10 + 230 + (i*236), 10 + 215 + 90)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*236), 11 + 215), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 11 + 235), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 250), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 265), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 235), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 250), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 265), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*236), 10 + 215 + 95), (10 + 230 + (i*236), 10 + 215 + 95 + 90)],  outline = "white", 
                          fill = (l2_rgb[i+8][0], l2_rgb[i+8][1], l2_rgb[i+8][2]))
    image_draw.text((11 + (i*236), 11 + 215 + 95), "L2 Cache-" + str(i + 8), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 11 + 330), "H : " + '{:.4f}'.format(l2[i + 8][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 345), "HR: " + '{:.4f}'.format(l2[i + 8][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 360), "M : " + '{:.4f}'.format(l2[i + 8][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 330), "RF: " + '{:.4f}'.format(l2[i + 8][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 345), "SM: " + '{:.4f}'.format(l2[i + 8][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 360), "MH: " + '{:.4f}'.format(l2[i + 8][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*236), 10 + 215 + 190), (10 + 230 + (i*236), 10 + 215 + 280)],  outline = "white", 
                          fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
    image_draw.text((11 + (i*236), 11 + 215 + 190), "L2 Cache-" + str(i + 16), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 11 + 425), "H : " + '{:.4f}'.format(l2[i + 16][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 440), "HR: " + '{:.4f}'.format(l2[i + 16][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*236), 11 + 455), "M : " + '{:.4f}'.format(l2[i + 16][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 425), "RF: " + '{:.4f}'.format(l2[i + 16][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 440), "SM: " + '{:.4f}'.format(l2[i + 16][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 115 + (i*236), 11 + 455), "MH: " + '{:.4f}'.format(l2[i + 16][5]), font = font_l1d_data, fill=(0,0,0))

  ## DRAM [0, 15]
  for i in range(0, 12):
    image_draw.rectangle([(10+(i*157), 520), (10+150+(i*157), 720)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11+(i*158), 521), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    image_draw.text((11+(i*158), 545), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+(i*158), 565), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

  image_draw.rectangle([(10, 15 + 215 + 280 + 220), (1900, 245 + 215 + 280 + 250)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 20 + 215 + 280 + 220), 
                  "- TITAN GPU based on Kepler Architecture includes 14 Streaming Multiprocessors (14 L1D caches). ",
                  font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 45 + 215 + 280 + 220), 
                  "- There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.text((18, 70 + 215 + 280 + 220), "- H: Hits ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 95 + 215 + 280 + 220), "- M: Misses ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 120 + 215 + 280 + 220), "- HR: Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 145 + 215 + 280 + 220), "- RF: Reservation Failures", font = font_info, fill=(255,255,255))
  image_draw.text((18, 170 + 215 + 280 + 220), "- MH: MSHR Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 195 + 215 + 280 + 220), "- SM: Sector Misses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 220 + 215 + 280 + 220), "- RB-H: Row Buffer Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 245 + 215 + 280 + 220), "- RB-M: Row Buffer Misses", font = font_info, fill=(255,255,255))

  image_draw.rectangle([(1700, 15 + 215 + 280 + 220), (1900, 775)], outline = "white", fill = (20,20,20))
  image_draw.text((1710, 740), " KERNEL = " + str(kernel), font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255,25,25)) 

  return image_draw
