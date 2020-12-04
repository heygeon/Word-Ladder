import streamlit as st
from collections import deque

class Solution(object):

    def ladderLength(self, begin, end, list):
        queue = deque()
        queue.append((begin, [begin]))

        while queue:
            st.sidebar.write("Current queue:", queue)
            node, path = queue.popleft()
            st.sidebar.write("Current transformation count:", len(path))
            for i in self.next_nodes(node, list) - set(path):
                if i == end:
                    st.sidebar.write("Found End Word at path:", path)
                    return len(path)
                else:
                    queue.append((i, path + [i]))
        return 0

    def next_nodes(self, word, word_list):
        possible_nodes = set()
        word_length = len(word)

        for words in word_list:
            wrong = 0
            for i in range(word_length):
                if words[i] != word[i]:
                    wrong += 1
            if wrong == 1:
                possible_nodes.add(words)

        st.sidebar.write("Possible next nodes:", possible_nodes)
        return possible_nodes

st.title("Word Ladder Solver")
st.write("by NG Chung Hei and Cheung Ka Shing")

st.sidebar.title("Progress:")
begin_word = st.text_input("Enter the begin word:")
end_word = st.text_input("Enter the end word:")
list = st.text_input("Enter the word list (separated with comma only):")
word__list = list.split(',')

if st.button("Run"):
    solution = Solution()
    result = solution.ladderLength(begin_word, end_word, word__list)
    st.write("Transformations needed:")
    st.write(result)

