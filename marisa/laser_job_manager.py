import time
from google_form_submission import submit_form


def seconds_to_hms(seconds=0):
    t = time.gmtime(seconds)
    h = t.tm_hour
    m = t.tm_min
    s = t.tm_sec
    return (h, m, s)


class LaserJobManager(object):

    _form_id = '128sPBtZ2DaWH1pTyH9y5_a7jR1FLeXdlS5fCz1KXReE'
    _field_name = 'entry.594634135'
    _field_desc = 'entry.134285113'
    _field_h = 'entry.1057491295_hour'
    _field_m = 'entry.1057491295_minute'
    _field_s = 'entry.1057491295_second'

    def __init__(self, user):
        self._user = user


    def submit_job(self, duration=0, description=None):
        """
        Submits a job as the current user.

        @param duration Job duration in seconds
        @param description Optional job description
        @returns True on success
        """
        t = seconds_to_hms(duration)

        responses = {
            self._field_name: self._user,
            self._field_h: t[0],
            self._field_m: t[1],
            self._field_s: t[2]
        }

        if description is not None:
            responses[self._field_desc] = description

        return submit_form(self._form_id, responses)


    def query_my_time(self):
        """
        Returns the time in seconds remaining for the current user.

        @return Remaining time in seconds
        """
        #TODO: query stuff
        raise NotImplementedError("nope.avi");


    def get_my_jobs(self):
        """
        Gets a list of all jobs (as tuple) for current user.

        @return Current users jobs
        """
        #TODO: query stuff
        raise NotImplementedError("nope.avi");


    def get_all_jobs(self):
        """
        Gets a list of all jobs (as tuple) for all users.

        @return All users jobs
        """
        #TODO: query stuff
        raise NotImplementedError("nope.avi");
