

class Scanner():

    def __init__(self,str_input):
        self.tokens=[]
        self.str_input= str_input + ';'
        self.token_type={'S': "special_sympole",'O' :"operator","N":"number"}

    @staticmethod
    def is_digit(c):
        if 48 <= ord(c) and 57 >= ord(c):
            return True
        return False

    @staticmethod
    def is_operator(c):
        if c == '+' or c == '-' or c == '*' or c == '/' or c == '%' or c == '&' or c == '|' or c == '!' or c == '^':
            return True
        return False

    @staticmethod
    def is_special_sympole(c):
        if c == '(' or c == ')' or c == ',':
            return True
        return False

    def get_tokens(self):
        state=0
        current_ind=0
        pre_ind=0
        error=False

        while True:
            current_char= self.str_input[current_ind]
            if state == 0 :

                if self.is_special_sympole(current_char) :
                    self.tokens.append([current_char,self.token_type['S']])
                    current_ind+=1
                    pre_ind=current_ind
                elif  self.is_digit(current_char) or (len(self.tokens) > 0 and self.tokens[-1][1] != self.token_type["N"] and current_char == '-'):
                    state=7
                    current_ind+=1
                elif self.is_operator(current_char):
                    self.tokens.append([current_char,self.token_type['O']])
                    current_ind += 1
                    pre_ind = current_ind

                elif current_char == '>':
                    state=1
                    current_ind+=1
                elif current_char == '<':
                    state=4
                    current_ind+=1
                elif current_char == 'f':
                    l=len("factorial")
                    print(current_ind + l,len(self.str_input))
                    if( current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind+l] == "factorial"):
                        self.tokens.append(["factorial", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                    else:
                        return False
                elif current_char == 'g':
                    l = len("gcd")
                    if (current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind + l] == "gcd"):
                        self.tokens.append(["gcd", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                    else:
                        return False
                elif current_char == 'l':
                    l = len("lcm")
                    if (current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind + l] == "lcm"):
                        self.tokens.append(["lcm", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                    else:
                        return False
                elif current_char == 'c':
                    l = len("comp")
                    if (current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind + l] == "comp"):
                        self.tokens.append(["comp", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                    else:
                        return False

                elif current_char == 'p':
                    l = len("pow")
                    if (current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind + l] == "pow"):
                        self.tokens.append(["pow", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                        continue

                    l = len("perm")
                    if (current_ind + l < len(self.str_input) and self.str_input[current_ind:current_ind + l] == "perm"):
                        self.tokens.append(["perm", self.token_type['O']])
                        current_ind += l
                        pre_ind = current_ind
                    else:
                        return False

                elif current_char == ';':
                    break
                elif current_char == ' ':
                    current_ind+=1
                    continue
                else:
                    return False



            elif state == 1:
                if(current_char == '>' ):
                    state=2
                    current_ind+=1
                else:
                    return False
            elif state == 2:
                if(current_char == '>'):
                    state=3
                    current_ind += 1
                else :
                    state=0
                    self.tokens.append([self.str_input[pre_ind:current_ind],self.token_type['O']])
                    pre_ind=current_ind

            elif state == 3:
                state=0
                self.tokens.append([self.str_input[pre_ind:current_ind],self.token_type['O']])
                pre_ind = current_ind


            elif state == 4:
                if(current_char == '<' ):
                    state=5
                    current_ind+=1
                else:
                    return False

            elif state == 5:
                if(current_char == '<'):
                    state=6
                    current_ind += 1
                else :
                    state=0
                    self.tokens.append([self.str_input[pre_ind:current_ind],self.token_type['O']])
                    pre_ind=current_ind

            elif state == 6:
                state=0
                self.tokens.append([self.str_input[pre_ind:current_ind],self.token_type['O']])
                pre_ind = current_ind

            elif state == 7:
                if self.is_digit(current_char) :
                    current_ind+=1
                else:
                    state = 0
                    self.tokens.append([self.str_input[pre_ind:current_ind], self.token_type['N']])
                    pre_ind = current_ind

        return True
