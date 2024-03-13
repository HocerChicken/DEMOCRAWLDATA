def merge_text_files(input_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for input_file in input_files:
            with open(input_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write('\n')

# Example usage
input_files = ['text_a_filtered.txt', 
               'text_b_filtered.txt', 
               'text_c_filtered.txt', 
               'text_d_filtered.txt', 
               'text_e_filtered.txt', 
               'text_f_g_filtered.txt', 
               'text_h_filtered.txt', 
               'text_i_k_filtered.txt', 
               'text_l_filtered.txt', 
               'text_m_filtered.txt', 
               'text_n_filtered.txt', 
               'text_o_p_q_filtered.txt', 
               'text_r_s_filtered.txt', 
               'text_t_filtered.txt', 
               'text_u_v_x_filtered.txt', 
               'text_y_filtered.txt']
output_file = 'merged_output.txt'

merge_text_files(input_files, output_file)
