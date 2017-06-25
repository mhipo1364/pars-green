from suds.client import Client


class ParsGreenSmsServiceClient(object):
    sendSmsURL = 'http://login.parsgreen.com/Api/SendSMS.asmx?WSDL'
    profileServiceURL = 'http://login.parsgreen.com/Api/profileservice.asmx?WSDL'
    msgServiceURL = 'http://login.parsgreen.com/Api/MsgService.asmx?WSDL'
    scheduleServiceURL = 'http://login.parsgreen.com/Api/ScheduleService.asmx?WSDL'

    def __init__(self, signature):
        self.sms_client = Client(self.sendSmsURL)
        self.profile_client = Client(self.profileServiceURL)
        # on creating msg service client program crash
        self.scheduleClient = Client(self.scheduleServiceURL)

        self.signature = signature
        self.udh = ""
        self.success = 0x0
        self.retStr = []

    def get_send_sms_client(self):
        return self.sms_client

    def get_profile_client(self):
        return self.profile_client

    # Sending text messages method
    def send(self, from_number, to, text, is_flash=False):
        str_arr = self.sms_client.factory.create('ArrayOfString')
        str_arr.string = to
        self.retStr = self.sms_client.service.SendGroupSMS(
            self.signature,
            from_number,
            str_arr,
            text,
            is_flash,
            self.udh,
            self.success,
            self.retStr
        )
        return self.retStr

    # Get delivery method
    def get_delivery(self, rec_id):
        """

        :param rec_id:
        :return:
        """
        return self.sms_client.service.GetDelivery(self.signature, rec_id)

    # Get number of received text messages
    def get_message_count(self, location, is_read):
        """

        :param location:
        :param is_read:
        :return:
        """
        return self.sms_client.service.GetMsgCount(self.signature, location, is_read)

    # Delete either received or sent text messages
    def delete_message(self, encrypted_message_id):
        """

        :param encrypted_message_id:
        :return:
        """
        return self.sms_client.service.MsgDelete(self.signature, encrypted_message_id)

    # Change text message as unread/read
    def get_message_change_is_read(self, location, is_read):
        """

        :param location:
        :param is_read:
        :return:
        """
        return self.sms_client.service.MsgChangeIsRead(self.signature, location, is_read)

    # Get either received or sent text messages
    def get_message(self, location, is_read):
        """

        :param location:
        :param is_read:
        :return:
        """
        return self.sms_client.service.GetMessage(self.signature, location, is_read)

    # Get credit amount left in your account
    def get_credit(self):
        """

        :return:
        """
        return self.profile_client.service.GetCredit(self.signature)

    # For transfer credit between from one account to another
    def transfer_credit(self, to_username, to_password, amount):
        """

        :param to_username:
        :param to_password:
        :param amount:
        :return:
        """
        return self.profile_client.service.TransferCredit(self.signature, to_username, to_password, amount)

    def register_schedule_daily(self, hour, minute, text, to, from_number, encrypted_schedule_id):
        """

        :param hour:
        :param minute:
        :param text:
        :param to:
        :param from_number:
        :param encrypted_schedule_id:
        :return:
        """
        str_arr = self.scheduleClient.factory.create('ArrayOfString')
        str_arr.string = to
        return self.scheduleClient.service.RegSchdeuleDaily(self.signature, hour, minute, text, str_arr, from_number,
                                                            encrypted_schedule_id)

    def register_schedule_yearly(self, month_of_year, day_of_month, hour, minute, text, to, from_number, encrypted_schedule_id):
        """

        :param month_of_year: In Jalali Calendar
        :param day_of_month: In Jalali Calendar
        :param hour:
        :param minute:
        :param text:
        :param to:
        :param from_number:
        :param encrypted_schedule_id:
        :return:
        """
        str_arr = self.scheduleClient.factory.create('ArrayOfString')
        str_arr.string = to
        return self.scheduleClient.service.RegSchdeuleYearly(self.signature, month_of_year, day_of_month, hour, minute,
                                                             text, str_arr, from_number, encrypted_schedule_id)

    def delete_schedule(self, encrypted_schedule_id):
        return self.scheduleClient.service.DeleteSchedule(self.signature, encrypted_schedule_id)
