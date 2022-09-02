import json
import urllib.request
from benion_tech_django.settings import env
from user_app.models import GalleryImage

base_url = 'https://benion-tech-server.herokuapp.com'
production = env('PRODUCTION') == 'True'
data = [
    {
        "caption": "benion-cryptoapp",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-cryptoapp_1641874992997?alt=media&token=cab291d2-5fb1-40b6-9d4e-15d1c959a3b5",
        "link": "https://benion-cryptoapp.netlify.app/",
        "tag": "react",
        "$key": "-Mt6N2xT82pQryvYsWzA"
    },
    {
        "caption": "Winifred Mough Amap Close Residence",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FWinifred%20Mough%20Amap%20Close%20Residence_1630659852585?alt=media&token=92c46861-6c28-4261-a21c-488d34c5eed4",
        "link": "",
        "tag": "express",
        "$key": "-MiethxVxahQfrTl43r7"
    },
    {
        "caption": "Iorver Mough Mbayar Residence",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FIorver%20Mough%20Mbayar%20Residence_1630659825650?alt=media&token=f5295bf3-d772-4740-b154-ce4de166d828",
        "link": "",
        "tag": "express",
        "$key": "-MietbJzAYF5pwYuL9NI"
    },
    {
        "caption": "Benion Ungwan Yelwa Television, Majelisa Street Residence",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FBenion%20Ungwan%20Yelwa%20Television%2C%20Majelisa%20Street%20Residence_1630659804918?alt=media&token=ae6f332a-4759-4adf-bfd1-9b5f31bdfc94",
        "link": "",
        "tag": "express",
        "$key": "-MietXLzEtCmBGxzX9Dl"
    },
    {
        "caption": "Benion NorthBank Residence, James Onyeke Street",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FBenion%20NorthBank%20Residence%2C%20James%20Onyeke%20Street_1630659781167?alt=media&token=5f533652-9763-4cdc-9c38-db7c237e9cc2",
        "link": "",
        "tag": "express",
        "$key": "-MietRQb3pBaI3e3jLBs"
    },
    {
        "caption": "code-cp",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fcode-cp_1628849604155?alt=media&token=4b87bece-2eb1-4576-a663-2a809819b017",
        "link": "",
        "tag": "express",
        "$key": "-Mgz-8ojbBeJkZApHywh"
    },
    {
        "caption": "Benion Tech Light",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FBenion%20Tech%20Light_1628849472516?alt=media&token=8ddc7b9c-bfb3-427e-94bd-be7371a21af6",
        "link": "",
        "tag": "express",
        "$key": "-Mgyzd_pus9J-0wRQRpr"
    },
    {
        "caption": "Benion Tech Dark",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FBenion%20Tech%20Dark_1628849421576?alt=media&token=594c2f17-e9ea-4da2-ae5a-8ccb827df428",
        "link": "",
        "tag": "express",
        "$key": "-MgyzSJBeCZLTB_ezK0c"
    },
    {
        "caption": "UAM/JOSTUM Block B",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FUAM%2FJOSTUM%20Block%20B_1627295515841?alt=media&token=3a1dac0b-4606-4b08-a81d-cc9926d75a41",
        "link": "",
        "tag": "express",
        "$key": "-MfVe2eNuIz26qjaGuK3"
    },
    {
        "caption": "Benion Profile Photo",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FBenion%20Profile%20Photo_1627295433685?alt=media&token=279809cc-8bab-4928-a663-9fa9ef67186c",
        "link": "",
        "tag": "express",
        "$key": "-MfVdjPeyY7iEIYb7vMW"
    },
    {
        "caption": "benion-wildfire-tracker",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-wildfire-tracker_1617068410033?alt=media&token=0f028b98-c221-47a1-9bfc-fda51352b88f",
        "link": "https://benion28.github.io/benion-wildfire-tracker/",
        "tag": "react",
        "$key": "-MX-mTds8SqMGsJDD978"
    },
    {
        "caption": "benion-paystack-payment",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-paystack-payment_1616193401779?alt=media&token=38b6e482-fccc-441f-b89b-ff97a8cbd0af",
        "link": "https://benion-paystack-payment.herokuapp.com/",
        "tag": "express",
        "$key": "-MWBcZgYXKD9wRrVKfFR"
    },
    {
        "caption": "National Park Service Logo",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FNational%20Park%20Service%20Logo_1598228034171?alt=media&token=192cde6c-b0a4-4e25-a3eb-d46192999865",
        "link": "",
        "tag": "express",
        "$key": "-MFSnyF0jOHXv4wEVPwy"
    },
    {
        "caption": "Dinosaur 2",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FDinosaur%202_1597964842513?alt=media&token=ad262382-fa5c-4759-83d7-3451bd77fa49",
        "link": "",
        "tag": "express",
        "$key": "-MFD6w8VU0Vky3XT2Bum"
    },
    {
        "caption": "Dinosaur 1",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2FDinosaur%201_1597963884307?alt=media&token=b51dd88f-3ef1-4151-85b4-43dd987242de",
        "link": "",
        "tag": "express",
        "$key": "-MFD3IQ_L6Ifrq-gpMfa"
    },
    {
        "caption": "benion-user-request",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-user-request_1594862628503?alt=media&token=0fb13590-ef4a-4f61-94b0-f62689f058a5",
        "link": "https://benion-user-request.herokuapp.com/",
        "tag": "express",
        "$key": "-MCKD8M1oiol6Rwx5FNl"
    },
    {
        "caption": "benion-story-books",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-story-books_1594862251214?alt=media&token=56015d44-95e3-4982-8afb-a5bd19abd27d",
        "link": "https://benion-story-books.herokuapp.com/",
        "tag": "express",
        "$key": "-MCKBgTK_FqVErgQ_Adb"
    },
    {
        "caption": "benion-login-page",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-login-page_1594862207928?alt=media&token=7028b542-fe2a-4a79-bd08-c4cec9e98e2a",
        "link": "https://benion28.github.io/benion-login-page/",
        "tag": "vanilla",
        "$key": "-MCKBXLC4I6bnYL9AQOF"
    },
    {
        "caption": "benion-image-gallery",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-image-gallery_1594862161599?alt=media&token=6d50a97a-8208-4559-adaa-f9ca06f3bfc2",
        "link": "https://benion-image-gallery.firebaseapp.com/",
        "tag": "angular",
        "$key": "-MCKBLm_HKgMKOTe03mz"
    },
    {
        "caption": "benion-breaking-bad",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-breaking-bad_1594862112580?alt=media&token=9d31f9d0-9828-48a3-98db-6aa4a32b5adc",
        "link": "https://benion28.github.io/benion-breaking-bad/",
        "tag": "react",
        "$key": "-MCKB9oFj0SLeb59laR7"
    },
    {
        "caption": "benion-blog-card",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-blog-card_1594861033936?alt=media&token=f254e9ae-9c8b-4635-8bc4-f9b5bacfa438",
        "link": "https://benion28.github.io/benion-blog-card/",
        "tag": "vanilla",
        "$key": "-MCK75V-jkjyMiza9kXo"
    },
    {
        "caption": "benion-ad-manager",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-ad-manager_1594860993092?alt=media&token=04cc4bcd-adaa-4ee1-829d-4a509be51285",
        "link": "https://benion28.github.io/benion-ad-manager/",
        "tag": "vanilla",
        "$key": "-MCK6tbjw6W3mKDjrBdZ"
    },
    {
        "caption": "technology",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Ftechnology_1594857543151?alt=media&token=8f4d8fef-71c3-4751-b494-b15de13896af",
        "link": "",
        "tag": "express",
        "$key": "-MCJujbTJVPckjw8aOl1"
    },
    {
        "caption": "smart-city",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fsmart-city_1594857512741?alt=media&token=c6b04999-5005-4132-a545-51cb65de772c",
        "link": "",
        "tag": "express",
        "$key": "-MCJucyHz3ojNnRGA7a1"
    },
    {
        "caption": "responsive-login-form",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fresponsive-login-form_1594857379916?alt=media&token=43bd797a-a200-437e-bd7e-50f2c58d6770",
        "link": "https://benion28.github.io/responsive-login-form/",
        "tag": "vanilla",
        "$key": "-MCJu6BwcIk5nS_kY8kf"
    },
    {
        "caption": "responsive-animated-navbar",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fresponsive-animated-navbar_1594857183404?alt=media&token=dfcdd51b-895c-4a57-9f6c-512d1e5de8ec",
        "link": "https://benion28.github.io/responsive-animated-navbar/",
        "tag": "vanilla",
        "$key": "-MCJtM7c0Y6F-xAoT7mS"
    },
    {
        "caption": "product-card",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fproduct-card_1594857144202?alt=media&token=e96afdd2-4db3-4003-87c9-6e64c166ebf7",
        "link": "https://benion28.github.io/product-card/",
        "tag": "vanilla",
        "$key": "-MCJtCnFUDR76PN1gfvO"
    },
    {
        "caption": "laptop",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Flaptop_1594857081473?alt=media&token=9aafd07a-76ce-497b-95b9-fa506cb1f82c",
        "link": "",
        "tag": "express",
        "$key": "-MCJszgSZ_-39DI6z6S8"
    },
    {
        "caption": "ict",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fict_1594857042147?alt=media&token=0b29bd91-d8f7-4e8c-bb8b-650a3fed8431",
        "link": "",
        "tag": "express",
        "$key": "-MCJssFnrPlzfuxU7I4A"
    },
    {
        "caption": "breathe-relax-app",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbreathe-relax-app_1594857002994?alt=media&token=69820ce2-6be0-4634-ac66-47fbd700ccb3",
        "link": "https://benion28.github.io/breathe-relax-app/",
        "tag": "vanilla",
        "$key": "-MCJsfCFLGEEX8P14Edk"
    },
    {
        "caption": "benion-tech-fb-icon",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fbenion-tech-fb-icon_1594856948707?alt=media&token=3904d6ba-05dd-4dca-a8bf-c57fdc6f7983",
        "link": "",
        "tag": "express",
        "$key": "-MCJsUMHl4b0hRyzD0Z9"
    },
    {
        "caption": "benion-tech-fb-banner",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fbenion-tech-fb-banner_1594856905421?alt=media&token=8c7f4f18-6e47-4a98-a021-018ae1394a3b",
        "link": "",
        "tag": "express",
        "$key": "-MCJsLSe0focdwOxFXxk"
    },
    {
        "caption": "benion-tech-banner",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fbenion-tech-banner_1594856868867?alt=media&token=2a58cc8e-02ce-412f-86f5-a506e2d9fe3f",
        "link": "",
        "tag": "express",
        "$key": "-MCJsB6EgNyZ0Lg4c6k5"
    },
    {
        "caption": "benion-tailwind",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-tailwind_1594856832017?alt=media&token=cf17b716-4ab6-4b69-bb90-6504000575bc",
        "link": "https://benion28.github.io/benion-tailwind/",
        "tag": "vanilla",
        "$key": "-MCJs0qVfU28c-5ixeDP"
    },
    {
        "caption": "benion-project",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-project_1594856760643?alt=media&token=9cbdd330-9cf9-42cb-ba81-8b9b4fc859b8",
        "link": "https://benion28.github.io/benion-project/",
        "tag": "angular",
        "$key": "-MCJrnRhb03JTy_aG5l5"
    },
    {
        "caption": "benion-portfolio",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-portfolio_1594856720418?alt=media&token=bfbb1bb6-1c91-44ea-87a6-4411698dba32",
        "link": "https://github.com/benion28/benion-portfolio/",
        "tag": "vanilla",
        "$key": "-MCJraElnnal-va48GB-"
    },
    {
        "caption": "benion-passport-login",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-passport-login_1594792243152?alt=media&token=0bb89b73-a056-4030-9eb8-1e14997f98de",
        "link": "https://benion-passport-login.herokuapp.com/",
        "tag": "express",
        "$key": "-MCG0pKx2T7gjkv6GOJA"
    },
    {
        "caption": "benion-parcel",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-parcel_1594792182070?alt=media&token=89e78dcb-160f-4d2f-a096-158b80e399b5",
        "link": "https://benion28.github.io/benion-parcel/",
        "tag": "vanilla",
        "$key": "-MCG0Pd5sRSw7eaCMT-p"
    },
    {
        "caption": "benion-health-panel",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-health-panel_1594792114454?alt=media&token=aa935b8e-d768-4de6-9eb0-a0e47216448c",
        "link": "https://benion28.github.io/benion-health-panel/",
        "tag": "vanilla",
        "$key": "-MCG0BShMxuaGblEmqgr"
    },
    {
        "caption": "benion-firebase-crud",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-firebase-crud_1594792045608?alt=media&token=2c40fe7a-12e5-4d67-9ecd-a8dab71b7945",
        "link": "https://benion28.github.io/benion-firebase-crud/",
        "tag": "react",
        "$key": "-MCG-ufP5r8x9OtJdw-I"
    },
    {
        "caption": "benion-express",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-express_1594791870700?alt=media&token=69129049-073b-41ae-bc64-7423c926c9be",
        "link": "https://benion-express.herokuapp.com/",
        "tag": "express",
        "$key": "-MCG-FmHItqlinXnD2mk"
    },
    {
        "caption": "benion-expense-tracker-react",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-expense-tracker-react_1594791806594?alt=media&token=b97f3f2c-8542-4e42-89ca-23b14a1fc1a7",
        "link": "https://benion28.github.io/benion-expense-tracker-react/",
        "tag": "react",
        "$key": "-MCG--gAMtTy3IBDxFbo"
    },
    {
        "caption": "benion-expense-tracker-mern",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-expense-tracker-mern_1594791732485?alt=media&token=4517c6be-39c4-449c-8dcf-b2b8f6ac9986",
        "link": "https://benion-expense-tracker.herokuapp.com/",
        "tag": "express",
        "$key": "-MCFzgjmW4LRwWXXo0-3"
    },
    {
        "caption": "benion-dashboard",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-dashboard_1594791647745?alt=media&token=798b036d-69ca-49fe-bd94-422ddae6a1cb",
        "link": "https://benion-dashboard.firebaseapp.com/",
        "tag": "angular",
        "$key": "-MCFzORBpo1qvIvAo2RY"
    },
    {
        "caption": "benion-chat-room",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-chat-room_1594791552545?alt=media&token=c1800689-23f3-475f-a03f-c8f0c24bbfde",
        "link": "https://benion-chat-room.herokuapp.com/",
        "tag": "express",
        "$key": "-MCFz-X0ZlEA9p4ltJE-"
    },
    {
        "caption": "benion-animated-moving-car",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-animated-moving-car_1594791494004?alt=media&token=39894101-a46b-4931-aca9-54f11215b79e",
        "link": "https://benion28.github.io/benion-animated-moving-car/",
        "tag": "vanilla",
        "$key": "-MCFyoKsrTjXKjNX5x2u"
    },
    {
        "caption": "benion-animated-counter",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbenion-animated-counter_1594791432217?alt=media&token=ca2954ad-9e06-4b9c-9e21-735ea36695e6",
        "link": "https://benion28.github.io/benion-animated-counter/",
        "tag": "vanilla",
        "$key": "-MCFyZl6HuotZyOr4WZK"
    },
    {
        "caption": "animated-profile-card",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fanimated-profile-card_1594791361618?alt=media&token=8238deb6-9631-4bfc-b34e-352818281106",
        "link": "https://benion28.github.io/animated-profile-card/",
        "tag": "vanilla",
        "$key": "-MCFyHcDK6ZSRxZSx8fr"
    },
    {
        "caption": "add_photo",
        "category": "Others",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Others%2Fadd_photo_1594791320106?alt=media&token=c85f2ec7-ce78-451d-b3b9-4fe64d91014e",
        "link": "",
        "tag": "express",
        "$key": "-MCFy6GKidn7DtuNIkxx"
    },
    {
        "caption": "breathe-relax-app",
        "category": "Works",
        "image": "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Works%2Fbreathe-relax-app_1594791261884?alt=media&token=cf10f56d-1671-47a2-a125-c78efa882347",
        "link": "https://benion28.github.io/breathe-relax-app/",
        "tag": "vanilla",
        "$key": "-MCFxuCSr2Ods-ImISTC"
    }
]


def get_images():
    items = GalleryImage.objects.all()
    images = []
    for item in items:
        images.append(item)
    all_images = images
    if production:
        response = urllib.request.urlopen(f'{base_url}/benion-users/api/all-images').read()
        json_data = json.loads(response)
        all_images = json_data['data'][3]
    return all_images


def category_images(value):
    images = get_images()
    items = []
    for image in images:
        if production:
            if image["category"] == value:
                items.append(image)
        else:
            if image.category == value:
                items.append(image)
    return items


def single_image_id(value):
    images = get_images()
    item = {}
    for image in images:
        if production:
            if image["id"] == int(value):
                item = image
        else:
            if image.id == int(value):
                item = image
    return item


def single_image(value):
    images = get_images()
    item = {}
    for image in images:
        if production:
            if image["caption"] == value:
                item = image
        else:
            if image.caption == value:
                item = image
    return item
