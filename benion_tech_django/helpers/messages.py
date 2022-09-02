import json
import urllib.request
from benion_tech_django.settings import env
from user_app.models import ContactMessage

base_url = 'https://benion-tech-server.herokuapp.com'
production = env('PRODUCTION') == 'True'
data = [
    {
        "date": "8/1/2022",
        "email": "divine-martins-cbt@exams.com",
        "fullname": "Divine Martins",
        "message": "I just concluded the Mathematics exams for SSS 2 of General category, i answered 19 questions and scored 16 (84%)",
        "time": "7:14:42 PM",
        "$key": "-N8PpELFBJ7oNu-2f8mJ"
    },
    {
        "date": "7/28/2022",
        "email": "joyce-martins-cbt@exams.com",
        "fullname": "Joyce Martins",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 17 (89%)",
        "time": "6:48:18 PM",
        "$key": "-N857pnoBftpLs_2X4r7"
    },
    {
        "date": "7/28/2022",
        "email": "rejoice-martins-cbt@exams.com",
        "fullname": "Rejoice Martins",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 10 (52%)",
        "time": "6:38:43 PM",
        "$key": "-N855dPKj6N3rYQ9plfM"
    },
    {
        "date": "7/26/2022",
        "email": "david-wilson-cbt@exams.com",
        "fullname": "David  Wilson ",
        "message": "I just concluded the Mathematics exams for JSS 3 of Junior category, i answered 19 questions and scored 19 (100%)",
        "time": "8:58:54 PM",
        "$key": "-N7wIYMxA4yk_yCP2Fxm"
    },
    {
        "date": "7/26/2022",
        "email": "victor-henry-cbt@exams.com",
        "fullname": "Victor  Henry ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 16 (84%)",
        "time": "8:42:17 AM",
        "$key": "-N7tewv5-IPl0GL1Jnsy"
    },
    {
        "date": "7/26/2022",
        "email": "mary-chibunna-cbt@exams.com",
        "fullname": "Mary Chibunna ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "8:39:19 AM",
        "$key": "-N7teGaFh4kK1RGqGipL"
    },
    {
        "date": "7/26/2022",
        "email": "kelvin-yakubu-cbt@exams.com",
        "fullname": "Kelvin  Yakubu ",
        "message": "I just concluded the Mathematics exams for JSS 3 of Junior category, i answered 19 questions and scored 6 (31%)",
        "time": "8:36:21 AM",
        "$key": "-N7tda25uugO8YEZU9wQ"
    },
    {
        "date": "7/26/2022",
        "email": "success-monday-cbt@exams.com",
        "fullname": "Success  Monday ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 11 (57%)",
        "time": "8:31:54 AM",
        "$key": "-N7tcZpQtD1M_-LeEbPV"
    },
    {
        "date": "7/26/2022",
        "email": "stephanie-bako-cbt@exams.com",
        "fullname": "Stephanie Bako ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 10 (52%)",
        "time": "8:28:11 AM",
        "$key": "-N7tbiWA8K88SyYsS8v-"
    },
    {
        "date": "7/26/2022",
        "email": "abraham-joseph-cbt@exams.com",
        "fullname": "Abraham  Joseph ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "8:23:29 AM",
        "$key": "-N7tadalZwTDT5zlsfaK"
    },
    {
        "date": "7/26/2022",
        "email": "stephanie-akolo-cbt@exams.com",
        "fullname": "Stephanie  Akolo ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 11 (57%)",
        "time": "8:18:41 AM",
        "$key": "-N7t_YOTnOY30UMlqSYw"
    },
    {
        "date": "7/26/2022",
        "email": "johnson-akolo-cbt@exams.com",
        "fullname": "Johnson  Akolo",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 7 (36%)",
        "time": "8:12:04 AM",
        "$key": "-N7tZ1Q7X7CQBZQw-xCg"
    },
    {
        "date": "7/25/2022",
        "email": "possible-wilson-cbt@exams.com",
        "fullname": "Possible  Wilson ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 19 (100%)",
        "time": "5:49:31 PM",
        "$key": "-N7qTbP6jANFoMb1AKYS"
    },
    {
        "date": "7/25/2022",
        "email": "moses-bulus-cbt@exams.com",
        "fullname": "Moses  Bulus",
        "message": "I just concluded the Mathematics exams for SSS 1 of General category, i answered 19 questions and scored 7 (36%)",
        "time": "11:55:37 AM",
        "$key": "-N7pCbHD9zvlOQP8niAG"
    },
    {
        "date": "7/25/2022",
        "email": "divine-irimiya-cbt@exams.com",
        "fullname": "Divine Irimiya ",
        "message": "I just concluded the Mathematics exams for SSS 1 of General category, i answered 19 questions and scored 11 (57%)",
        "time": "11:53:56 AM",
        "$key": "-N7pCDhBucFAtWKaztgA"
    },
    {
        "date": "7/25/2022",
        "email": "merit-michael-cbt@exams.com",
        "fullname": "Merit  Michael ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 12 (63%)",
        "time": "11:46:36 AM",
        "$key": "-N7pAYC55J2NNaoBwfOn"
    },
    {
        "date": "7/25/2022",
        "email": "melody-irimiya-cbt@exams.com",
        "fullname": "Melody  Irimiya ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "11:39:55 AM",
        "$key": "-N7p90KW9WxCAmWki8rC"
    },
    {
        "date": "7/25/2022",
        "email": "janet-olayemi-cbt@exams.com",
        "fullname": "Janet  Olayemi ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "11:33:41 AM",
        "$key": "-N7p7_x5T8O0KAdBtc8c"
    },
    {
        "date": "7/25/2022",
        "email": "purity-ezekiel-cbt@exams.com",
        "fullname": "Purity  Ezekiel ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 7 (36%)",
        "time": "11:29:07 AM",
        "$key": "-N7p6YB30PX10WMAL8IX"
    },
    {
        "date": "7/25/2022",
        "email": "charles-joshua-cbt@exams.com",
        "fullname": "Charles  Joshua",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 13 (68%)",
        "time": "11:24:52 AM",
        "$key": "-N7p5Zs_y2sHbOcQLVCN"
    },
    {
        "date": "7/25/2022",
        "email": "jesse-joseph-cbt@exams.com",
        "fullname": "Jesse  Joseph ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 14 (73%)",
        "time": "11:20:17 AM",
        "$key": "-N7p4WidvHqDWWcsAZAj"
    },
    {
        "date": "7/25/2022",
        "email": "rhoda-matthew-cbt@exams.com",
        "fullname": "Rhoda Matthew ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 11 (57%)",
        "time": "11:15:16 AM",
        "$key": "-N7p3NEYLq-_mTBFf2Q-"
    },
    {
        "date": "7/25/2022",
        "email": "grace-dogara-cbt@exams.com",
        "fullname": "Grace  Dogara ",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 14 (73%)",
        "time": "11:02:25 AM",
        "$key": "-N7p0R2qlJAr7M_AZIUF"
    },
    {
        "date": "7/25/2022",
        "email": "victoria-solomon-cbt@exams.com",
        "fullname": "Victoria  Solomon ",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 15 (78%)",
        "time": "10:54:48 AM",
        "$key": "-N7ozgWSstcq4MPmRvod"
    },
    {
        "date": "7/24/2022",
        "email": "test-testing-cbt@exams.com",
        "fullname": "Test Testing",
        "message": "I just concluded the Mathematics exams for SSS 1 of General category, i answered 19 questions and scored 17 (89%)",
        "time": "3:47:45 AM",
        "$key": "-N7iJLxsHhZhISKm5M5R"
    },
    {
        "date": "7/24/2022",
        "email": "example-test-cbt@exams.com",
        "fullname": "Example  Test",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 19 (100%)",
        "time": "3:08:47 AM",
        "$key": "-N7iARMGCaAxBTW9zOKr"
    },
    {
        "date": "7/24/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Rejoice Martins",
        "message": "A new cbt user (Rejoice Martins) with password (WkTDaLjy) and role (student) was attempted to be created by access code (88288828).",
        "time": "2:08:28 AM",
        "$key": "-N7hxciUXjpJBF9U87mw"
    },
    {
        "date": "7/24/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Joyce Martins",
        "message": "A new cbt user (Joyce Martins) with password (GAC5jH4h) and role (student) was attempted to be created by access code (88288828).",
        "time": "2:08:03 AM",
        "$key": "-N7hxXZ8pCVKJTdH9l0C"
    },
    {
        "date": "7/24/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Cletus Iorver",
        "message": "A new cbt user (Cletus Iorver) with password (xtYNPb28) and role (student) was attempted to be created by access code (88288828).",
        "time": "2:07:39 AM",
        "$key": "-N7hxRewn0e88Y1YwxWr"
    },
    {
        "date": "7/24/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Divine Martins",
        "message": "A new cbt user (Divine Martins) with password (9b72uPEV) and role (student) was attempted to be created by access code (88288828).",
        "time": "2:06:38 AM",
        "$key": "-N7hxCta3BCLRT3zmxT7"
    },
    {
        "date": "7/24/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Hilary Iorver",
        "message": "A new cbt user (Hilary Iorver) with password (n4fHF94O) and role (student) was attempted to be created by access code (88288828).",
        "time": "2:05:22 AM",
        "$key": "-N7hwvFYhUp8yyPeanKX"
    },
    {
        "date": "7/24/2022",
        "email": "test-testing-cbt@exams.com",
        "fullname": "Test Testing",
        "message": "I just concluded the Mathematics exams for SSS 1 of General category, i answered 19 questions and scored 16 (84%)",
        "time": "2:02:43 AM",
        "$key": "-N7hwJYdnGE0L0zebP-x"
    },
    {
        "date": "7/24/2022",
        "email": "example -test-cbt@exams.com",
        "fullname": "Example  Test",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "1:45:28 AM",
        "$key": "-N7hsMn-0Q_vPoSM714M"
    },
    {
        "date": "7/23/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for SSS 2 of General category, i answered 19 questions and scored 19 (100%)",
        "time": "5:07:10 AM",
        "$key": "-N7dRwb1yB0D4KfCerNB"
    },
    {
        "date": "7/23/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for SSS 1 of General category, i answered 19 questions and scored 19 (100%)",
        "time": "4:45:46 AM",
        "$key": "-N7dN2G83xe-0IUY5ykz"
    },
    {
        "date": "7/23/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for JSS 3 of Junior category, i answered 19 questions and scored 19 (100%)",
        "time": "3:45:36 AM",
        "$key": "-N7d9Ginfws7RwIjJzpk"
    },
    {
        "date": "7/23/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for JSS 2 of Junior category, i answered 19 questions and scored 17 (89%)",
        "time": "3:32:28 AM",
        "$key": "-N7d6GM0eiqq3hB_pmkc"
    },
    {
        "date": "7/23/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for JSS 1 of Junior category, i answered 19 questions and scored 18 (94%)",
        "time": "3:18:42 AM",
        "$key": "-N7d36gT7UYzc1JZVnrU"
    },
    {
        "date": "7/22/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Possible  Wilson ",
        "message": "A new cbt user (Possible  Wilson ) with password (syQSYUd2) and role (student) was attempted to be created by access code (88288828).",
        "time": "10:22:53 AM",
        "$key": "-N7_QbbyQ9mcCpkukCNb"
    },
    {
        "date": "7/22/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for SSS 2 of General category, i answered 19 questions and scored 16 (84%)",
        "time": "5:28:49 AM",
        "$key": "-N7ZNJ0rZEwQJALRunOL"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Success  Monday ",
        "message": "A new cbt user (Success  Monday ) with password (PxItjo3X) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:41:51",
        "$key": "-N7KbiV6HaWgO966ocny"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Stephanie  Akolo ",
        "message": "A new cbt user (Stephanie  Akolo ) with password (NCfG94bI) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:41:28",
        "$key": "-N7KbckSEjx6uuIf4P4Z"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Stephanie Bako ",
        "message": "A new cbt user (Stephanie Bako ) with password (UeLelTBk) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:41:7",
        "$key": "-N7KbYhN-ZxAruN5-lDk"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Purity  Ezekiel ",
        "message": "A new cbt user (Purity  Ezekiel ) with password (oQVa6EMT) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:40:13",
        "$key": "-N7KbLPaoa8uokEF7zP4"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Merit  Michael ",
        "message": "A new cbt user (Merit  Michael ) with password (ukvIS47S) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:39:34",
        "$key": "-N7KbC1EaD2OnNeYIm0I"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Jesse  Joseph ",
        "message": "A new cbt user (Jesse  Joseph ) with password (B2Ph5kc8) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:39:8",
        "$key": "-N7Kb5g2Mg4AXLQKR6IR"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Rhoda Matthew ",
        "message": "A new cbt user (Rhoda Matthew ) with password (l53zSOA6) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:38:21",
        "$key": "-N7KavF1j2fW11a7tD1-"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Grace  Dogara ",
        "message": "A new cbt user (Grace  Dogara ) with password (Yb0ZfGbL) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:37:6",
        "$key": "-N7Kacjk2iq0JEHDlPFM"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Soteria  John ",
        "message": "A new cbt user (Soteria  John ) with password (MmXJKgmg) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:35:27",
        "$key": "-N7KaFbRT3vSDce_G0r5"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Kelvin  Yakubu ",
        "message": "A new cbt user (Kelvin  Yakubu ) with password (YldVKQTW) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:34:48",
        "$key": "-N7Ka66hvsT-wa4nXHv4"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Shedrach Ogonna ",
        "message": "A new cbt user (Shedrach Ogonna ) with password (im6WUIAm) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:34:28",
        "$key": "-N7Ka1IHzk_OQSgW-xQN"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Bolu Henry ",
        "message": "A new cbt user (Bolu Henry ) with password (TL11QOl7) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:33:13",
        "$key": "-N7K_jqGBvXqpxmmsjUQ"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Joseph  Okih",
        "message": "A new cbt user (Joseph  Okih) with password (2flVE7a0) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:32:48",
        "$key": "-N7K_ds5BnjWDCKSYF7y"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "John  Michael ",
        "message": "A new cbt user (John  Michael ) with password (ksG9fR2a) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:32:22",
        "$key": "-N7K_YPs_ul74KcAzZa2"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "David  Wilson ",
        "message": "A new cbt user (David  Wilson ) with password (oTCILAQq) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:31:54",
        "$key": "-N7K_RZ-R_4v8H9hN-BD"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Precious  Tony",
        "message": "A new cbt user (Precious  Tony) with password (NK6V6eEd) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:29:38",
        "$key": "-N7KZvRb2gVjfJ7TpVYm"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Emmanuel  Tony ",
        "message": "A new cbt user (Emmanuel  Tony ) with password (2PDjVgQS) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:29:19",
        "$key": "-N7KZqhn4528HViTTv0s"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Moses  Bulus",
        "message": "A new cbt user (Moses  Bulus) with password (Iju3sinb) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:28:23",
        "$key": "-N7KZd5t7MGmH3RjCZ-t"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Divine Irimiya ",
        "message": "A new cbt user (Divine Irimiya ) with password (USFEnbKP) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:27:40",
        "$key": "-N7KZT_xnNc-df-wo1UB"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Chidiebube Ikechukwu",
        "message": "A new cbt user (Chidiebube Ikechukwu) with password (76hpVIDs) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:27:15",
        "$key": "-N7KZNYugMT18jjyFyZF"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Joshua  Philip ",
        "message": "A new cbt user (Joshua  Philip ) with password (4P2eNNDq) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:23:11",
        "$key": "-N7KYRt6qM30W1m6uxpb"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Goodluck  Jonathan ",
        "message": "A new cbt user (Goodluck  Jonathan ) with password (ePK4NzkS) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:22:32",
        "$key": "-N7KYIM6t_K_LynWH-70"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Johnson  Akolo",
        "message": "A new cbt user (Johnson  Akolo) with password (v4apBSJg) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:22:8",
        "$key": "-N7KYCUM-Kbxzpz49Tac"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Abraham  Joseph ",
        "message": "A new cbt user (Abraham  Joseph ) with password (q3u7JDYp) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:21:32",
        "$key": "-N7KY3hEC1oP_tsDK-G1"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Victor  Henry ",
        "message": "A new cbt user (Victor  Henry ) with password (z6Cw70Hm) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:21:10",
        "$key": "-N7KXzPZSnia-91lfBsn"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Charles  Joseph ",
        "message": "A new cbt user (Charles  Joseph ) with password (s0U6d7ks) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:20:51",
        "$key": "-N7KXuiKQkiFQJDvacFG"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Mary Chibunna ",
        "message": "A new cbt user (Mary Chibunna ) with password (YCScCOU6) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:20:19",
        "$key": "-N7KXmufi8cGBjaawzRT"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Janet  Olayemi ",
        "message": "A new cbt user (Janet  Olayemi ) with password (fWFwDupT) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:19:39",
        "$key": "-N7KXdDKmnYb0bsPMCau"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Melody  Irimiya ",
        "message": "A new cbt user (Melody  Irimiya ) with password (eGkIvh4L) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:19:9",
        "$key": "-N7KXWztRHVxeJIu1FL9"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Victoria  Solomon ",
        "message": "A new cbt user (Victoria  Solomon ) with password (p9iNaNie) and role (student) was attempted to be created by access code (88288828).",
        "time": "8:18:44",
        "$key": "-N7KXQlEiqzfxEhQycVo"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Victor  Nwabudike",
        "message": "A new cbt user (Victor  Nwabudike) with password (CEwWACmx) and role (moderator) was attempted to be created by access code (88288828).",
        "time": "8:16:48",
        "$key": "-N7KWzZ3U-W3FIu-sVzU"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Joshua  Ayobami",
        "message": "A new cbt user (Joshua  Ayobami) with password (1tT3i8CY) and role (moderator) was attempted to be created by access code (88288828).",
        "time": "8:16:3",
        "$key": "-N7KWoT3ETMFfi70xaZ9"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Jacob  Wayo",
        "message": "A new cbt user (Jacob  Wayo) with password (xmcCkwfE) and role (moderator) was attempted to be created by access code (88288828).",
        "time": "8:15:24",
        "$key": "-N7KWf2wceZUrz0C3z_J"
    },
    {
        "date": "19/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Test Testing",
        "message": "A new cbt user (Test Testing) with password (SqZmQfUj) and role (student) was attempted to be created by access code (88288828).",
        "time": "1:52:25",
        "$key": "-N7J9-vntNFIQBqMlbd5"
    },
    {
        "date": "19/7/2022",
        "email": "bernard.iorver88@yahoo.com",
        "fullname": "Guest User",
        "message": "A new user (Guest User) with username (guest), password (guest123) and role (guest) was attempted to be created.",
        "time": "0:44:2",
        "$key": "-N7IuMCKxZqlJZ_yIc_u"
    },
    {
        "date": "19/7/2022",
        "email": "bernard.benion.iorver@hotmail.com",
        "fullname": "Bemshima Iorver",
        "message": "A new user (Bemshima Iorver) with username (benifresh), password (rice8828) and role (admin) was attempted to be created.",
        "time": "0:41:27",
        "$key": "-N7ItlH-rdNt3LSOQLt8"
    },
    {
        "date": "18/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Example  Test",
        "message": "A new cbt user (Example  Test) with password (y6eJAnl5) and role (student) was attempted to be created by access code (88288828).",
        "time": "10:19:57",
        "$key": "-N7Fo__xP4MNn-uwWEIf"
    },
    {
        "date": "18/7/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for SSS 2 of General category, i answered 19 questions and scored 17 (89%)",
        "time": "8:8:7",
        "$key": "-N7FLPV6G5EyHctEehtQ"
    },
    {
        "date": "18/7/2022",
        "email": "bernard-iorver-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the Mathematics exams for SSS 2 of General category, i answered 19 questions and scored 15 (78%)",
        "time": "3:2:14",
        "$key": "-N7EFOssNWF43qnpYcaB"
    },
    {
        "date": "18/7/2022",
        "email": "benion-cbt@exams.com",
        "fullname": "Bernard Iorver",
        "message": "I just concluded the maths exams, i answered 19 questions and scored 17 (89%)",
        "time": "2:1:21",
        "$key": "-N7E1Sv98Teqq1QfvzFL"
    }
]


def get_messages():
    items = ContactMessage.objects.all()
    messages = []
    for item in items:
        messages.append(item)
    all_messages = messages
    if production:
        response = urllib.request.urlopen(f'{base_url}/benion-users/api/contact-messages').read()
        json_data = json.loads(response)
        all_messages = json_data['data'][3]
    return all_messages
