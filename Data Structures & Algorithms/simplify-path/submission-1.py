class Solution:
    def simplifyPath(self, path: str) -> str:
        # simplify the path to follow these rules:
            # the new path should not have any single or double dots
            # must start with a slash
            # must not end with a slash
            # each directory separated by single slash

        # path = "/neetcode/practice//...///../courses"
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        # "/..//"    = ['', '..', '']                                           
        # path="/a/./b/../../c/"
        # [a/c]
        # "/c"
        new_path = path.split('/')
        stack = []
       
        for char in new_path:
            if char == '' or char == '.':
                continue
            elif stack and char == '..':
                stack.pop()
            else:
                if char != "..":
                    stack.append(char)

        return "/" + "/".join(stack)

            


        
