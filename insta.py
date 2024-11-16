from instabot import Bot
bot = Bot()
bot.login(username="raginee_darade", password="******")
# bot.unfollow('raginee_darade')
# bot.block('suman_34')
# bot.upload_photo(
#     "C:/Users/ASUS/Downloads/images of khandwa/dadagi.jpg", caption="i love this")
# bot.send_messages(" i love you", ["raginee_darade", "what_a_writter"])
followers = bot.get_user_followers("raginee_darade")
for follower in followers:
    print(bot.get_user_info(follower))
