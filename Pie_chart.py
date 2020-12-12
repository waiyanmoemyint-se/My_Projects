#pie chart
from matplotlib import pyplot
citizes = ['Yangon','Mandalay','Bago','Shan State']
slices  = [19,20,20,36]
colors  = ['c','r','b','y']

pyplot.pie(
    slices,
    labels=citizes,
    colors=colors,
    startangle=90,
    shadow=True,
    explode = (0,0.1,0,0),
    autopct = "%1.2f%%"

)
pyplot.title("Sales in the Different Colors")
pyplot.show()
