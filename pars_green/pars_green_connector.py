from zeep import Client


class ParsGreenSmsServiceClient(object):
    SEND_SMS_URL = 'http://login.parsgreen.com/Api/SendSMS.asmx?WSDL'
    PROFILE_SERVICE_URL = 'http://login.parsgreen.com/Api/profileservice.asmx?WSDL'
    MSG_SERVICE_URL = 'http://login.parsgreen.com/Api/MsgService.asmx?WSDL'
    SCHEDULE_SERVICE_URL = 'http://login.parsgreen.com/Api/ScheduleService.asmx?WSDL'

    def __init__(self, signature):
        """
        :param signature:
        """
        self._sms_client = None
        self._profile_client = None
        self._schedule_client = None

        self.signature = signature
        self.udh = ""
        self.success = 0x0
        self.retStr = []

    @property
    def sms_client(self):
        if not self._sms_client:
            self._sms_client = Client(self.SEND_SMS_URL)
        return self._sms_client

    @property
    def profile_client(self):
        if not self._profile_client:
            self._profile_client = Client(self.PROFILE_SERVICE_URL)
        return self._profile_client

    @property
    def schedule_client(self):
        if not self._schedule_client:
            self._schedule_client = Client(self.SCHEDULE_SERVICE_URL)
        return self._schedule_client

    def get_send_sms_client(self):
        """
        Get sms client data
        :return:
        """
        return self.sms_client

    def get_profile_client(self):
        """
        Get profile client
        :return:
        """
        return self.profile_client

    # Sending text messages method
    def send(self, from_number, to, text, is_flash=False):
        """
        Sending SMS
        :param from_number:
        :param to:
        :param text:
        :param is_flash:
        :return:
        """
        array_of_string = self.schedule_client.get_type('ns0:ArrayOfString')
        str_arr = array_of_string(to if isinstance(to, (tuple, list)) else [to])
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
        Get delivery data
        :param rec_id:
        :return:
        """
        return self.sms_client.service.GetDelivery(self.signature, rec_id)

    # Get number of received text messages
    def get_message_count(self, location, is_read):
        """
        Get message count
        :param location:
        :param is_read:
        :return:
        """
        return self.sms_client.service.GetMsgCount(self.signature, location, is_read)

    # Delete either received or sent text messages
    def delete_message(self, encrypted_message_id):
        """
        Delete message from Pars Green account
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
        array_of_string = self.schedule_client.get_type('ns0:ArrayOfString')
        str_arr = array_of_string(to if isinstance(to, (tuple, list)) else [to])
        return self.schedule_client.service.RegSchdeuleDaily(self.signature, hour, minute, text, str_arr, from_number,
                                                             encrypted_schedule_id)

    def register_schedule_yearly(self, month_of_year, day_of_month, hour, minute, text, to, from_number,
                                 encrypted_schedule_id):
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
        array_of_string = self.schedule_client.get_type('ns0:ArrayOfString')
        str_arr = array_of_string(to if isinstance(to, (tuple, list)) else [to])
        return self.schedule_client.service.RegSchdeuleYearly(self.signature, month_of_year, day_of_month, hour, minute,
                                                              text, str_arr, from_number, encrypted_schedule_id)

    def delete_schedule(self, encrypted_schedule_id):
        """
        :param encrypted_schedule_id:
        :return:
        """
        return self.schedule_client.service.DeleteSchedule(self.signature, encrypted_schedule_id)