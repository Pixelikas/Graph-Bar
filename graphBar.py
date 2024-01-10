import matplotlib.pyplot as plt

games = ['Zelda', 'Pokemon', 'The Last Of Us', 'God of War']
sell = [15, 19, 22, 10]
colors = ['#AC8DCA', 'yellow', 'blue', 'red']

plt.title('Venda Franquias Jogos', loc='left')

plt.xlabel("Jogos")
plt.ylabel("Quantidade")

plt.bar(games, sell, color = colors)

plt.show()