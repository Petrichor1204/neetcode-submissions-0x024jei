class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # goal: take a list of words and turn them into a list of strings wwhich has each line left and right justified, with max width chars, and last line only left justified. numchars = 14 temp_list = [justification]
        # [[this, is, an] [example, of, text][justification]]
        result = []
        to_justify = []
        num_chars = 0
        i = 0
        temp_list = []
        # iterate through words
        while i < len(words):
            additional = len(words[i]) if len(temp_list) == 0 else len(words[i]) + 1
            if num_chars + additional > maxWidth:
                to_justify.append(temp_list)
                num_chars = 0
                temp_list = []
            else:
                num_chars += additional
                temp_list.append(words[i])
                i += 1
                
        if temp_list and num_chars > 0:
            to_justify.append(temp_list)

        last_line = len(to_justify) 

        line_count = 0
        for temp_list in to_justify:
            line_count += 1
            num_spaces = maxWidth - len("".join(temp_list))
            to_fill = len(temp_list) - 1
            if to_fill > 0:
                spaces_needed = num_spaces // to_fill
                extra_spaces = num_spaces % to_fill
            else:
                spaces_needed = num_spaces
            

            if line_count == last_line or len(temp_list) == 1:
                line = " ".join(temp_list)
                line += " " * (maxWidth - len(line))
                result.append(line)
            else:

                curr_list = []
                curr_list.append(temp_list[0])

                for i in range(1, len(temp_list)):
                    spaces = spaces_needed + (1 if i <= extra_spaces else 0)
                    curr_list.append(" " * spaces)
                    curr_list.append(temp_list[i])

                result.append("".join(curr_list))

        return result
                


        
        
        