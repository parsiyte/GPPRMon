from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 15 L1D,12 L2, 6 DRAM banks
def plot_GTX480(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)

  ## L1D [0, 14]
  for i in range(0, 15):
    image_draw.rectangle([(10 + (i*126), 10), (10 + 120 + (i*126), 10+120)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((12 + (i*126), 12), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((12 + (i*126), 32), "H  : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((12 + (i*126), 45), "HR : " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((12 + (i*126), 60), "M  : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((12 + (i*126), 75), "RF : " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((12 + (i*126), 90), "SM : " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((12 + (i*126), 105), "MH : " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(10, 145), (1900, 145+55)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 150), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 150), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 150), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 150), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  ## L2 [0, 11]
  font_l2_data = ImageFont.truetype('FreeMonoBold.ttf', 14)
  for i in range(0, 6):
    image_draw.rectangle([(10 + (i*320), 10 + 210), (10 + 300 + (i*320), 10 + 300)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((12 + (i*320), 12 + 210), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 5]
    image_draw.text((12 + (i*320), 12 + 230), "H  : " + '{:.4f}'.format(l1d[i][0]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + (i*320), 12 + 250), "HR : " + '{:.4f}'.format(l1d[i][1]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + (i*320), 12 + 270), "M  : " + '{:.4f}'.format(l1d[i][2]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 230), "RF : " + '{:.4f}'.format(l1d[i][3]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 250), "SM : " + '{:.4f}'.format(l1d[i][4]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 270), "MH : " + '{:.4f}'.format(l1d[i][5]), font = font_l2_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*320), 10 + 300 + 10), (10 + 300 + (i*320), 10+ 300 + 90)], outline = "white", 
                         fill = (l2_rgb[i+6][0], l2_rgb[i+6][1], l2_rgb[i+6][2]))
    image_draw.text((12 + (i*320), 12 + 300 + 10), "L2 Cache-" + str(i+6), font = font_l1d, fill=(0, 0, 0)) #L2 [6, 11]
    image_draw.text((12 + (i*320), 12 + 330), "H  : " + '{:.4f}'.format(l1d[i+6][0]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + (i*320), 12 + 350), "HR : " + '{:.4f}'.format(l1d[i+6][1]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + (i*320), 12 + 370), "M  : " + '{:.4f}'.format(l1d[i+6][2]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 330), "RF : " + '{:.4f}'.format(l1d[i+6][3]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 350), "SM : " + '{:.4f}'.format(l1d[i+6][4]), font = font_l2_data, fill=(0,0,0))
    image_draw.text((12 + 150 + (i*320), 12 + 370), "MH : " + '{:.4f}'.format(l1d[i+6][5]), font = font_l2_data, fill=(0,0,0))

  ## DRAM [0, 6]
  for i in range(0, 6):
    image_draw.rectangle([(10+(i*320), 10+ 300 + 100), (10+300+(i*320), 600)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((12+(i*320), 12+ 300 + 100), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    image_draw.text((18 + (i*320), 440), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((18 + (i*320), 470), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

  image_draw.rectangle([(1700, 620), (1900, 660)], outline = "white", fill = (20,20,20))
  image_draw.text((1700, 630), " KERNEL = " + str(kernel), font = ImageFont.truetype('FreeMonoBold.ttf', 20) , fill=(255,10,10)) 

  image_draw.rectangle([(10, 680), (1900, 1000)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 700), 
                  "- TITAN GPU based on Kepler Architecture includes 14 Streaming Multiprocessors (14 L1D caches). ",
                  font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 25 + 700), 
                  "- There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.text((18, 70 + 700), "- H: Hits ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 95 + 700), "- M: Misses ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 120 +700), "- HR: Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 145 +700), "- RF: Reservation Failures", font = font_info, fill=(255,255,255))
  image_draw.text((18, 170 +700), "- MH: MSHR Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 195 +700), "- SM: Sector Misses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 220 +700), "- RB-H: Row Buffer Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 245 +700), "- RB-M: Row Buffer Misses", font = font_info, fill=(255,255,255))

  return image_draw
