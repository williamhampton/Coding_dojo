# this is an edge graph exercise  a=>e is one
# (first number is start second is where its being pointed too)
# [a, b][ a,h][b,e][b,d][h,g][h,f][g,h][g,f][f,e][c,d][d,e]


class edge:
    def __init__(self, data):
        self.data = data;
        self.children = {}
    def add(self,parent,child):
        if self.data != parent and self.children != {}:
            for child in self.children:
                self.children[child].add(parent,child)
        if self.data == parent:
            self.children[child] = edge(child)
        if self.data != parent and self.children == {}:
            return False;


    def babies(self,parent):
        chil = []
        if self.data == parent:
            for child in self.children:
                chil.append(self.children[child].data);
            arr = ["parent: {}".format(self.data), 'children: {}'.format(chil)]
            print arr
            return arr
        if self.data != parent and self.children != {}:
            for child in self.children:
                self.children[child].babies(parent)

test = edge('a');
test.add('a','b');
test.add('a','h')
test.add('b', 'e');
test.add('b', 'd');
test.babies('b')
