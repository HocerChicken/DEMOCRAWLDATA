def filter(string):
  with open(string + '.txt', 'r', encoding='utf-8') as file:
    content = [line.strip() for line in file.readlines()]
  with open(string + '_filtered.txt', 'w', encoding='utf-8') as f:
      for line in content:
          f.write(f"{line.split(' ')[0]}\n")
          
def remove_duplicates(input_file, output_file):
    unique_words = set()

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                unique_words.add(word)

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for word in sorted(unique_words):  
            output_file.write(f"{word}\n")

remove_duplicates("text_a_filtered.txt", "text_a_filtered.txt")
remove_duplicates("text_b_filtered.txt", "text_b_filtered.txt")
remove_duplicates("text_c_filtered.txt", "text_c_filtered.txt")
remove_duplicates("text_d_filtered.txt", "text_d_filtered.txt")
remove_duplicates("text_e_filtered.txt", "text_e_filtered.txt")
remove_duplicates("text_f_g_filtered.txt", "text_f_g_filtered.txt")
remove_duplicates("text_h_filtered.txt", "text_h_filtered.txt")
remove_duplicates("text_i_k_filtered.txt", "text_i_k_filtered.txt")
remove_duplicates("text_l_filtered.txt", "text_l_filtered.txt")
remove_duplicates("text_m_filtered.txt", "text_m_filtered.txt")
remove_duplicates("text_n_filtered.txt", "text_n_filtered.txt")
remove_duplicates("text_o_p_q_filtered.txt", "text_o_p_q_filtered.txt")
remove_duplicates("text_r_s_filtered.txt", "text_r_s_filtered.txt")
remove_duplicates("text_t_filtered.txt", "text_t_filtered.txt")
remove_duplicates("text_u_v_x_filtered.txt", "text_u_v_x_filtered.txt")
remove_duplicates("text_y_filtered.txt", "text_y_filtered.txt")