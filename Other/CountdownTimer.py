# Author: Shreyan Gupta
# Date Started: 02/06/2023
# Date Completed: 02/08/2023

import time as timeLib


# Countdown Timer Function
def pyTime(i_time):
    m_minutes = i_time // 60
    m_seconds = i_time % 60
    m_curTime = getCurTime()
    m_finalTime = m_curTime + i_time
    mw_curTime = 0
    while mw_curTime != m_finalTime:
        mw_curTime = getCurTime()
        mw_startTime = mw_curTime % m_curTime
        m_reverseTime = m_seconds - mw_startTime
        if m_reverseTime == -1:
            m_seconds += 60

            if m_minutes > 0:
                m_minutes -= 1

        print(f"Time Left: {m_minutes:02d}:{m_reverseTime:02d}", end="\r")

    print("\nDone Bitch!")


# Get Current Time
def getCurTime():
    m_curTime = int(timeLib.time())
    return m_curTime


# Convert Input to Seconds
def secondConv(is_time):
    m_colonCount = is_time.find(":")
    m_stringLength = len(is_time)

    if m_colonCount == 2 and m_stringLength == 8:
        m_hours = int(is_time[0:2])
        m_minutes = int(is_time[3:5])
        m_seconds = int(is_time[6:8])

        m_timeInSeconds = (m_hours * 3600) + (m_minutes * 60) + m_seconds
        return m_timeInSeconds
    elif m_colonCount == 2 and m_stringLength == 5:
        m_minutes = int(is_time[0:2])
        m_seconds = int(is_time[3:5])

        m_timeInSeconds = (m_minutes * 60) + m_seconds
        return m_timeInSeconds
    elif m_colonCount == -1:
        return int(is_time)
    else:
        return -1


if __name__ == "__main__":
    m_retryCount = 0

    while m_retryCount != 5:
        is_time = input(
            "Enter the timer count in one of the following formats:\n - hh:mm:ss\n - mm:ss\n - seconds\n Timer Count: "
        )
        try:
            i_timeInSeconds = secondConv(is_time)

            if secondConv(is_time) != -1:
                pyTime(i_timeInSeconds)
            else:
                m_retryCount += 1
                print("Invalid Input, Please Try Again.\n")
        except ValueError:
            m_retryCount += 1
            print("Invalid Input, Please Try Again.\n")

    print("Too Many Retries, Please Try Again Later.")
