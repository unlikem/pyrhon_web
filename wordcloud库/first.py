import wordcloud
c = wordcloud.WordCloud()
c.generate("WordCloud By Python")
c.to_file("first.png")