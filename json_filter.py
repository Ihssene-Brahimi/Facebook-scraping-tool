import json


def filter_json(MyFile):

    with open(MyFile, 'r') as data_file:
        data = json.load(data_file)

    for element in data:                               #For loop to omit all the unwanted keys
        element.pop('original_request_url', None)
        #element.pop('post_url', None)
        element.pop('post_id', None)
        element.pop('text', None)
        element.pop('shared_text', None)
        element.pop('original_text', None)
        element.pop('time', None)
        element.pop('timestamp', None)
        element.pop('image', None)
        element.pop('image_lowquality', None)
        element.pop('images', None)
        element.pop('images_description', None)
        element.pop('images_lowquality', None)
        element.pop('images_lowquality_description', None)
        element.pop('video', None)
        element.pop('video_duration_seconds', None)
        element.pop('video_height', None)
        element.pop('video_id', None)
        element.pop('video_quality', None)
        element.pop('video_size_MB', None)
        element.pop('video_thumbnail', None)
        element.pop('video_watches', None)
        element.pop('video_width', None)
        element.pop('link', None)
        element.pop('links', None)
        element.pop('user_id', None)
        element.pop('user_url', None)
        element.pop('is_live', None)
        element.pop('factcheck', None)
        element.pop('shared_post_id', None)
        element.pop('shared_time', None)
        element.pop('shared_user_id', None)
        element.pop('shared_username', None)
        element.pop('shared_post_url', None)
        element.pop('available', None)
        element.pop('w3_fb_url', None)
        element.pop('with', None)
        element.pop('page_id', None)
        element.pop('sharers', None)
        element.pop('image_id', None)
        element.pop('image_ids', None)
        element.pop('was_live', None)
        element.pop('fetched_time', None)

    with open(MyFile, 'w') as data_file:
        data = json.dump(data, data_file,indent=4)



    #Creating a new file containing only posts "Posts_MyFile"

    with open(MyFile, 'r') as data_file:
        data = json.load(data_file)

    for element in data:                               #For loop to omit all the unwanted keys
        element.pop('comments_full', None)

    with open("Posts_"+ MyFile, 'w') as data_file:
        data = json.dump(data, data_file,indent=4)

    #Creating a new file containing only Comments "Comments_MyFile"

    with open(MyFile, 'r') as data_file:
        data = json.load(data_file)

    for element in data:                               #For loop to omit all the unwanted keys
        element.pop('post_text', None)
        element.pop('likes', None)
        element.pop('comments', None)
        element.pop('shares', None)
        element.pop('username', None)
        element.pop('reactors', None)
        element.pop('reactions', None)
        element.pop('reaction_count', None)

    with open("Comments_"+ MyFile, 'w') as data_file:
        data = json.dump(data, data_file,indent=4)

    #Creating a new file containing only replies "Replies_MyFile"

    with open(MyFile, 'r') as data_file:
        data = json.load(data_file)

    for element in data:                               #For loop to omit all the unwanted keys
        element.pop('post_text', None)
        element.pop('likes', None)
        element.pop('comments', None)
        element.pop('shares', None)
        element.pop('username', None)
        element.pop('reactors', None)
        element.pop('reactions', None)
        element.pop('reaction_count', None)
        for dictionary in element['comments_full']:
            dictionary.pop('comment_id', None)
            dictionary.pop('comment_url', None)
            dictionary.pop('commenter_id', None)
            dictionary.pop('commenter_url', None)
            dictionary.pop('commenter_name', None)
            dictionary.pop('commenter_meta', None)
            dictionary.pop('comment_text', None)
            dictionary.pop('comment_time', None)
            dictionary.pop('comment_image', None)
            dictionary.pop('comment_reactors', None)
            dictionary.pop('comment_reactions', None)
            dictionary.pop('comment_reaction_count', None)

    with open("Replies_"+ MyFile, 'w') as data_file:
        data = json.dump(data, data_file,indent=4)