class StatsAlerter:
    """ class contains function check and alert """
    def __init__(self, max_threshold, alerts):
        self.max_threshold = max_threshold
        self.email_alert = alerts[0]
        self.led_alert = alerts[1]

    def checkAndAlert(self, numbers):
        """ function that will alert if max of numbers is above threshold """
        maximum = max(numbers)
        if maximum > self.max_threshold:
            self.email_alert.emailSent = True
            self.led_alert.ledGlows = True