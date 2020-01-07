from mycroft import MycroftSkill, intent_file_handler


class HomeSensorCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.sensor.home.intent')
    def handle_check_sensor_home(self, message):
        self.speak_dialog('check.sensor.home')


def create_skill():
    return HomeSensorCheck()

