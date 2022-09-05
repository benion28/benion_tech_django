import json
import urllib.request
from benion_tech_django.settings import env
from user_app.models import CbtUser


base_url = env('BASE_URL')
production = env('PRODUCTION') == 'True'
data = [
    {
        "role": "admin",
        "regType": "add",
        "_id": "629685da809a591558e9029d",
        "firstname": "Bernard",
        "lastname": "Iorver",
        "username": "2022/ADM/42710",
        "className": "graduated",
        "password": "$2a$10$AowNZX1spL9rrnjt95s9ouPBkXMHUrngb7QrLkRinZetOn3tRXyoq",
        "gender": "male",
        "accessCode": 88288828,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-05-31T21:17:14.100Z",
        "__v": 0,
        "category": "science",
        "completed": True,
        "activeExam": "d3N3SEQalp"
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d533cd00840600044dcf86",
        "firstname": "Example ",
        "lastname": "Test",
        "username": "2022/SDT/6162",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$h.WN4i7MWTTrFErUIs03..2ZpC.9RJlqRcnUvgEYVdQIauhWWRrJ2",
        "gender": "others",
        "accessCode": 22014685,
        "creator": 88288828,
        "school": "others",
        "date": "2022-07-18T10:19:57.207Z",
        "__v": 0,
        "activeExam": "rUoDFs6LUB",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d60e5ac35a8b0004f9151d",
        "firstname": "Test",
        "lastname": "Testing",
        "username": "2022/SDT/62589",
        "className": "sss-1",
        "category": "arts",
        "password": "$2a$10$1EkgdY540O7rRUIFVadOlun6022jw.ukpr7R76mnnc4fBqYBzp5/y",
        "gender": "female",
        "accessCode": 29805710,
        "creator": 88288828,
        "school": "gbis",
        "date": "2022-07-19T01:52:26.696Z",
        "__v": 0,
        "activeExam": "izjP7cYOtb",
        "completed": True
    },
    {
        "role": "moderator",
        "regType": "add",
        "_id": "62d6681dcdaa5e0004b85616",
        "firstname": "Jacob ",
        "lastname": "Wayo",
        "username": "2022/MDR/62940",
        "className": "graduated",
        "category": "science",
        "password": "$2a$10$Qf5p/7mc8J3QHY5asG4mXu7H/FFOf3PwoS2eQWapPNhycIpV0RcHi",
        "gender": "male",
        "accessCode": 28850223,
        "creator": 88288828,
        "school": "others",
        "date": "2022-07-19T08:15:25.036Z",
        "__v": 0
    },
    {
        "role": "moderator",
        "regType": "add",
        "_id": "62d66844cdaa5e0004b85617",
        "firstname": "Joshua ",
        "lastname": "Ayobami",
        "username": "2022/MDR/62964",
        "className": "graduated",
        "category": "science",
        "password": "$2a$10$TzXCqO8MWElq.HHOkrRNH.ieNJXoh21HmzhjstcanIB/fDCcEWpUu",
        "gender": "male",
        "accessCode": 66404297,
        "creator": 88288828,
        "school": "khcs",
        "date": "2022-07-19T08:16:04.054Z",
        "__v": 0
    },
    {
        "role": "moderator",
        "regType": "add",
        "_id": "62d66871cdaa5e0004b85618",
        "firstname": "Victor ",
        "lastname": "Nwabudike",
        "username": "2022/MDR/62930",
        "className": "graduated",
        "category": "science",
        "password": "$2a$10$L3Munl8o.XfakmRmxddSjuEzYc1VMqNXFvnii5MnQLc.tToPyr9tq",
        "gender": "male",
        "accessCode": 56277287,
        "creator": 88288828,
        "school": "others",
        "date": "2022-07-19T08:16:49.022Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d668e4cdaa5e0004b85619",
        "firstname": "Victoria ",
        "lastname": "Solomon ",
        "username": "2022/SDT/62357",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$R9w5zBS9kXVxBIKdtWM1zO34hnVVi3XaQaONwwvfp1BXhWXtbkbCm",
        "gender": "female",
        "accessCode": 15240023,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:18:44.446Z",
        "__v": 0,
        "activeExam": "wqbo3F4gtY",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d668fecdaa5e0004b8561a",
        "firstname": "Melody ",
        "lastname": "Irimiya ",
        "username": "2022/SDT/62976",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$uEU5MYiNcKjrqyArR4kKLutQsLg3WokQB8gLfpe9iAR6w2jQhRvqu",
        "gender": "female",
        "accessCode": 73104944,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:19:10.068Z",
        "__v": 0,
        "activeExam": "wuAQbQtAcT",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d6691bcdaa5e0004b8561b",
        "firstname": "Janet ",
        "lastname": "Olayemi ",
        "username": "2022/SDT/62454",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$SL.3GDXTxD6XnKbYSJU.zOWOAthJfPbj1LhrRFypEvTAT.7MNSlK.",
        "gender": "female",
        "accessCode": 25837888,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:19:39.556Z",
        "__v": 0,
        "activeExam": "Sz0QjgrXof",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66943cdaa5e0004b8561c",
        "firstname": "Mary",
        "lastname": "Chibunna ",
        "username": "2022/SDT/62168",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$r4CdBAzslQkRkYXZWviLDOKi6JPbLNrJLdmXAcGP.Js01M0UT5r66",
        "gender": "female",
        "accessCode": 34381653,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:20:19.258Z",
        "__v": 0,
        "activeExam": "wNcoNmhsHo",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66963cdaa5e0004b8561d",
        "firstname": "Charles ",
        "lastname": "Joshua",
        "username": "2022/SDT/62237",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$KsiSjBZkzw/7Of4vkUigk.lQ7NUtN9XQ1KRzJLXTZQTdm8RFd1Ze6",
        "gender": "male",
        "accessCode": 8365206,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:20:51.328Z",
        "__v": 0,
        "activeExam": "vGACkXquS0",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66976cdaa5e0004b8561e",
        "firstname": "Victor ",
        "lastname": "Henry ",
        "username": "2022/SDT/62452",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$bcBol/T51cwuunBOIo9Ny.GZWpU6lB.aUSO02YHa0eR65OHG9CEN.",
        "gender": "male",
        "accessCode": 87026445,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:21:10.560Z",
        "__v": 0,
        "activeExam": "IDnAdrt4DX",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d6698ccdaa5e0004b8561f",
        "firstname": "Abraham ",
        "lastname": "Joseph ",
        "username": "2022/SDT/62991",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$YCbAJXRsoICuv26l8Tav2uzejv2TeXFuQ.kTuGGxZflhW8Ucv3iua",
        "gender": "male",
        "accessCode": 72945801,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:21:32.132Z",
        "__v": 0,
        "activeExam": "gU5Z8PVBtd",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d669b0cdaa5e0004b85620",
        "firstname": "Johnson ",
        "lastname": "Akolo",
        "username": "2022/SDT/6214",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$dKvOYhX7/kks0jbD9.OkGeXFJJaUBgjdolP6XS2qUkb1S38Frk/pi",
        "gender": "male",
        "accessCode": 65629925,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:22:08.103Z",
        "__v": 0,
        "activeExam": "GaYSbY8gJ3",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d669c8cdaa5e0004b85621",
        "firstname": "Goodluck ",
        "lastname": "Jonathan ",
        "username": "2022/SDT/62151",
        "className": "jss-1",
        "category": "junior",
        "password": "$2a$10$.xYC2Egmca2G6U2ptepbdO8Oa3YkIbOBhc9ZHr8Q1e8yrSMlKya3m",
        "gender": "male",
        "accessCode": 17030809,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:22:32.242Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d669efcdaa5e0004b85622",
        "firstname": "Joshua ",
        "lastname": "Philip ",
        "username": "2022/SDT/62201",
        "className": "sss-1",
        "category": "science",
        "password": "$2a$10$KTQeYpPt3TqMcP4cCi4Rcu6icLLH0iTLKE6j.bC7Yb1kPVlmZta8q",
        "gender": "male",
        "accessCode": 90873199,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:23:11.291Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66ae3cdaa5e0004b85623",
        "firstname": "Chidiebube",
        "lastname": "Ikechukwu",
        "username": "2022/SDT/62502",
        "className": "sss-1",
        "category": "science",
        "password": "$2a$10$/tKYlFWxlgeUWF4PIyBuMuwjSs.Y41aloCVhP.JAzj40lFr4kcTL.",
        "gender": "male",
        "accessCode": 76798133,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:27:15.594Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66afccdaa5e0004b85624",
        "firstname": "Divine",
        "lastname": "Irimiya ",
        "username": "2022/SDT/62317",
        "className": "sss-1",
        "category": "arts",
        "password": "$2a$10$LE2RNWnR9q0fcZ8eRZ4dY.2hUvx91/Rarskw7Hy/44OmXBbXM3r22",
        "gender": "female",
        "accessCode": 81299370,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:27:40.409Z",
        "__v": 0,
        "activeExam": "gNfCt1qMeZ",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66b27cdaa5e0004b85625",
        "firstname": "Moses ",
        "lastname": "Bulus",
        "username": "2022/SDT/62369",
        "className": "sss-1",
        "category": "arts",
        "password": "$2a$10$eP7Yt5r65gqkiZKGXTCwiuWM/6aJgPpoY/Vv8mVPeBUV4/93DoVAu",
        "gender": "male",
        "accessCode": 73986513,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:28:23.461Z",
        "__v": 0,
        "activeExam": "RQlrm72r3H",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66b5fcdaa5e0004b85626",
        "firstname": "Emmanuel ",
        "lastname": "Tony ",
        "username": "2022/SDT/6217",
        "className": "sss-2",
        "category": "arts",
        "password": "$2a$10$NsJFSmJIw8Ij8wQFSiVylec9SOchn5nRjzc2t4jt2VCR.l8JVRL2q",
        "gender": "male",
        "accessCode": 10269321,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:29:19.107Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66b72cdaa5e0004b85627",
        "firstname": "Precious ",
        "lastname": "Tony",
        "username": "2022/SDT/62397",
        "className": "sss-2",
        "category": "science",
        "password": "$2a$10$9hOwkzHd8KjjyhoNfL1ApuM.LaEF6sMgZbBQmY7noUIhxxQeFyhK2",
        "gender": "female",
        "accessCode": 80358232,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:29:38.486Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66bfacdaa5e0004b85628",
        "firstname": "David ",
        "lastname": "Wilson ",
        "username": "2022/SDT/62694",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$JYCPj/iLTYhMc.3ifobHJegkrSrV95Ce989LcZMZjowklgZ6T7TTO",
        "gender": "male",
        "accessCode": 78671089,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:31:54.790Z",
        "__v": 0,
        "activeExam": "leFSviK4hs",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66c16cdaa5e0004b85629",
        "firstname": "John ",
        "lastname": "Michael ",
        "username": "2022/SDT/6267",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$5vsGjubkP//6NLTzyecP4uivAdfYeCj7AvvAYZYqIxjed.mxJHJke",
        "gender": "male",
        "accessCode": 32682457,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:32:22.156Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66c30cdaa5e0004b8562a",
        "firstname": "Joseph ",
        "lastname": "Okih",
        "username": "2022/SDT/62678",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$IuHWpL3PPz.lwa7Y/OQTau3AHm6y9jfafu22xEa.co9yzpwqvvhse",
        "gender": "male",
        "accessCode": 9879872,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:32:48.774Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66c49cdaa5e0004b8562b",
        "firstname": "Bolu",
        "lastname": "Henry ",
        "username": "2022/SDT/62136",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$v4z3h0FZ4aOkIV8EC2bH3ewMt620D7dlILU1SMBhuGwGqnSwBiX3e",
        "gender": "female",
        "accessCode": 97450570,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:33:13.226Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66c94cdaa5e0004b8562c",
        "firstname": "Shedrach",
        "lastname": "Ogonna ",
        "username": "2022/SDT/62615",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$/FsyWX.fBAaWiHhLLg5uY.5zpLYttcuKA44oVBVyEN4cTmq8NdpvC",
        "gender": "male",
        "accessCode": 23103900,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:34:28.707Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66ca8cdaa5e0004b8562d",
        "firstname": "Kelvin ",
        "lastname": "Yakubu ",
        "username": "2022/SDT/62343",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$2HLdNehgZ4zs/MLB9Ti6oeElsQ98xxSMKjgVQZV9SgXUtzTjZiMUa",
        "gender": "male",
        "accessCode": 48466394,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:34:48.444Z",
        "__v": 0,
        "activeExam": "TlevDNwR0y",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66ccfcdaa5e0004b8562e",
        "firstname": "Soteria ",
        "lastname": "John ",
        "username": "2022/SDT/62250",
        "className": "jss-3",
        "category": "junior",
        "password": "$2a$10$dvYswBGKigXTHGOkBt4KHO2DqknHMADspfNeR6qiTv0EBZYL7TnZW",
        "gender": "female",
        "accessCode": 6400713,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:35:27.340Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66d32cdaa5e0004b8562f",
        "firstname": "Grace ",
        "lastname": "Dogara ",
        "username": "2022/SDT/6265",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$SmclzUneJbEkEDjnOmZhFeu20jWNrEczBqlfKaBq1wkMT7lDCq/4q",
        "gender": "female",
        "accessCode": 18574152,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:37:06.175Z",
        "__v": 0,
        "activeExam": "FKx0Fki5zY",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66d7dcdaa5e0004b85630",
        "firstname": "Rhoda",
        "lastname": "Matthew ",
        "username": "2022/SDT/62882",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$USmAUQkmhIOZXHXhyubDbOMb25bqBbT.CS8RTm6Clt0enmR.AOOpq",
        "gender": "female",
        "accessCode": 15554139,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:38:21.971Z",
        "__v": 0,
        "activeExam": "3o8YZuvSM7",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66daccdaa5e0004b85631",
        "firstname": "Jesse ",
        "lastname": "Joseph ",
        "username": "2022/SDT/62834",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$L9JiEeeb3wQvfKMiRCd8BO.mZ3iZI2JqcVnscuHo868FM3NlnG7dO",
        "gender": "male",
        "accessCode": 68029703,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:39:08.926Z",
        "__v": 0,
        "activeExam": "O7zCse37yx",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66dc6cdaa5e0004b85632",
        "firstname": "Merit ",
        "lastname": "Michael ",
        "username": "2022/SDT/62818",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$PGMdxyYewDLJqeDYijFUCemHae2mudkhMIaOULjWV5aehRk/X4Yfq",
        "gender": "female",
        "accessCode": 95958609,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:39:34.910Z",
        "__v": 0,
        "activeExam": "KUHaNORIrm",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66dedcdaa5e0004b85633",
        "firstname": "Purity ",
        "lastname": "Ezekiel ",
        "username": "2022/SDT/62239",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$00fq4USOMxFwPV1fdDff/OBJ9K/om9tqx1FkOz50k59L6vpxu69b2",
        "gender": "female",
        "accessCode": 50137722,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:40:13.331Z",
        "__v": 0,
        "activeExam": "E7Zsf9UppY",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66e23cdaa5e0004b85634",
        "firstname": "Stephanie",
        "lastname": "Bako ",
        "username": "2022/SDT/62703",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$neRtI7vEiCS8gimsGpb0lODixrrghAc43OTwW4CSfPArnhWsLKQ12",
        "gender": "female",
        "accessCode": 78120442,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:41:07.794Z",
        "__v": 0,
        "activeExam": "6Wqf2Cn9Sv",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66e38cdaa5e0004b85635",
        "firstname": "Stephanie ",
        "lastname": "Akolo ",
        "username": "2022/SDT/62370",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$xgfM7O.PhvgUpCrfFxM8LeGb0xpIfdj3gS0rlem3JucF/RnUmDKD2",
        "gender": "female",
        "accessCode": 90249652,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:41:28.475Z",
        "__v": 0,
        "activeExam": "Bcw07p0rG8",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62d66e4fcdaa5e0004b85636",
        "firstname": "Success ",
        "lastname": "Monday ",
        "username": "2022/SDT/62805",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$XdxqeFMgMC4vKJn3NcASOuP5zHCxsWAk0I23tZ8yHvJYDkudBghAG",
        "gender": "female",
        "accessCode": 45848309,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-19T08:41:51.895Z",
        "__v": 0,
        "activeExam": "XzIEXmIWuS",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62da7a7d55eb2c00046d8991",
        "firstname": "Possible ",
        "lastname": "Wilson ",
        "username": "2022/SDT/65335",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$qghO82W37z2DeIEsRzxKe.wCYHbKrinBvEvP0BdRttns16uU3mO3u",
        "gender": "male",
        "accessCode": 82754796,
        "creator": 88288828,
        "school": "mrds",
        "date": "2022-07-22T10:22:53.433Z",
        "__v": 0,
        "activeExam": "IbwFmyVwCH",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62dca8e24d716e00046314a4",
        "firstname": "Hilary",
        "lastname": "Iorver",
        "username": "2022/SDT/60254",
        "className": "sss-2",
        "category": "arts",
        "password": "$2a$10$fALazZOCJknKB4JJSbozneyysZB1aY0JfIx/wcqaKAwptqpGH/K.u",
        "gender": "male",
        "accessCode": 36158665,
        "creator": 88288828,
        "school": "gbis",
        "date": "2022-07-24T02:05:22.350Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62dca92e4d716e00046314a5",
        "firstname": "Divine",
        "lastname": "Martins",
        "username": "2022/SDT/60619",
        "className": "sss-2",
        "category": "science",
        "password": "$2a$10$V3U4F6sMFauh1lH78DF1MeswJoIXBYZZmHqBgrIP6oquLvmDSm.r6",
        "gender": "female",
        "accessCode": 56652833,
        "creator": 88288828,
        "school": "gsst",
        "date": "2022-07-24T02:06:38.711Z",
        "__v": 0,
        "activeExam": "yNGthmyRPg",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62dca96b4d716e00046314a6",
        "firstname": "Cletus",
        "lastname": "Iorver",
        "username": "2022/SDT/60106",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$mh1Lg57uNexoOlsVG9nDBOwOB.C6GufmY686XKVWh55jJycxZm246",
        "gender": "male",
        "accessCode": 47204243,
        "creator": 88288828,
        "school": "gbis",
        "date": "2022-07-24T02:07:39.196Z",
        "__v": 0
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62dca9834d716e00046314a7",
        "firstname": "Joyce",
        "lastname": "Martins",
        "username": "2022/SDT/60372",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$fiyYymMmeHgQcBV5fz1AuOv59RPX0me.f2ZuclEaN5IY8LATDdMum",
        "gender": "female",
        "accessCode": 81518810,
        "creator": 88288828,
        "school": "gsst",
        "date": "2022-07-24T02:08:03.462Z",
        "__v": 0,
        "activeExam": "qrpQj8veJF",
        "completed": True
    },
    {
        "role": "student",
        "regType": "add",
        "_id": "62dca99c4d716e00046314a8",
        "firstname": "Rejoice",
        "lastname": "Martins",
        "username": "2022/SDT/60504",
        "className": "jss-2",
        "category": "junior",
        "password": "$2a$10$7Ff1tD1fO00hnBY4ZlIbDOZi0h5nPoQtfbgIyYR2JP4KYYbjFGVtG",
        "gender": "female",
        "accessCode": 18990523,
        "creator": 88288828,
        "school": "gsst",
        "date": "2022-07-24T02:08:28.593Z",
        "__v": 0,
        "activeExam": "Zf4h7avkUh",
        "completed": True
    }
]


def get_cbt_users():
    items = CbtUser.objects.all()
    cbt_users = []
    for item in items:
        cbt_users.append(item)
    users = cbt_users
    if production:
        response = urllib.request.urlopen(f'{base_url}/benion-cbt/api/users').read()
        json_data = json.loads(response)
        users = json_data['data']['allCbtUsers']
    return users
