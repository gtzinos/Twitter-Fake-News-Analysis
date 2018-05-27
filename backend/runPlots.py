from config.credentials import  *
from twitter.login import *
from twitter.owner import *
import networkx as nx
import matplotlib.pyplot as plt

def runNetworkGraph():
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
    G = nx.Graph()

    for follower in followers:
        G.add_edge(follower['source']['user']['id'], follower['target']['user']['id'], length = follower['hop_number'])

    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()

runNetworkGraph()
