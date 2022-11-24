from read_write.read_file import read_from_file, write_to_file


def lps_array(pattern, pattern_length, lps):
    len = 0
    i = 1
    while i < pattern_length:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len - 1]

            else:
                lps[i] = 0
                i += 1


def kmp_search_in_string(pattern, string):
    pattern_length = len(pattern)
    text_length = len(string)
    lps = [0] * pattern_length
    j = 0
    result_match_list = []
    lps_array(pattern, pattern_length, lps)
    i = 0
    while i < text_length:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == pattern_length:
            result_match_list.append("[" + str(i - j) + "-" + str(i - j + pattern_length - 1) + "]")
            j = lps[j - 1]
        elif pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result_match_list


if __name__ == '__main__':
    result = read_from_file("test.in")
    pattern = result[1]
    string = result[0]

    write_to_file(kmp_search_in_string(pattern, string), "result")
