import json
import urllib.request
from benion_tech_django.settings import env
from user_app.models import ExamScore

base_url = env('BASE_URL')
production = env('PRODUCTION') == 'True'
data = [
    {
        "className": "sss-1",
        "comment": "Very Good",
        "exam": 56,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Chidiebube Ikechukwu",
        "grade": "A",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "physics",
        "term": "third-term",
        "total": 77,
        "username": "2022/SDT/62502",
        "$key": "-N8WVarCCdD5kZ-3458U"
    },
    {
        "className": "sss-1",
        "comment": "Fairly Good",
        "exam": 40,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Joshua Philip",
        "grade": "C",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "physics",
        "term": "third-term",
        "total": 54,
        "username": "2022/SDT/62201",
        "$key": "-N8WUbvxn7RoXr16LqCo"
    },
    {
        "className": "sss-2",
        "comment": "Fail",
        "exam": 16,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Emmanuel Tony",
        "grade": "F",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "geography",
        "term": "third-term",
        "total": 37,
        "username": "2022/SDT/6217",
        "$key": "-N8WUQi6EyUBNCfnJVnq"
    },
    {
        "className": "sss-2",
        "comment": "Fairly Good",
        "exam": 40,
        "examiner": 88288828,
        "firstCA": 7,
        "fullname": "Emmanuel Tony",
        "grade": "C",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 59,
        "username": "2022/SDT/6217",
        "$key": "-N8WUFIw_UCD3dX1ESh6"
    },
    {
        "className": "sss-1",
        "comment": "Fairly Good",
        "exam": 41,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Divine Irimiya",
        "grade": "C",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 59,
        "username": "2022/SDT/62317",
        "$key": "-N8WU6Em0rtEsZc5BJ2e"
    },
    {
        "className": "sss-1",
        "comment": "Weak",
        "exam": 22,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Chidiebube Ikechukwu",
        "grade": "E",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 41,
        "username": "2022/SDT/62502",
        "$key": "-N8WTw7GWB60ops3cs1D"
    },
    {
        "className": "sss-1",
        "comment": "Fail",
        "exam": 14,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Joshua Philip",
        "grade": "F",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 26,
        "username": "2022/SDT/62201",
        "$key": "-N8WTn8icBSiQ_WRJnFx"
    },
    {
        "className": "sss-1",
        "comment": "Fairly Good",
        "exam": 36,
        "examiner": 88288828,
        "firstCA": 13,
        "fullname": "Moses Bulus",
        "grade": "C",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 57,
        "username": "2022/SDT/62369",
        "$key": "-N8WTc6jGksgs7KP5ZaT"
    },
    {
        "className": "jss-3",
        "comment": "Weak",
        "exam": 24,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Kelvin Yakubu",
        "grade": "E",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 44,
        "username": "2022/SDT/62343",
        "$key": "-N8WTT993Z4mi8mNHxYv"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 14,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "John Michael",
        "grade": "F",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 35,
        "username": "2022/SDT/6267",
        "$key": "-N8WTJAuozz80bMBB0R4"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 0,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Shedrach Ogonna",
        "grade": "F",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 19,
        "username": "2022/SDT/62615",
        "$key": "-N8WT2y_64khq7shn_qc"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 0,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Joseph Okih",
        "grade": "F",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 20,
        "username": "2022/SDT/62678",
        "$key": "-N8WRLgJNxCac-OuYseB"
    },
    {
        "className": "jss-3",
        "comment": "Pass",
        "exam": 26,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Soteria John",
        "grade": "D",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 47,
        "username": "2022/SDT/62250",
        "$key": "-N8WQzv6HwFUjrKYSuNL"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 10,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "David Wilson",
        "grade": "F",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 30,
        "username": "2022/SDT/62694",
        "$key": "-N8WQnB-B0wvcJrx7pZZ"
    },
    {
        "className": "jss-3",
        "comment": "Fairly Good",
        "exam": 38,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Bolu Henry",
        "grade": "C",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 59,
        "username": "2022/SDT/62136",
        "$key": "-N8WQcTcg8rLdEWE-S0U"
    },
    {
        "className": "jss-2",
        "comment": "Very Good",
        "exam": 54,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Grace Dogara",
        "grade": "A",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 77,
        "username": "2022/SDT/6265",
        "$key": "-N8WQUL4B63B_RXvj2-U"
    },
    {
        "className": "jss-2",
        "comment": "Very Good",
        "exam": 48,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Merit Michael",
        "grade": "A",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 71,
        "username": "2022/SDT/62818",
        "$key": "-N8WQJmUjJYsrHupMG4z"
    },
    {
        "className": "jss-2",
        "comment": "Very Good",
        "exam": 58,
        "examiner": 88288828,
        "firstCA": 8,
        "fullname": "Jesse Joseph",
        "grade": "A",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 75,
        "username": "2022/SDT/62834",
        "$key": "-N8WQ4ZneGQxzjbaqQJh"
    },
    {
        "className": "jss-2",
        "comment": "Weak",
        "exam": 28,
        "examiner": 88288828,
        "firstCA": 8,
        "fullname": "Stephanie Bako",
        "grade": "E",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 43,
        "username": "2022/SDT/62703",
        "$key": "-N8WPv1QWpbqUyXXow75"
    },
    {
        "className": "jss-2",
        "comment": "Pass",
        "exam": 29,
        "examiner": 88288828,
        "firstCA": 7,
        "fullname": "Success Monday",
        "grade": "D",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 46,
        "username": "2022/SDT/62805",
        "$key": "-N8WPl60-pnjvl3EqdTG"
    },
    {
        "className": "jss-2",
        "comment": "Fairly Good",
        "exam": 35,
        "examiner": 88288828,
        "firstCA": 9,
        "fullname": "Purity Ezekiel",
        "grade": "C",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 52,
        "username": "2022/SDT/62239",
        "$key": "-N8WPHbnxp2OgeGECMsT"
    },
    {
        "className": "jss-2",
        "comment": "Fairly Good",
        "exam": 35,
        "examiner": 88288828,
        "firstCA": 8,
        "fullname": "Stephanie Akolo",
        "grade": "C",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 52,
        "username": "2022/SDT/62370",
        "$key": "-N8WP7ADuem9DVIdsQRH"
    },
    {
        "className": "jss-2",
        "comment": "Very Good",
        "exam": 48,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Rhoda Matthew",
        "grade": "A",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 71,
        "username": "2022/SDT/62882",
        "$key": "-N8WOzarjx0u01MzeFxY"
    },
    {
        "className": "jss-2",
        "comment": "Excellent",
        "exam": 69,
        "examiner": 88288828,
        "firstCA": 15,
        "fullname": "Possible Wilson",
        "grade": "A*",
        "secondCA": 15,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 99,
        "username": "2022/SDT/65335",
        "$key": "-N8WOjrwCjZVAzoXQ0Q_"
    },
    {
        "className": "jss-1",
        "comment": "Weak",
        "exam": 28,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Johnson Akolo",
        "grade": "E",
        "secondCA": 9,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 42,
        "username": "2022/SDT/6214",
        "$key": "-N8WOYkDUyPUhfIFTPKk"
    },
    {
        "className": "jss-1",
        "comment": "Pass",
        "exam": 29,
        "examiner": 88288828,
        "firstCA": 7,
        "fullname": "Charles Joshua",
        "grade": "D",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 47,
        "username": "2022/SDT/62237",
        "$key": "-N8WOCQV1YHYwluM7TgJ"
    },
    {
        "className": "jss-1",
        "comment": "Good",
        "exam": 43,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Melody Irimiya",
        "grade": "B",
        "secondCA": 14,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 67,
        "username": "2022/SDT/62976",
        "$key": "-N8WNxpzyWsRQce3fXmm"
    },
    {
        "className": "jss-1",
        "comment": "Very Good",
        "exam": 51,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Janet Olayemi",
        "grade": "A",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 71,
        "username": "2022/SDT/62454",
        "$key": "-N8WNdkmYY5XOEUsxzkW"
    },
    {
        "className": "jss-1",
        "comment": "Weak",
        "exam": 29,
        "examiner": 88288828,
        "firstCA": 6,
        "fullname": "Mary Chibunna",
        "grade": "E",
        "secondCA": 6,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 41,
        "username": "2022/SDT/62168",
        "$key": "-N8WNVHQ1Y2NrLZj-ElL"
    },
    {
        "className": "jss-1",
        "comment": "Excellent",
        "exam": 63,
        "examiner": 88288828,
        "firstCA": 13,
        "fullname": "Victor Henry",
        "grade": "A*",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 87,
        "username": "2022/SDT/62452",
        "$key": "-N8WNLKHU7Pnipq88Zy0"
    },
    {
        "className": "jss-1",
        "comment": "Excellent",
        "exam": 59,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Abraham Joseph",
        "grade": "A*",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 82,
        "username": "2022/SDT/62991",
        "$key": "-N8WNBcuEqpcmeM8plGO"
    },
    {
        "className": "jss-1",
        "comment": "Excellent",
        "exam": 69,
        "examiner": 88288828,
        "firstCA": 15,
        "fullname": "Victoria Solomon",
        "grade": "A*",
        "secondCA": 15,
        "session": "2021/2022",
        "subject": "maths",
        "term": "third-term",
        "total": 99,
        "username": "2022/SDT/62357",
        "$key": "-N8WN3jt8qr3-_Aj7Q4y"
    },
    {
        "className": "sss-2",
        "comment": "Fail",
        "exam": 22,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Precious Tony",
        "grade": "F",
        "secondCA": 5,
        "session": "2021/2022",
        "subject": "physics",
        "term": "second-term",
        "total": 38,
        "username": "2022/SDT/62397",
        "$key": "-N8WMh3HHABt__OPuZuX"
    },
    {
        "className": "sss-1",
        "comment": "Good",
        "exam": 39,
        "examiner": 88288828,
        "firstCA": 13,
        "fullname": "Chidiebube Ikechukwu",
        "grade": "B",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "physics",
        "term": "second-term",
        "total": 64,
        "username": "2022/SDT/62502",
        "$key": "-N8WMZon6bWTSXZECa_Z"
    },
    {
        "className": "sss-1",
        "comment": "Pass",
        "exam": 32,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Joshua Philip",
        "grade": "D",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "physics",
        "term": "second-term",
        "total": 49,
        "username": "2022/SDT/62201",
        "$key": "-N8WMPfXAm323aJJBtK2"
    },
    {
        "className": "sss-2",
        "comment": "Pass",
        "exam": 27,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Emmanuel Tony",
        "grade": "D",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "geography",
        "term": "second-term",
        "total": 45,
        "username": "2022/SDT/6217",
        "$key": "-N8WMDScnIYYIgsJlYHc"
    },
    {
        "className": "sss-2",
        "comment": "Fail",
        "exam": 19,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Precious Tony",
        "grade": "F",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "geography",
        "term": "second-term",
        "total": 36,
        "username": "2022/SDT/62397",
        "$key": "-N8WM4hQbG6ylSxokqd0"
    },
    {
        "className": "sss-1",
        "comment": "Weak",
        "exam": 23,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Chidiebube Ikechukwu",
        "grade": "E",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "geography",
        "term": "second-term",
        "total": 44,
        "username": "2022/SDT/62502",
        "$key": "-N8WLv1rBY5P1fsy4478"
    },
    {
        "className": "sss-1",
        "comment": "Pass",
        "exam": 31,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Joshua Philip",
        "grade": "D",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "geography",
        "term": "second-term",
        "total": 49,
        "username": "2022/SDT/62201",
        "$key": "-N8WL_IMRuhLJs0kB7Mq"
    },
    {
        "className": "sss-2",
        "comment": "Weak",
        "exam": 20,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Emmanuel Tony",
        "grade": "E",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 41,
        "username": "2022/SDT/6217",
        "$key": "-N8WLD0OM6MLOpWMjkn_"
    },
    {
        "className": "sss-2",
        "comment": "Fail",
        "exam": 10,
        "examiner": 88288828,
        "firstCA": 8,
        "fullname": "Precious Tony",
        "grade": "F",
        "secondCA": 8,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 26,
        "username": "2022/SDT/62397",
        "$key": "-N8WL3LYSpVSc1cx8_23"
    },
    {
        "className": "sss-1",
        "comment": "Excellent",
        "exam": 64,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Divine Irimiya",
        "grade": "A*",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 87,
        "username": "2022/SDT/62317",
        "$key": "-N8WKvdrVV754nzuEcnM"
    },
    {
        "className": "sss-1",
        "comment": "Fairly Good",
        "exam": 37,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Chidiebube Ikechukwu",
        "grade": "C",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 55,
        "username": "2022/SDT/62502",
        "$key": "-N8WKkp-jr7O9TQgGBKW"
    },
    {
        "className": "sss-1",
        "comment": "Fail",
        "exam": 15,
        "examiner": 88288828,
        "firstCA": 6,
        "fullname": "Joshua Philip",
        "grade": "F",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 34,
        "username": "2022/SDT/62201",
        "$key": "-N8WK_Xy-BF8HEdK4mMW"
    },
    {
        "className": "sss-1",
        "comment": "Very Good",
        "exam": 57,
        "examiner": 88288828,
        "firstCA": 7,
        "fullname": "Moses Bulus",
        "grade": "A",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 76,
        "username": "2022/SDT/62369",
        "$key": "-N8WKLzFaa8OjnvjiUTx"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 17,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Kelvin Yakubu",
        "grade": "F",
        "secondCA": 5,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 27,
        "username": "2022/SDT/62343",
        "$key": "-N8WJvthAgi4mJ8hi3md"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 20,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "John Michael",
        "grade": "F",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 36,
        "username": "2022/SDT/6267",
        "$key": "-N8WJdMMojSVozpmA09N"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 19,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Shedrach Ogonna",
        "grade": "F",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 35,
        "username": "2022/SDT/62615",
        "$key": "-N8WJTe2IhTrGaWHVEl1"
    },
    {
        "className": "jss-3",
        "comment": "Good",
        "exam": 40,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Joseph Okih",
        "grade": "B",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 61,
        "username": "2022/SDT/62678",
        "$key": "-N8WJJAGPbDIX4XTJ8v-"
    },
    {
        "className": "jss-3",
        "comment": "Weak",
        "exam": 28,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Soteria John",
        "grade": "E",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 43,
        "username": "2022/SDT/62250",
        "$key": "-N8WJ4pn8sFal01FL9EM"
    },
    {
        "className": "jss-3",
        "comment": "Excellent",
        "exam": 63,
        "examiner": 88288828,
        "firstCA": 15,
        "fullname": "David Wilson",
        "grade": "A*",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 91,
        "username": "2022/SDT/62694",
        "$key": "-N8WIuME9Ab_Synez860"
    },
    {
        "className": "jss-3",
        "comment": "Fail",
        "exam": 22,
        "examiner": 88288828,
        "firstCA": 5,
        "fullname": "Bolu Henry",
        "grade": "F",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 34,
        "username": "2022/SDT/62136",
        "$key": "-N8WIhpNlzg0XMGEnDH7"
    },
    {
        "className": "jss-2",
        "comment": "Good",
        "exam": 41,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Grace Dogara",
        "grade": "B",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 64,
        "username": "2022/SDT/6265",
        "$key": "-N8WIMt7LAMXhb9wtfwV"
    },
    {
        "className": "jss-2",
        "comment": "Fairly Good",
        "exam": 27,
        "examiner": 88288828,
        "firstCA": 12,
        "fullname": "Merit Michael",
        "grade": "C",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 51,
        "username": "2022/SDT/62818",
        "$key": "-N8WIAvEDmJvalvtZHzr"
    },
    {
        "className": "jss-2",
        "comment": "Fail",
        "exam": 14,
        "examiner": 88288828,
        "firstCA": 6,
        "fullname": "Jesse Joseph",
        "grade": "F",
        "secondCA": 5,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 25,
        "username": "2022/SDT/62834",
        "$key": "-N8WI-pPLOD7tneaguze"
    },
    {
        "className": "jss-2",
        "comment": "Fail",
        "exam": 18,
        "examiner": 88288828,
        "firstCA": 6,
        "fullname": "Stephanie Bako",
        "grade": "F",
        "secondCA": 7,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 31,
        "username": "2022/SDT/62703",
        "$key": "-N8WHqsgqkLWN54LhbUw"
    },
    {
        "className": "jss-2",
        "comment": "Fail",
        "exam": 11,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Success Monday",
        "grade": "F",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 32,
        "username": "2022/SDT/62805",
        "$key": "-N8WHd5v1kfZcMk4bAcc"
    },
    {
        "className": "jss-2",
        "comment": "Fail",
        "exam": 15,
        "examiner": 88288828,
        "firstCA": 9,
        "fullname": "Purity Ezekiel",
        "grade": "F",
        "secondCA": 6,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 30,
        "username": "2022/SDT/62239",
        "$key": "-N8WHU0xz6wr0V1n3HOn"
    },
    {
        "className": "jss-2",
        "comment": "Fail",
        "exam": 15,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Stephanie Akolo",
        "grade": "F",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 35,
        "username": "2022/SDT/62370",
        "$key": "-N8WHKTs3oVs5ssFr-wS"
    },
    {
        "className": "jss-2",
        "comment": "Good",
        "exam": 40,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Rhoda Matthew",
        "grade": "B",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 62,
        "username": "2022/SDT/62882",
        "$key": "-N8WH7Up0KE_fgU6PkUG"
    },
    {
        "className": "jss-2",
        "comment": "Excellent",
        "exam": 58,
        "examiner": 88288828,
        "firstCA": 15,
        "fullname": "Possible Wilson",
        "grade": "A*",
        "secondCA": 14,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 87,
        "username": "2022/SDT/65335",
        "$key": "-N8WGxsNXJgkgfvwpPay"
    },
    {
        "className": "jss-1",
        "comment": "Weak",
        "exam": 20,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Johnson Akolo",
        "grade": "E",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 41,
        "username": "2022/SDT/6214",
        "$key": "-N8WGgWtC7r8vJX0m_p6"
    },
    {
        "className": "jss-1",
        "comment": "Fail",
        "exam": 18,
        "examiner": 88288828,
        "firstCA": 10,
        "fullname": "Goodluck Jonathan",
        "grade": "F",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 39,
        "username": "2022/SDT/62151",
        "$key": "-N8WGPLNf_tOW55S8mIg"
    },
    {
        "className": "jss-1",
        "comment": "Fairly Good",
        "exam": 32,
        "examiner": 88288828,
        "firstCA": 12,
        "fullname": "Melody Irimiya",
        "grade": "C",
        "secondCA": 11,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 55,
        "username": "2022/SDT/62976",
        "$key": "-N8WG8A9oGJiAByIA_xU"
    },
    {
        "className": "jss-1",
        "comment": "Fairly Good",
        "exam": 30,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Janet Olayemi",
        "grade": "C",
        "secondCA": 12,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 53,
        "username": "2022/SDT/62454",
        "$key": "-N8WFyMLxMVJ2p7QaAIh"
    },
    {
        "className": "jss-1",
        "comment": "Fail",
        "exam": 20,
        "examiner": 88288828,
        "firstCA": 9,
        "fullname": "Mary Chibunna",
        "grade": "F",
        "secondCA": 10,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 39,
        "username": "2022/SDT/62168",
        "$key": "-N8WFlI_C0Tk_Pr3us2x"
    },
    {
        "className": "jss-1",
        "comment": "Good",
        "exam": 41,
        "examiner": 88288828,
        "firstCA": 12,
        "fullname": "Victor Henry",
        "grade": "B",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 66,
        "username": "2022/SDT/62452",
        "$key": "-N8WFa7p4pBxgfDQWjsk"
    },
    {
        "className": "jss-1",
        "comment": "Fairly Good",
        "exam": 28,
        "examiner": 88288828,
        "firstCA": 11,
        "fullname": "Abraham Joseph",
        "grade": "C",
        "secondCA": 13,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 52,
        "username": "2022/SDT/62991",
        "$key": "-N8WFRXwuVO1zvcpZgoZ"
    },
    {
        "className": "jss-1",
        "comment": "Very Good",
        "exam": 47,
        "examiner": 88288828,
        "firstCA": 14,
        "fullname": "Victoria Solomon",
        "grade": "A",
        "secondCA": 14,
        "session": "2021/2022",
        "subject": "maths",
        "term": "second-term",
        "total": 75,
        "username": "2022/SDT/62357",
        "$key": "-N8WFDTEVaDWg4oSk765"
    }
]


def get_scores():
    items = ExamScore.objects.all()
    scores = []
    for item in items:
        scores.append(item)
    all_exams = scores
    if production:
        response = urllib.request.urlopen(f'{base_url}/benion-cbt/api/cbt-exam-data').read()
        json_data = json.loads(response)
        all_exams = json_data['data'][3]
    return all_exams
