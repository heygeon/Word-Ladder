import streamlit as st
from collections import deque


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        queue = deque()
        queue.append((beginWord, [beginWord]))

        while queue:

            st.sidebar.write("Current queue:", queue)

            node, path = queue.popleft()

            st.sidebar.write("Current transformation count:",
                  len(path))

            for i in self.next_nodes(node, wordList) - set(path):
                if i == endWord:
                    st.sidebar.write("Found End Word at path:",
                          path)
                    return len(path)
                else:
                    queue.append((i, path + [i]))
        return 0

    def next_nodes(self, word, word_list):

        possible_nodes = set()

        wl_word_length = len(word)

        for wl_word in word_list:
            mismatch_count = 0

            for i in range(wl_word_length):
                if wl_word[i] != word[i]:
                    mismatch_count += 1
            if mismatch_count == 1:

                possible_nodes.add(wl_word)

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

