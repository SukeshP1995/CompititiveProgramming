import unittest


class Trie(object):
        
    c = 0
    def __init__(self):
        self.path = {}
        self.value_valid = False

    def add_word(self, key):
        if len(key) == 0:
            node = Trie()
            if key in self.path:
                return False
            else:
                node = Trie()
                node.value_valid = True
                self.path[key] = node
                return True
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            return node.add_word(remains)
        else:
            if node.value_valid:
                return False
            else:
                self.path[head].value_valid = True
                return True  
            


















# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)