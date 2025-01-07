def get_topic_id(bot_object, user_id, forum_id):
    topics = bot_object.get_forum_topic_list(forum_id)

    for topic in topics.topics:
        if topic.name.startswith(str(user_id)):
            details = bot_object.get_forum_topic_details(forum_id, topic.topic_id)
            return details.topic_id, True
    else:
        return None, False
