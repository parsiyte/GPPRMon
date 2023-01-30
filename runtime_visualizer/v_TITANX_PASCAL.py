from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_TITANX(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  for i in range(0, 14):
  ## L1D [0, 28]
    image_draw.rectangle([(10 + (i*135), 10), (10 + 130 + (i*135), 10 + 130)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((11 + (i*135), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*135), 31),  "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 46),  "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 61), "M : " + '{:.4f}'.format( l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 76), "RF: " + '{:.4f}'.format( l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 91), "SM: " + '{:.4f}'.format( l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 106), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*135), 10 + 135), (10 + (i*135) + 130, 10 + 135 + 130)], outline = "white", 
                          fill = (l1d_rgb[i+14][0], l1d_rgb[i+14][1], l1d_rgb[i+14][2]))
    image_draw.text((11 + (i*135), 11 + 135), "L1 Data-" + str(i + 14), font = font_l1d, fill=(0,0,0))
    image_draw.text((11 + (i*135), 31 + 135),  "H : " + '{:.4f}'.format(l1d[i + 14][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 46 + 135),  "HR: " + '{:.4f}'.format(l1d[i + 14][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 61 + 135), "M : " + '{:.4f}'.format(l1d[i + 14][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 76 + 135), "RF: " + '{:.4f}'.format(l1d[i + 14][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 91 + 135), "SM: " + '{:.4f}'.format(l1d[i + 14][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*135), 106 + 135), "MH: " + '{:.4f}'.format(l1d[i + 14][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(10, 285), (1910, 345)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeMonoBold.ttf', 16)
  ## L2 [0, 24]
  for i in range(0, 12):
    image_draw.rectangle([(10 + (i*158), 355), (10 + 153 + (i*158), 80 + 355)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*158),  355), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11+(i*158), 355 + 20), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+(i*158), 355 + 35), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+(i*158), 355 + 50), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+78+(i*158),355 + 20), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+78+(i*158),355 + 35), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11+78+(i*158),355 + 50), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 440), (10 + 153 + (i*158), 620)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11 + (i*158), 441), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    image_draw.text((11 + (i*158), 441 + 30), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 441 + 50), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 625), (10 + 153 + (i*158), 705)], outline = "white", 
                          fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    image_draw.text((11 + (i*158), 626), "L2 Cache-" + str(i+ 12), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    image_draw.text((11 + (i*158), 626 + 20), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 626 + 35), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 626 + 50), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 78 + (i*158), 626 + 20), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 78 + (i*158), 626 + 35), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 78 + (i*158), 626 + 50), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l1d_data, fill=(0,0,0))

  image_draw.rectangle([(10, 750), (1900, 1040)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 760), 
                  "- TITANX GPU based on Pascal Architecture includes 28 Streaming Multiprocessors (28 L1D caches). ",
                  font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 25 + 760), 
                  "- There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.text((18, 70 + 760), "- H : Hits ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 95 + 760), "- M : Misses ", font = font_info, fill=(255,255,255)) 
  image_draw.text((18, 120+ 760), "- HR : Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 145+ 760), "- RF : Reservation Failures", font = font_info, fill=(255,255,255))
  image_draw.text((18, 170+ 760), "- MH : MSHR Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 195+ 760), "- SM : Sector Misses", font = font_info, fill=(255,255,255))
  image_draw.text((18, 220+ 760), "- RB-H : Row Buffer Hits", font = font_info, fill=(255,255,255))
  image_draw.text((18, 245+ 760), "- RB-M : Row Buffer Misses", font = font_info, fill=(255,255,255))

  image_draw.rectangle([(1700, 750), (1900, 810)], outline = "white", fill = (20,20,20))
  image_draw.text((1705, 760), " KERNEL = " + str(kernel),
                  font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255,25,25)) 
  return image_draw
