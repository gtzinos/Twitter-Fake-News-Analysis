from networkx import Graph

from config.credentials import  *
from twitter.login import *
from twitter.owner import *
import matplotlib.pyplot as plt

# Open connection
db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)

# Login user
auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)
# Owner login
loggedInUser = getUser(username, auth_api)

#Get followers
followersModel = Followers(followers_table_name)
followers = followersModel.get_my_followers(db, loggedInUser.id)

#Create Graph
G = Graph()

edgesArray = []
for follower in followers:
    edgesArray.append((follower['source']['user']['id'], follower['target']['user']['id']))

G.add_edges_from(edgesArray)

#Draw plot
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()