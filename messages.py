# main_body = '''
# Congratulations on becoming a member of Delhi Public School Ruby Park's Tech Club! Your passion for technology and dedication to exploring its vast possibilities have brought you here. We're excited to have you on board, and we can't wait to see the amazing contributions you'll bring to our community. Get ready to embark on an incredible journey of innovation and growth. Let's dive into coding, robotics, development, and much more. 

# Click the adjoining link(s) to join us and begin your electrifying journey with the club.

# *Your Department:*
# '''

# robo_message = "*Robotics*\nJoin the Robotics Group: https://chat.whatsapp.com/CUJa9PLxB6AETNiQCYTLrT\n"
# cp_message = "*Competitive Programming*\nJoin the Competitive Programming Group: https://chat.whatsapp.com/I0af6PO2uI0Jf806vfkVLm\n"     
# dev_message = "*Development*\nJoin the Development Group: https://chat.whatsapp.com/DKU5w4VwWVQ2xy3DCnqtQa\n" 

disc_message = 'lol'

def message_builder(name:str) -> str:
    message=''
    message += f"Greetings {name},\n{disc_message}"
    print(name, message)
    return message