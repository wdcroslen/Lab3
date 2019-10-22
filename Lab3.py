red = "red"
black = "black"
count = 0
#Lab3 William Croslen
class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.height = 0
        self.left = None
        self.right = None
        self.color = red
################### RedBlackTree Class ####################
class RedBlackTree:
    def __init__(self, root = None, height = -1):
        self.root = root
        
    def RBTreeSetChild(self, parent, whichChild, child):
       if (whichChild != "left" and whichChild != "right"):
          return False
       if (whichChild == "left"):
          parent.left = child
       else:
          parent.right = child
       if (child != None):
          child.parent = parent
       return True

    def RBTreeReplaceChild(self, parent, currentChild, newChild):
       if (parent.left == currentChild):
          return self.RBTreeSetChild(parent, "left", newChild)
       elif (parent.right == currentChild):
          return self.RBTreeSetChild(parent, "right", newChild)
       return False
    
    def rbt_rotate_left(self, node):
       rightLeftChild = node.right.left
       if (node.parent != None):
          self.RBTreeReplaceChild(node.parent, node, node.right)
       else: # node is root
          self.root = node.right
          self.root.parent = None
       
       self.RBTreeSetChild(node.right, "left", node)
       self.RBTreeSetChild(node, "right", rightLeftChild)
    
    def rbt_rotate_right(self, node):
       leftRightChild = node.left.right
       if (node.parent != None):
          self.RBTreeReplaceChild(node.parent, node, node.left)
       else: # node is root
          self.root = node.left
          self.root.parent = None
       
       self.RBTreeSetChild(node.left, "right", node)
       self.RBTreeSetChild(node, "left", leftRightChild)

    def rbt_insert(self, data): #insert data into rbt
       node = Node(data)
       self._bst_insert(node)
       node.color = red
       self.rbt_balance(node)
    
    def _bst_insert(self, node): #helper for rbt
        if (self.root == None):
          self.root = node
          node.parent = None
          return
        cur = self.root
        while (cur != None):
          if (node.data < cur.data):
             if (cur.left == None):
                cur.left = node
                node.parent = cur
                cur = None
             else:
                cur = cur.left
          else:
             if (cur.right == None):
                cur.right = node
                node.parent = cur
                cur = None
             else:
                cur = cur.right
        
    def RBTreeGetGrandparent(self, node):
       if (node.parent == None):
          return None
       return node.parent.parent
    
    def RBTreeGetUncle(self, node):
       grandparent = None
       if (node.parent != None):
          grandparent = node.parent.parent
       if (grandparent == None):
          return None
       if (grandparent.left == node.parent):
          return grandparent.right
       else:
          return grandparent.left
    
    def rbt_balance(self, node): #rebalances after insertion
      if (node.parent == None):
         node.color = black
         return
      
      if (node.parent.color == black):
         return
        
      parent = node.parent
      grandparent = self.RBTreeGetGrandparent(node)
      uncle = self.RBTreeGetUncle(node)
    
      if (uncle != None and uncle.color == red):
         parent.color = uncle.color = black
         grandparent.color = red
         self.rbt_balance(grandparent)
         return
      
      if (node == parent.right and
          parent == grandparent.left):
         self.rbt_rotate_left(parent)
         node = parent
         parent = node.parent
      
      elif (node == parent.left and
               parent == grandparent.right):
         self.rbt_rotate_right(parent)
         node = parent
         parent = node.parent
      
      parent.color = black
      grandparent.color = red
      if (node == parent.left):
         self.rbt_rotate_right(grandparent)
      else:
         self.rbt_rotate_left(grandparent)
            
    def printTree(self, node):
        if node is None:
            return
        print(node.data, node.color)
        self.printTree(node.left)
        self.printTree(node.right)
        return

    def rbt_search(self,data,cur):
        if not cur:
            return 0
        if cur.data == data:
            return 1
        if data < cur.data:
            return self.rbt_search(data,cur.left)
        if data > cur.data:
            return self.rbt_search(data,cur.right)
        return 0    
#################### AVL CLASS ##########################
class AVLTree:
    def __init__(self, root=None, height=-1):
        self.root = root
        
    def avl_rotate_right(self, node):
       leftRightChild = node.left.right
       if (node.parent != None):
          self.avl_replace_child(node.parent, node, node.left)
       else: # node is root
          self.root = node.left
          self.root.parent = None
       
       self.avl_set_child(node.left, "right", node)
       self.avl_set_child(node, "left", leftRightChild)
    
    def avl_rotate_left(self, node):
       rightLeftChild = node.right.left
       if (node.parent != None):
          self.avl_replace_child(node.parent, node, node.right)
       else: # node is root
          self.root = node.right
          self.root.parent = None
       
       self.avl_set_child(node.right, "left", node)
       self.avl_set_child(node, "right", rightLeftChild)

    def avl_update_height(self,node):
       leftHeight = -1
       if (node.left != None):
          leftHeight = node.left.height
       rightHeight = -1
       if (node.right != None):
          rightHeight = node.right.height
       node.height = max(leftHeight, rightHeight) + 1

    def avl_set_child(self,parent, whichChild, child): 
       if (whichChild != "left" and whichChild != "right"):
          return False
       if (whichChild == "left"):
          parent.left = child
       else:
          parent.right = child
       if (child != None):
          child.parent = parent
            
       self.avl_update_height(parent)
       return True

    def avl_replace_child(self, parent, currentChild, newChild):
       if (parent.left == currentChild):
          return self.avl_set_child(parent, "left", newChild)
       elif (parent.right == currentChild):
          return self.avl_set_child(parent, "right", newChild)
       return False

    def avl_get_balance(self,node):
       leftHeight = -1
       if (node.left != None):
          leftHeight = node.left.height
       rightHeight = -1
       if (node.right != None):
          rightHeight = node.right.height
       return leftHeight - rightHeight

    def avl_rebalance(self, node):
       self.avl_update_height(node)        
       if (self.avl_get_balance(node) == -2):
          if (self.avl_get_balance(node.right) == 1):
             # Double rotation case.
             self.avl_rotate_right(node.right)
          
          return self.avl_rotate_left(node)
       
       elif (self.avl_get_balance(node) == 2):
          if (self.avl_get_balance(node.left) == -1):
             # Double rotation case.
             self.avl_rotate_left(node.left)
          
          return self.avl_rotate_right(node)
               
       return node
    #########INSERT################
    def avl_insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            self._avl_insert(new_node)
    ###############################
    def _avl_insert(self, node): #insert helper
       if (self.root == None):
          self.root = node
          node.parent = None
          return
       cur = self.root
       while (cur != None):
          if (node.data < cur.data):
             if (cur.left == None):
                cur.left = node
                node.parent = cur
                cur = None
             else:
                cur = cur.left
          else:
             if (cur.right == None):
                cur.right = node
                node.parent = cur
                cur = None
             else:
                cur = cur.right
       node = node.parent
       while (node != None):
          self.avl_rebalance(node)
          node = node.parent
                 
    def avl_search(self,data,cur):
        if not cur:
            return 0
        if cur.data == data:
            return 1
        if data < cur.data:
            return self.avl_search(data,cur.left)
        if data > cur.data:
            return self.avl_search(data,cur.right)
        return 0    

    def printTree(self, node): #avlPrintTree
        if node is None:
            return
        print(node.data)
        self.printTree(node.left)
        self.printTree(node.right)
        return

################################################# 
################################################# 
def print_anagrams_rbt(word,english_words,prefix = ""):
    if len(word) <= 1:
       str = prefix + word
       if english_words.rbt_search(prefix + word,english_words.root):
           print(prefix + word)
    else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur
           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams_rbt(before + after,english_words, prefix + cur) 
    return count

def print_anagrams_avl(word,english_words,prefix = ""):
    arr = []
    num = 0
    if len(word) <= 1:
       str = prefix + word
       if english_words.avl_search(prefix + word,english_words.root):
           print(prefix + word)
           arr.append(prefix + word)
    else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur
           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams_avl(before + after,english_words, prefix + cur) 
    return num + len(arr)

def avl_readfile():
    file = open("test.txt", "r")
    singleLine = file.readline() #reads a single line at a time
    avl = AVLTree()
    for singleLine in file:
        #Inserts each line in avl
        avl.avl_insert(singleLine.replace("\n",""))
    return avl
        
def rbt_readfile():
    file = open("test.txt", "r")
    singleLine = file.readline() #reads a single line at a time
    rbt = RedBlackTree()
    for singleLine in file:
        #Inserts each line in rbt
        rbt.rbt_insert(singleLine.replace("\n",""))
    return rbt

def count_anagrams_avl(word,english_words,prefix = ""):
    global count # calls global count to count recursively
    if len(word) <= 1:
       str = prefix + word
       if english_words.avl_search(prefix + word,english_words.root):
           count = count + 1
    else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur
           if cur not in before: # Check if permutations of cur have not been generated.
               count_anagrams_avl(before + after, english_words, prefix + cur) 
    return count

def most_anagrams_avl(english_words): # finds word with most anagrams in the file
    file = open("test.txt", "r")
    biggest = 0
    word = ""
    global count
    count = 0
    for singleLine in file:
        #Inserts each line in avl
        a = str(singleLine.replace("\n",""))
        q = count_anagrams_avl(a,english_words)
        if  q > biggest:
            word = a
            biggest = q
        global count
        count = 0
    print(word, biggest)
    return 0

def main():
     print("Hello! I will be producing anagrams for you using a list of english words.")
     print("How do you want the words to be stored?")
     print("Either \"AVL\" or \"RBT\"")
     a = raw_input()
     print(a)
        
    #AVL
     if (a == "AVL" or a == "avl"):
        print("What word would you like to use?")
        user_word = raw_input()
        print("______AVL_____")
        english_words = avl_readfile()
        english_words.printTree(english_words.root)
        print("")
        print("ANAGRAMS for " + user_word + ": ")
        print(count_anagrams_avl(user_word,english_words))
        print_anagrams_avl(user_word,english_words)
     #RBT
     elif (a == "RBT" or a == "rbt"):
        print("What word would you like to use?")
        user_word = raw_input()
        print("______RBT_____")
        engish_words = rbt_readfile()
        engish_words.printTree(engish_words.root)
        print("")
        print("ANAGRAMS for " + user_word + ": ")
        print_anagrams_rbt(user_word,engish_words)
     #MostAnagrams
     else:
        print("That is not a proper input. Would you like to see the word with the most anagrams?.(yes or no) ")
        b = raw_input()
        if b == "yes":
            english_words = avl_readfile()
            print("")
            print("The word with the most anagrams is: ")
            most_anagrams_avl(english_words)
        else:
            print("ok, goodbye")
    
main()
