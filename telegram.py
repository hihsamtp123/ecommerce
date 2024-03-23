import pyrogram


client - pyrogram.client("my_account")

clientr.start()


chat_id = 5082350285
message_limit = 10

counter = 0
while counter <message_limt:

    client.send_message(chat_id,"Hello,this is an automated message")
    counter += 1

    client.stop()