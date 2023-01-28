from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 1593178008
bot_user = "f_64bot"
api_id = 13296661
api_hash = "44d7de0b99917321d0db5d1572623208"
session = "BADK5BUAwjkR1NqjXYSgESwpVmpWybBJXfLfryFtZAwkQ5UJ_8IBjDQnFUvYwq6Gaj1E6qwd6l02xdwyNAa2h94Aj7OKs7xjCdie_9YQlyiIaLuJFHUoZlUHWkeioUJmJb1gUr4dI9sAk0DffjRdOXbNe2e1QSIWgh8xcLRupr3y9gRwwDW3U8ObPDT8sGFJcTXUx5cMgYfy9ls6eFQU7f0BeXt2j7IXuUPiGyMRo-EkCYeUZD05RXq_3qGjqz8QUGJ_z-wP4DwAkXsZw7DBmJaCo3otMYi1z32D1RytyLaP2zpfrZOi06rDwTC7oWy_O3tAhqnJqRwUCOpnwZZkEcMRu1FWfQAAAABe9feYAA"
token = "5093364753:AAFuUPp0qK6WAvK622ku6TIe19M6o264iOg"
pm = "-1001762627348"
mention = "-1001698764129"
plugins = dict(root="plugins")
app = Client("user:bot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("bot_id",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))