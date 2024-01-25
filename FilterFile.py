import random
import json

def filter(string):
  with open(string + '.txt', 'r', encoding='utf-8') as file:
    content = [line.strip() for line in file.readlines()]
  new_content = random.choices(content, k = 700)
  with open(string + '_filtered.txt', 'w', encoding='utf-8') as f:
      for line in new_content[:699]:
          f.write(f"{line}\n")
      f.write(new_content[699])


filter("text_i_k")
filter("text_l")
filter("text_m")
filter("text_n")
filter("text_o_p_q")
filter("text_r_s")
filter("text_t")
filter("text_u_v_x_y")