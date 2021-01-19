from datetime import datetime

IOTD_SUBMISSION_WINDOW_DAYS = 1
IOTD_SUBMISSION_MAX_PER_DAY = 3
IOTD_SUBMISSION_MIN_PROMOTIONS = 3

IOTD_REVIEW_WINDOW_DAYS = 5
IOTD_REVIEW_MAX_PER_DAY = 3
IOTD_REVIEW_MIN_PROMOTIONS = 3

IOTD_JUDGEMENT_WINDOW_DAYS = 7
IOTD_JUDGEMENT_MAX_PER_DAY = 1
IOTD_JUDGEMENT_MAX_FUTURE_DAYS = 7
IOTD_JUDGEMENT_MAX_FUTURE_PER_JUDGE = 2

IOTD_SHOW_CHOOSING_JUDGE = False

IOTD_DESIGNATED_SUBMITTERS_PERCENTAGE = 20
IOTD_DESIGNATED_REVIEWERS_PERCENTAGE = 20

IOTD_QUEUES_PAGE_SIZE = 10
IOTD_MULTIPLE_PROMOTIONS_REQUIREMENT_START = datetime(2021, 1, 20)
