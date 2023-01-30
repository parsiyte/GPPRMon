from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_TITANV(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)

  ## L1D [0, 39]
  for i in range(0, 10):
    image_draw.rectangle([(10 + (i*190), 10), (100 + (i*190), 105)], outline = "white", 
                          fill = (l1d_rgb[i*4][0], l1d_rgb[i*4][1], l1d_rgb[i*4][2]))
    image_draw.text((11 + (i*190), 11), "L1 Data-" + str(i*4), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*190), 27), "H : " + '{:.4f}'.format(l2[i*4][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 40), "HR: " + '{:.4f}'.format(l2[i*4][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 53), "M : " + '{:.4f}'.format(l2[i*4][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 66), "RF: " + '{:.4f}'.format(l2[i*4][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 79), "SM: " + '{:.4f}'.format(l2[i*4][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 92), "MH: " + '{:.4f}'.format(l2[i*4][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(105 + (i*190), 10), (195 + (i*190), 105)], outline = "white", 
                          fill = (l1d_rgb[i*4+1][0], l1d_rgb[i*4+1][1], l1d_rgb[i*4+1][2]))
    image_draw.text((106 +(i*190), 11), "L1 Data-" + str(i*4+1), font = font_l1d, fill=(0,0,0))
    image_draw.text((106 + (i*190), 27), "H : " + '{:.4f}'.format(l2[i*4+1][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 + (i*190), 40), "HR: " + '{:.4f}'.format(l2[i*4+1][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 + (i*190), 53), "M : " + '{:.4f}'.format(l2[i*4+1][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 + (i*190), 66), "RF: " + '{:.4f}'.format(l2[i*4+1][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 + (i*190), 79), "SM: " + '{:.4f}'.format(l2[i*4+1][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 + (i*190), 92), "MH: " + '{:.4f}'.format(l2[i*4+1][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*190), 110), (100 + (i*190), 200)], outline = "white", 
                          fill = (l1d_rgb[i*4+2][0], l1d_rgb[i*4+2][1], l1d_rgb[i*4+2][2]))
    image_draw.text((11 + (i*190), 111), "L1 Data-" + str(i*4+2), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*190), 27 + 100), "H : " + '{:.4f}'.format(l2[i*4 + 2][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 40 + 100), "HR: " + '{:.4f}'.format(l2[i*4 + 2][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 53 + 100), "M : " + '{:.4f}'.format(l2[i*4 + 2][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 66 + 100), "RF: " + '{:.4f}'.format(l2[i*4 + 2][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 79 + 100), "SM: " + '{:.4f}'.format(l2[i*4 + 2][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*190), 92 + 100), "MH: " + '{:.4f}'.format(l2[i*4 + 2][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(105 + (i*190), 110), (195 + (i*190), 200)], outline = "white", 
                          fill = (l1d_rgb[i*4+3][0], l1d_rgb[i*4+3][1], l1d_rgb[i*4+3][2]))
    image_draw.text((106 +(i*190), 111), "L1 Data-" + str(i*4+3), font = font_l1d, fill=(0,0,0))
    image_draw.text((106 +(i*190), 27 + 100), "H : " + '{:.4f}'.format(l2[i*4 + 3][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 +(i*190), 40 + 100), "HR: " + '{:.4f}'.format(l2[i*4 + 3][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 +(i*190), 53 + 100), "M : " + '{:.4f}'.format(l2[i*4 + 3][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 +(i*190), 66 + 100), "RF: " + '{:.4f}'.format(l2[i*4 + 3][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 +(i*190), 79 + 100), "SM: " + '{:.4f}'.format(l2[i*4 + 3][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((106 +(i*190), 92 + 100), "MH: " + '{:.4f}'.format(l2[i*4 + 3][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  image_draw.rectangle([(15, 210), (1900, 250)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((180+16, 211), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475, 211), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 2, 211), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((180+16 + 475 * 3, 211), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  ## L2 [0, 48]
  for i in range(0, 12):
    image_draw.rectangle([(10 + (i*158), 255), (10 + 153 + (i*158), 345)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*158), 256), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*158), 20 + 256), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 256), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 256), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 256), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 256), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 256), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 350), (10 + 153 + (i*158), 440)],  outline = "white", 
                          fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    image_draw.text((11 + (i*158), 351), "L2 Cache-" + str(i + 12), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*158), 20 + 351), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 351), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 351), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 351), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 351), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 351), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 445), (10 + 153 + (i*158), 525)],  outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11 + (i*158), 446), "DRAM Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    image_draw.text((11 + (i*158), 446 + 30), "RB-H : " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 446 + 50), "RB-M : " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 530), (10 + 153 + (i*158), 615)],  outline = "white", 
                          fill = (dram_rgb[i+12][0], dram_rgb[i+12][1], dram_rgb[i+12][2]))
    image_draw.text((11 + (i*158), 530), "DRAM Bank-" + str(i+12), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    image_draw.text((11 + (i*158), 530 + 30), "RB-H : " + '{:.4f}'.format(dram[i+12][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 530 + 50), "RB-M : " + '{:.4f}'.format(dram[i+12][1]), font = font_l1d_data, fill=(0,0,0))

    image_draw.rectangle([(10 + (i*158), 620), (10 + 153 + (i*158), 710)],  outline = "white", 
                          fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    image_draw.text((11 + (i*158), 621), "L2 Cache-" + str(i+24), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*158), 20 + 621), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 621), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 621), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 621), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 621), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 621), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0,0,0)) 
    
    image_draw.rectangle([(10 + (i*158), 715), (10 + 153 + (i*158), 805)],  outline = "white", 
                          fill = (l2_rgb[i+36][0], l2_rgb[i+36][1], l2_rgb[i+36][2]))
    image_draw.text((11 + (i*158), 715), "L2 Cache-" + str(i+36), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*158), 20 + 716), "H : " + '{:.4f}'.format(l2[i + 36][0]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 35 + 716), "HR: " + '{:.4f}'.format(l2[i + 36][1]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + (i*158), 50 + 716), "M : " + '{:.4f}'.format(l2[i + 36][2]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 20 + 716), "RF: " + '{:.4f}'.format(l2[i + 36][3]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 35 + 716), "SM: " + '{:.4f}'.format(l2[i + 36][4]), font = font_l1d_data, fill=(0,0,0))
    image_draw.text((11 + 75 + (i*158), 50 + 716), "MH: " + '{:.4f}'.format(l2[i + 36][5]), font = font_l1d_data, fill=(0,0,0)) 

  image_draw.rectangle([(10, 835), (1885, 1055)], outline = "white", fill = (0,0,0))
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

  image_draw.rectangle([(1700, 835), (1900, 875)], outline = "white", fill = (20,20,20))
  image_draw.text((1700, 845), " KERNEL = " + str(kernel), font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255, 25, 25)) 

  return image_draw
