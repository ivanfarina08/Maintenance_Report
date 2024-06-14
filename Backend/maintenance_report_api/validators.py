"""Report"""
def report_title(user_title):
    return len(user_title) > 3 and len(user_title) < 50
def report_description(user_description):
    return len(user_description) < 200
def report_time_spend(user_time_spend):
    return len(user_time_spend) <= 2

"""Executor"""
def executor_name(user_name):
    return len(user_name) > 3 and len(user_name) < 50

"""Line"""
def line_name(user_name):
    return len(user_name) > 3 and len(user_name) < 50

"""Machine"""
def machine_name(user_name):
    return len(user_name) > 3 and len(user_name) < 50



