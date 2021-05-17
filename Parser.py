

class Parser :
    def __init__(self,tokens):
        self.tokens=tokens
        self.tokens_ind=0
        self.token_type = {'S': "special_sympole", 'O': "operator", "N": "number"}
        self.tokens_len=len(tokens)
        self.error=False

    def match(self,c):
        if self.tokens_ind >= self.tokens_len or  c != self.tokens[self.tokens_ind][0] :
            self.error=True
            return  False
        self.tokens_ind+=1
        return True

    def compute_exp(self):
        self.error = False
        ans=self.exp()
        if(self.error == True):
            return False
        return  ans

    def exp(self):
        temp = self.term()
        while (self.tokens_ind < self.tokens_len and(self.tokens[self.tokens_ind][0] == '-' or self.tokens[self.tokens_ind][0] == '+')):
            if self.tokens[self.tokens_ind][0] == '+':
                self.match('+')
                temp = temp + self.factor()
            elif self.tokens[self.tokens_ind][0] == '-':
                self.match('-')
                temp = temp - self.factor()
        return temp

    def term(self):
        temp=self.factor()
        while(self.tokens_ind < self.tokens_len and ( self.tokens[self.tokens_ind][0] == '*'or self.tokens[self.tokens_ind][0]== '/')):
            if self.tokens[self.tokens_ind][0] == '*':
                self.match('*')
                temp=temp * self.factor()
            elif self.tokens[self.tokens_ind][0] == '/':
                self.match('/')
                temp = temp / self.factor()
        return temp

    def factor(self):
        if(self.tokens_ind < self.tokens_len and self.tokens[self.tokens_ind][0] == '('):
            self.match('(')
            temp=self.exp()
            self.match(')')
            return temp
        elif self.tokens[self.tokens_ind][1] == self.token_type['N']:
            self.tokens_ind+=1
            return int(self.tokens[self.tokens_ind-1][0])
        else:
            self.error=True
            return False
