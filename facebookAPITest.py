import facebook

token='EAABZCrQb9tfwBAEnU1L5Ficq8QjHbmUaGCRXFAqCnLaiKKsYlqvLqChWyW9flss4qyJQpqT540dZCwRZBsWBok7YFVDoQsEoPLBjUkouyUZClquwgO8H4ZCfgg5PYKTBl8xKqmHNWT3FhxzvGCrkmqaOwRBXAIiLiUqVsA8ffjhi5DyerM03i2CknKBDkxrYZD'

graph=facebook.GraphAPI(token)
profile=graph.get_object('me')
friend_list=graph.get_object('me/friendlists')
friends=graph.get_connections('me','friends')



#friend_list=[friend['name'] for friend in friends['data']]
