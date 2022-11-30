# import pygal library
import pygal

# create a world map
worldMap = pygal.maps.world.World()

# set the title of the map
worldMap.title = 'Countries'

# adding the countries 
worldMap.add('Random Data',{

    'aq': 10,
    'cd': 30,
    'de': 40,
    'eg': 50,
    'ga': 45,
    'hk': 23,
    'in': 70,
    'jp': 54,
    'nz': 41,
    'kz': 32,
    'us': 66
})

# save into the file
worldMap.render_to_file('abc.svg')

print('Success')